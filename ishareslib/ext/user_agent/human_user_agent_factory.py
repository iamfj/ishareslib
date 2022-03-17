from random import choice

from ishareslib.core.user_agent_factory import UserAgentFactory


class HumanUserAgentFactory(UserAgentFactory):
    def __init__(self):
        self._selected_user_agent = None
        self._available_user_agents = [
            "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
            "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)",
            "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
        ]

    def get_user_agent(self) -> str:
        if self._selected_user_agent is None:
            return self.new_user_agent()
        return self._selected_user_agent

    def new_user_agent(self) -> str:
        _previous_user_agent = self._selected_user_agent
        self._selected_user_agent = choice(self._available_user_agents)
        if _previous_user_agent == self._selected_user_agent:
            return self.new_user_agent()
        return self._selected_user_agent
