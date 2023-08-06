from ssql import Class
from ssql.__types import Condition

from typing import Any, List
import sqlite3


class ClassNotSupportedException(Exception):
    def __init__(self, cls: type) -> None:
        super().__init__(f"This database does not support the {cls.__name__} class")


class Selection:
    def __init__(self, cursor: sqlite3.Cursor, cls: type) -> None:
        self.__cursor = cursor
        self.__cls = cls
        self.__query = f"SELECT * FROM {self.__cls.__name__} WHERE 1 = 1"
        self.__cursor.execute(self.__query)

    def where(
        self, condition: Condition
    ) -> "Selection":  # NOTE: Maybe have a where function, and function, or function, etc.
        self.__query += f" AND {str(condition)}"
        self.__cursor.execute(self.__query)
        return self

    def first(self) -> object:
        return self.__cls.__from_row__(self.__cls, self.__cursor.fetchone())

    def all(self) -> List[object]:
        return [
            self.__cls.__from_row__(self.__cls, row) for row in self.__cursor.fetchall()
        ]


class Database:
    def __init__(self, path: str, classes: List[Class]) -> None:
        self.__classes = set()
        for cls in classes:
            if not issubclass(cls, Class):
                raise TypeError(f"{cls.__name__} is not a valid sql class")
            self.__classes.add(cls)

        self.__setup_database(path)

    def __setup_database(self, path: str) -> None:
        self.__connection = sqlite3.connect(path)
        self.__connection.row_factory = sqlite3.Row

        self.__cursor = self.__connection.cursor()

        self.__create_tables()

    def __create_tables(self) -> None:
        for cls in self.__classes:
            self.__cursor.execute(cls.__create_table__(cls))

    def __support_check(self, cls_or_instance: Any) -> None:
        if isinstance(cls_or_instance, type):
            if cls_or_instance not in self.__classes:
                raise ClassNotSupportedException(cls_or_instance)
        elif type(cls_or_instance) not in self.__classes:
            raise ClassNotSupportedException(type(cls_or_instance))

    def insert(self, instance: object) -> None:
        self.__support_check(instance)

        try:
            self.__cursor.execute(instance.__insert_query__(), instance.__values__())
        except sqlite3.IntegrityError:
            raise ValueError(f"Value {instance} already exists in database")
        self.__connection.commit()

    # Can be called like `database.select(User).where(User.id == 5).first()`
    def select(self, cls: Class) -> Selection:
        return Selection(self.__cursor, cls)
