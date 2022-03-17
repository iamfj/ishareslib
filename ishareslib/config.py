from ishareslib.core.user_agent_factory import UserAgentFactory
from ishareslib.ext.user_agent.human_user_agent_factory import HumanUserAgentFactory


class Config:
    def __init__(self, user_agent_factory: UserAgentFactory = None):
        self._user_agent_factory = user_agent_factory

    def get_user_agent_factory(self):
        if self._user_agent_factory is None:
            return HumanUserAgentFactory()
        return self._user_agent_factory
