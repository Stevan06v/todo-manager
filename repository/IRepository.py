from abc import ABC, abstractmethod


# define interface
class IRepository(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplemented

    @abstractmethod
    def create(self, item):
        raise NotImplemented

    @abstractmethod
    def update(self, item):
        raise NotImplemented

    @abstractmethod
    def delete(self, id):
        raise NotImplemented
