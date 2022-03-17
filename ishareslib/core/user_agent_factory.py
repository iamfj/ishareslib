from abc import ABC, abstractmethod


class UserAgentFactory(ABC):
    @abstractmethod
    def get_user_agent(self) -> str:
        pass

    @abstractmethod
    def new_user_agent(self) -> str:
        pass
