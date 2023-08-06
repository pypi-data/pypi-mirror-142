import inspect
import os
import re
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
)

from smartparams.cli import Print, parse_arguments
from smartparams.io import load_data, print_data, save_data
from smartparams.options import Option
from smartparams.utils import (
    check_key_is_in,
    check_missings,
    check_overrides,
    check_typings,
    convert_to_primitive_types,
    flatten_keys,
    get_nested_dictionary_and_key,
    get_object_name,
    import_callable,
    join_keys,
    join_objects,
    parse_object,
    parse_param,
    remove_duplicated_key_and_value,
    str_to_bool,
)

T = TypeVar('T')


class Smart(Generic[T]):
    """Creates a partial wrapper for a class that can be configurable from a file or a cli.

    Smart class has functionality of both partial and dict classes. It allows creating
    objects with lazy instantiating. This makes possible injecting values from config
    file or command line.

    Examples:
        # script.py
        from dataclasses import dataclass
        from pathlib import Path

        from smartparams import Smart


        @dataclass
        class Params:
            value: str


        def main(smart: Smart[Params]) -> None:
            params = smart()
            # do some stuff ...


        if __name__ == '__main__':
            Smart.strict = True
            Smart(Params).run(
                function=main,
                path=Path('params.yaml'),
            )

        #  Run in command line:
        #    $ python script.py value="Some value"
        #    $ python script.py --dump
        #    $ python script.py
        #    $ python script.py --print keys
        #    $ python script.py --help


    Attributes:
        keyword: Name of the key containing the value with the path of the class to be imported.
            Can be set by env variable SMARTPARAMS_KEYWORD, default 'class'.
        missing_value: Value assigned to unknown types when creating a representation.
            Can be set by env variable SMARTPARAMS_MISSING_VALUE, default '???'.
        check_missings: Whether to check missing values before instantiating object.
            Can be set by env variable SMARTPARAMS_CHECK_MISSINGS, default 'true'.
        check_typings: Whether to check arguments type before instantiating object.
            Can be set by env variable SMARTPARAMS_CHECK_TYPINGS, default 'true'.
        check_overrides: Whether to check override arguments before instantiating object.
            Can be set by env variable SMARTPARAMS_CHECK_OVERRIDES, default 'true'.
        allow_only_registered_classes: Whether to allow import only registered classes.
            Can be set by env variable SMARTPARAMS_ALLOW_ONLY_REGISTERED_CLASSES, default 'false'.
        strict: Whether to raise exceptions instead of warnings.
            Can be set by env variable SMARTPARAMS_STRICT, default 'false'.

    """

    keyword: str = os.getenv('SMARTPARAMS_KEYWORD', default='class')
    missing_value: str = os.getenv('SMARTPARAMS_MISSING_VALUE', default='???')

    check_missings: bool = str_to_bool(os.getenv('SMARTPARAMS_CHECK_MISSINGS', default='true'))
    check_typings: bool = str_to_bool(os.getenv('SMARTPARAMS_CHECK_TYPINGS', default='true'))
    check_overrides: bool = str_to_bool(os.getenv('SMARTPARAMS_CHECK_OVERRIDES', default='true'))

    allow_only_registered_classes: bool = str_to_bool(
        os.getenv('SMARTPARAMS_ALLOW_ONLY_REGISTERED_CLASSES', default='false'),
    )

    strict: bool = str_to_bool(os.getenv('SMARTPARAMS_STRICT', default='false'))

    _aliases: Dict[str, str] = dict()
    _origins: Dict[str, str] = dict()

    def __init__(
        self,
        _class: Callable[..., T] = cast(Callable[..., T], dict),
        /,
        **kwargs: Any,
    ) -> None:
        """Creates instance of Smart class.

        Args:
            _class: Class to be wrapped.
            **kwargs: Partial keyword arguments to be passed to the class constructor.

        """
        self._class: Callable[..., T] = _class
        self._params: Dict[str, Any] = dict()

        self._location: str = ''

        for k, v in kwargs.items():
            self.set(k, v)

    @property
    def type(self) -> Callable[..., T]:
        return self._class

    @property
    def dict(self) -> Dict[str, Any]:
        return self._params.copy()

    def __call__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> T:
        """Creates instance of given type.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            An class instance.

        """
        params = self._init_dict(
            dictionary=self._params,
            location=self._location,
        )

        callable_name = join_objects(self._location, get_object_name(self._class))

        if self.check_overrides:
            check_overrides(
                params=params,
                kwargs=kwargs,
                callable_name=callable_name,
                raise_error=self.strict,
            )

        params.update(kwargs)

        return self._instantiate(
            location=self._location,
            callable_name=callable_name,
            callable_=self._class,
            args=args,
            kwargs=params,
        )

    def __str__(self) -> str:
        class_string = "" if self._class is dict else f"[{get_object_name(self._class)}]"
        params_string = ", ".join((f"{k}={v}" for k, v in self._params.items()))
        return f"{self.__class__.__name__}{class_string}({params_string})"

    def __repr__(self) -> str:
        return str(self)

    def keys(
        self,
        flatten: bool = False,
        pattern: Optional[str] = None,
    ) -> Iterable[str]:
        """Generates keys existing in the dictionary.

        Args:
            flatten: Whether to return the flattened keys in the nested dictionaries.
            pattern: Regex pattern for filtering keys.

        Yields:
            Keys from dictionary.

        """
        keys = flatten_keys(self._params) if flatten else self._params
        if pattern is None:
            yield from keys
        else:
            yield from (key for key in keys if re.fullmatch(pattern, key))

    def values(
        self,
        flatten: bool = False,
        pattern: Optional[str] = None,
    ) -> Iterable[Any]:
        """Generates values existing in the dictionary.

        Args:
            flatten: Whether to return the values in the nested dictionaries.
            pattern: Regex pattern for filtering values by key.

        Yields:
            Values from dictionary.

        """
        return (self.get(k) for k in self.keys(flatten, pattern))

    def items(
        self,
        flatten: bool = False,
        pattern: Optional[str] = None,
    ) -> Iterable[Tuple[str, Any]]:
        """Generates items existing in the dictionary.

        Args:
            flatten: Whether to return the items in the nested dictionaries.
            pattern: Regex pattern for filtering items by key.

        Yields:
            Items from dictionary.

        """
        return ((k, self.get(k)) for k in self.keys(flatten, pattern))

    def isin(
        self,
        name: str,
    ) -> bool:
        """Checks if name is in dictionary.

        Args:
            name: The key to be checked.

        Returns:
            True if name is in dictionary, otherwise False.

        """
        return check_key_is_in(name, self._params)

    def get(
        self,
        name: str,
        default: Optional[Any] = ...,
    ) -> Any:
        """Returns value of given name from dictionary.

        Args:
            name: The key of value.
            default: Value returned if key doesn't exist.

        Returns:
            Value matched with given name.

        Raises:
            ValueError if name doesn't exist and default value not specified.

        """
        dictionary, key = get_nested_dictionary_and_key(
            dictionary=self._params,
            name=name,
            required=default is ...,
        )
        return dictionary.get(key, default)

    def set(
        self,
        name: str,
        value: Any,
    ) -> Any:
        """Sets new value of given name in dictionary.

        Args:
            name: The key of value.
            value: Value to be set.

        Returns:
            The given value.

        """
        dictionary, key = get_nested_dictionary_and_key(
            dictionary=self._params,
            name=name,
            set_mode=True,
        )
        dictionary[key] = value
        return value

    def pop(
        self,
        name: str,
        default: Optional[Any] = ...,
    ) -> Any:
        """Removes and returns value of given name from dictionary.

        Args:
            name: The key of value.
            default: Value returned if key doesn't exist.

        Returns:
            Removed value.

        Raises:
            ValueError if name doesn't exist and default value not specified.

        """
        dictionary, key = get_nested_dictionary_and_key(
            dictionary=self._params,
            name=name,
            required=default is ...,
        )
        return dictionary.pop(key, default)

    def map(
        self,
        name: str,
        function: Callable,
    ) -> Any:
        """Applies value of given name to given function.

        Args:
            name: Name of value to be mapped.
            function: A function to which map passes a value.

        Returns:
            Mapped value.

        Raises:
            ValueError if name doesn't exist.

        """
        dictionary, key = get_nested_dictionary_and_key(
            dictionary=self._params,
            name=name,
            required=True,
        )

        dictionary[key] = value = function(dictionary[key])
        return value

    def update_from(
        self,
        source: Union['Smart', Mapping[str, Any], Sequence[str], Path],
        name: Optional[str] = None,
        override: bool = True,
        required: bool = True,
    ) -> 'Smart':
        """Inserts items from given source.

        Args:
            source: Smart object, dictionary, list or path of items to insert.
            name: Key of source dictionary to insert.
            override: Whether to override existing items.
            required: Whether the name is required to exist.

        Returns:
            Smart instance.

        Raises:
            TypeError if given source is not supported.

        """
        smart: Smart
        if isinstance(source, Smart):
            smart = source
        elif isinstance(source, Mapping):
            smart = Smart(**source)
        elif isinstance(source, Sequence):
            smart = Smart(**dict(map(parse_param, source)))
        elif isinstance(source, Path):
            smart = Smart(**load_data(source))
        else:
            raise TypeError(f"Source type '{type(source)}' is not supported.")

        if name is None:
            for key in smart.keys(flatten=True):
                if override or not self.isin(key):
                    self.set(key, smart.get(key))
        else:
            try:
                self.update_from(
                    source=smart.get(name, default=... if required else dict()),
                    override=override,
                )
            except Exception as e:
                raise RuntimeError(f"Cannot update with source name '{name}'. " + ' '.join(e.args))

        return self

    @classmethod
    def load_from(
        cls,
        source: Union['Smart', Mapping[str, Any], Sequence[str], Path],
        name: Optional[str] = None,
    ) -> Any:
        """Loads object from the given source.

        Args:
            source: Smart object, dictionary, list or path of object to load.
            name: Key of source dictionary.

        Returns:
            Instance of loaded source.

        Raises:
            TypeError if given source is not supported.

        """
        return cls().update_from(source=source, name=name).init()

    def init(
        self,
        name: Optional[str] = None,
        persist: bool = True,
    ) -> Any:
        """Instantiates dictionary with given name.

        Args:
            name: Key of dictionary to be instantiated.
            persist: Whether to keep instantiated object in dictionary.

        Returns:
            Object of instantiated class.

        """
        if name is None:
            obj = self._init_object(
                obj=self.dict,
                location=self._location,
            )
        else:
            obj = self._init_object(
                obj=self.get(name),
                location=join_keys(self._location, name),
            )

            if persist:
                return self.set(name, obj)

        return obj

    def representation(
        self,
        skip_defaults: bool = False,
        merge_params: bool = False,
    ) -> Dict[str, Any]:
        """Creates representation of Smart object.

        Args:
            skip_defaults: Whether to skip arguments with default values.
            merge_params: Whether to join items from dictionary.

        Returns:
            Dictionary with Smart representation.

        """
        smart: Smart = Smart()

        if merge_params:
            smart.update_from(self)

        smart.update_from(
            source=self._object_representation(
                obj=self._class,
                skip_default=skip_defaults,
            ),
            override=False,
        )

        return convert_to_primitive_types(
            obj=smart.dict,
            missing_value=self.missing_value,
        )

    @classmethod
    def register(
        cls,
        classes: Union[
            Sequence[Union[str, Callable]],
            Mapping[str, str],
            Mapping[Callable, str],
            Mapping[Union[str, Callable], str],
        ],
        prefix: str = '',
    ) -> Type['Smart']:
        """Registers classes to be imported.

        Args:
            classes: Class list or dict with aliases to be registered.
            prefix: Prefix string added to alias.

        Returns:
            Smart object.

        """
        if isinstance(classes, Sequence):
            cls._register_classes(
                classes=classes,
                prefix=prefix,
            )
        elif isinstance(classes, Mapping):
            cls._register_aliases(
                aliases=classes,
                prefix=prefix,
            )
        else:
            raise TypeError(f"Register classes type '{type(classes)}' is not supported.")

        return cls

    def run(
        self,
        function: Optional[Callable[['Smart'], Any]] = None,
        path: Optional[Path] = None,
    ) -> 'Smart':
        """Runs main function.

        Args:
            function: Main function to be run.
            path: Path of params file.

        Returns:
            Smart object.

        """
        args = parse_arguments(
            default_path=path,
        )

        if args.strict:
            Smart.strict = True

        if args.path:
            self.update_from(args.path)

        self.update_from(args.params)

        if args.dump:
            if not args.path:
                raise ValueError("Cannot dump params if path is not specified.")

            save_data(
                data=self.representation(
                    skip_defaults=args.skip_defaults,
                    merge_params=args.merge_params,
                ),
                path=args.path,
            )
        elif args.print:
            if args.print == Print.PARAMS:
                print_data(
                    data=self.representation(
                        skip_defaults=args.skip_defaults,
                        merge_params=args.merge_params,
                    ),
                    fmt=args.format,
                )
            elif args.print == Print.KEYS:
                print_data(
                    data=tuple(self.keys(flatten=True)),
                    fmt=args.format,
                )
            else:
                raise NotImplementedError(f"Print '{args.print}' has not been implemented yet.")
        elif function is None:
            self()
        else:
            function(self)

        return self

    def _init_object(
        self,
        obj: Any,
        location: str,
    ) -> Any:
        if isinstance(obj, dict):
            if self.keyword in obj:
                return self._instantiate_from_dict(
                    dictionary=obj,
                    location=location,
                )

            return self._init_dict(
                dictionary=obj,
                location=location,
            )

        if isinstance(obj, list):
            return self._init_list(
                lst=obj,
                location=location,
            )

        return obj

    def _init_dict(
        self,
        dictionary: Dict[str, Any],
        location: str,
    ) -> Dict[str, Any]:
        return {
            key: self._init_object(
                obj=value,
                location=join_keys(location, key),
            )
            for key, value in dictionary.items()
        }

    def _init_list(
        self,
        lst: List[Any],
        location: str,
    ) -> List[Any]:
        return [
            self._init_object(
                obj=element,
                location=join_keys(location, str(index)),
            )
            for index, element in enumerate(lst)
        ]

    def _instantiate_from_dict(
        self,
        dictionary: Dict[str, Any],
        location: str,
    ) -> Any:
        kwargs, name, option = parse_object(
            dictionary=dictionary,
            keyword=self.keyword,
        )

        if name == self.__class__.__name__:
            return self._instantiate(
                location=location,
                callable_name=join_objects(location, self.__class__.__name__),
                callable_=Smart,
                kwargs=kwargs,
            )

        if name in self._origins:
            name = self._origins[name]
        elif self.allow_only_registered_classes:
            raise ImportError(f"Class '{name}' is not registered.")

        callable_ = import_callable(name)
        callable_name = join_objects(location, get_object_name(callable_))

        if option:
            if option == Option.SMART:
                return self._instantiate(
                    location=location,
                    callable_name=callable_name,
                    callable_=Smart,
                    args=(callable_,),
                    kwargs=kwargs,
                )

            if option == Option.TYPE:
                if kwargs:
                    raise ValueError(f"Cannot specify any arguments for {callable_name}'s type.")

                return callable_

            raise ValueError(f"Option '{option}' is not supported.")

        return self._instantiate(
            location=location,
            callable_name=callable_name,
            callable_=callable_,
            kwargs=kwargs,
        )

    def _instantiate(
        self,
        location: str,
        callable_name: str,
        callable_: Callable,
        args: Optional[Tuple[Any, ...]] = None,
        kwargs: Optional[Dict[str, Any]] = None,
    ) -> Any:
        args = args or tuple()
        kwargs = kwargs or dict()

        if self.check_missings:
            check_missings(
                kwargs=kwargs,
                missing_value=self.missing_value,
                callable_name=callable_name,
                raise_error=self.strict,
            )

        if self.check_typings:
            check_typings(
                callable_=callable_,
                args=args,
                kwargs=kwargs,
                callable_name=callable_name,
                raise_error=self.strict,
            )

        try:
            callable_ = callable_(*args, **kwargs)
        except Exception as e:
            raise RuntimeError(f"Error during instantiate '{callable_name}'.") from e
        else:
            if isinstance(callable_, Smart):
                callable_._location = location

            return callable_

    def _object_representation(
        self,
        obj: Any,
        skip_default: bool,
    ) -> Dict[str, Any]:
        representation: Dict[str, Any] = dict()
        signature = inspect.signature(obj)

        for i, param in enumerate(signature.parameters.values()):
            name = param.name
            kind = param.kind
            annotation = param.annotation
            default = param.default

            if not (i == 0 and annotation is param.empty and default is param.empty) or kind in (
                param.POSITIONAL_OR_KEYWORD,
                param.KEYWORD_ONLY,
            ):
                if annotation is Smart or isinstance(default, Smart) and default.type is dict:
                    representation[name] = {
                        self.keyword: self.__class__.__name__,
                    }
                elif get_origin(annotation) is Smart or isinstance(default, Smart):
                    if isinstance(default, Smart):
                        param_type = default.type
                    else:
                        param_type, *_ = get_args(annotation)

                    keyword = inspect.formatannotation(param_type)
                    keyword = self._aliases.get(keyword, keyword)
                    keyword = join_objects(keyword, Option.SMART.value)

                    representation[name] = {
                        self.keyword: keyword,
                        **self._object_representation(
                            obj=param_type,
                            skip_default=skip_default,
                        ),
                    }
                elif default is not param.empty and skip_default:
                    continue
                elif default is None or isinstance(default, (bool, float, int, str)):
                    representation[name] = default
                elif annotation is not param.empty and isinstance(annotation, type):
                    if annotation in (bool, float, int, str):
                        representation[name] = annotation.__name__ + self.missing_value
                    else:
                        keyword = inspect.formatannotation(annotation)
                        keyword = self._aliases.get(keyword, keyword)
                        representation[name] = {
                            self.keyword: keyword,
                            **self._object_representation(
                                obj=annotation,
                                skip_default=skip_default,
                            ),
                        }
                else:
                    representation[name] = self.missing_value

        return representation

    @classmethod
    def _register_classes(
        cls,
        classes: Sequence[Union[str, Callable]],
        prefix: str = '',
    ) -> None:
        cls._register_aliases(
            aliases={c: c if isinstance(c, str) else get_object_name(c) for c in classes},
            prefix=prefix,
        )

    @classmethod
    def _register_aliases(
        cls,
        aliases: Union[
            Mapping[str, str],
            Mapping[Callable, str],
            Mapping[Union[str, Callable], str],
        ],
        prefix: str = '',
    ) -> None:
        for origin, alias in aliases.items():
            origin = origin if isinstance(origin, str) else inspect.formatannotation(origin)
            alias = join_keys(prefix, alias)

            remove_duplicated_key_and_value(
                key=origin,
                key_dict=cls._aliases,
                value_dict=cls._origins,
                message=f"Origin '{origin}' has been overridden.",
                raise_error=cls.strict,
            )

            remove_duplicated_key_and_value(
                key=alias,
                key_dict=cls._origins,
                value_dict=cls._aliases,
                message=f"Alias '{alias}' has been overridden.",
                raise_error=cls.strict,
            )

            cls._aliases[origin] = alias
            cls._origins[alias] = origin
