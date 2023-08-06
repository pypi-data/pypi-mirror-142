from pyssql.__types import Type

from typing import Any


class Class:
    def __init_subclass__(cls: Any) -> None:
        cls.__sql_types__ = {}
        for name, value in cls.__annotations__.items():
            # Distinguishing between `name: type` and `name: type()`
            if isinstance(value, type):
                continue

            # Making sure all the attributes are sql types
            if not isinstance(value, Type):
                continue

            cls.__sql_types__[name] = value

        for name, value in cls.__sql_types__.items():
            # Creating the attribute
            setattr(cls, name, value)
            value.__attribute_name__ = name
            value._class = cls

    def __getattribute__(self, name: str) -> Any:
        attribute = super().__getattribute__(name)
        if isinstance(attribute, Type):
            return attribute.get(self)
        return attribute

    def __setattr__(self, name: str, value: Any) -> None:
        # If it's an sql type
        if name in self.__sql_types__:
            self.__sql_types__[name].set(self, value)
        else:
            super().__setattr__(name, value)

    def __create_table__(cls) -> str:
        columns = []
        for name, type in cls.__sql_types__.items():
            columns.append(type.__create_table_column__())
        return f"CREATE TABLE IF NOT EXISTS {cls.__name__} ({', '.join(columns)});"

    def __insert_query__(self) -> str:
        columns = []
        values = []
        for name, type in self.__sql_types__.items():
            columns.append(name)
            values.append(f"?")
        return f"INSERT INTO {self.__class__.__name__} ({', '.join(columns)}) VALUES ({', '.join(values)});"

    def __values__(self) -> tuple:
        values = []
        for name, type in self.__sql_types__.items():
            values.append(type.get(self))
        return tuple(values)

    def __from_row__(cls, row: dict) -> object:
        instance = cls.__new__(cls)
        for name, type in cls.__sql_types__.items():
            type.set(instance, row[name])
        if hasattr(cls, "on_load"):
            cls.on_load(instance)
        return instance
