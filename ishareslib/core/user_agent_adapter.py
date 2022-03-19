from abc import ABC, abstractmethod


class UserAgentAdapter(ABC):
    def __init__(self):
        self._user_agent = None

    def get_user_agent(self) -> str:
        if self._user_agent is None:
            return self.new_user_agent()
        return self._user_agent

    @abstractmethod
    def new_user_agent(self) -> str:
        pass
