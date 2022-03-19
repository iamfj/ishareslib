from ishareslib.core.user_agent_adapter import UserAgentAdapter
from ishareslib.ext.user_agent.human_user_agent_adapter import HumanUserAgentAdapter


class Config:
    def __init__(self, user_agent_adapter: UserAgentAdapter = None):
        self._user_agent_adapter = user_agent_adapter

    def get_user_agent_factory(self):
        if self._user_agent_adapter is None:
            return HumanUserAgentAdapter()
        return self._user_agent_adapter
