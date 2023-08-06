from enum import Enum
from typing import Any, Optional


def _type_check(value: Any, type: type) -> Optional[TypeError]:
    if value is not None and not isinstance(value, type):
        raise TypeError(f"Value {value!r} is not a valid {type.__name__}")


def _null_check(value: Any, nullable: bool) -> Optional[TypeError]:
    if not nullable and value is None:
        raise TypeError("Value cannot be null")


class SupportsOperators:
    # &
    def __and__(self, other: "Condition") -> "Condition":
        return Condition(self, other, "AND")

    # ==
    def __eq__(self, other: Any) -> "Condition":
        return Condition(self, other, "==")

    # !=
    def __ne__(self, other: Any) -> "Condition":
        return Condition(self, other, "!=")

    # >
    def __gt__(self, other: Any) -> "Condition":
        return Condition(self, other, ">")

    # >=
    def __ge__(self, other: Any) -> "Condition":
        return Condition(self, other, ">=")

    # <
    def __lt__(self, other: Any) -> "Condition":
        return Condition(self, other, "<")

    # <=
    def __le__(self, other: Any) -> "Condition":
        return Condition(self, other, "<=")


class Condition(SupportsOperators):
    def __init__(self, left: Any, right: Any, operator: str) -> None:
        self.__left = left
        self.__right = right
        self.__operator = operator

    def __repr(self, obj: object) -> str:
        if isinstance(obj, Type):
            return obj.__attribute_name__
        elif isinstance(obj, Condition):
            return str(obj)
        return repr(obj)

    def __str__(self) -> str:
        return (
            f"{self.__repr(self.__left)} {self.__operator} {self.__repr(self.__right)}"
        )


class Key(Enum):
    NONE = ""
    PRIMARY = "PRIMARY KEY"
    FOREIGN = "FOREIGN KEY"
    UNIQUE = "UNIQUE"


class Type(SupportsOperators):
    _PYTHON_TYPE: Any
    _SQL_TYPE: str
    __values = {}

    def __init__(
        self,
        not_null: bool = False,
        key: Key = Key.NONE,
        default: Any = None,
    ) -> None:
        self._not_null = not_null
        self._key = key
        self._default = default

        if self._key == Key.PRIMARY:
            self._not_null = True

        if self._not_null and default is not None:
            self.set(self, default)

    def __validate(self, value: Any) -> None:
        _type_check(value, self._PYTHON_TYPE)
        _null_check(value, not self._not_null)

    def __create_table_column__(self) -> str:
        query = f"{self.__attribute_name__} {self._SQL_TYPE}"
        if self._key != Key.NONE:
            query += f" {self._key.value}"
        if self._not_null:
            query += " NOT NULL"
        if self._default is not None:
            query += f" DEFAULT {self._default}"
        return query

    def set(self, instance: Any, value: Any) -> None:
        self.__validate(value)
        self.__values[(self, instance)] = value

    def get(self, instance: Any) -> Any:
        return self.__values[(self, instance)]

    def __hash__(self) -> int:
        return hash((self.__attribute_name__, self._class, self._SQL_TYPE))


class Types:
    class Integer(Type):
        _PYTHON_TYPE = int
        _SQL_TYPE = "INTEGER"

        def __validate(self, value: Any) -> None:
            super().validate(value)

    class String(Type):
        _PYTHON_TYPE = str

        def __init__(self, max_length: int = 255, **kwargs) -> None:
            super().__init__(**kwargs)

            self._SQL_TYPE = f"VARCHAR({max_length})"
            self.max_length = max_length

        def __validate(self, value: Any) -> None:
            super().validate(value)

            if len(value) > self.max_length:
                raise ValueError(f"Value {value!r} is too long")
