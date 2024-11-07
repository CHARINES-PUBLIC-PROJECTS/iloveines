from abc import ABC, abstractmethod

class ContractBase(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def sanitize(self):
        pass
