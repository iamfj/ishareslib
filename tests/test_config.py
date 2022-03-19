from ishareslib.config import Config
from ishareslib.core.user_agent_adapter import UserAgentAdapter
from ishareslib.ext.user_agent.human_user_agent_adapter import HumanUserAgentAdapter


class DummyUserAgentAdapter(UserAgentAdapter):
    def __init__(self):
        super().__init__()

    def new_user_agent(self) -> str:
        return "New Dummy User Agent"


def test_get_user_agent_adapter_with_default():
    config = Config()
    assert isinstance(config.get_user_agent_factory(), HumanUserAgentAdapter)


def test_get_user_agent_adapter_with_custom():
    config = Config(user_agent_adapter=DummyUserAgentAdapter())
    assert isinstance(config.get_user_agent_factory(), DummyUserAgentAdapter)
