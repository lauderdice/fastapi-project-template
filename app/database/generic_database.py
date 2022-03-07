import abc
from uuid import UUID


class GenericSQLDatabase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user_name(self, user_id: UUID) -> str:
        pass

