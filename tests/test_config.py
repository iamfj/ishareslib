from ishareslib.config import Config
from ishareslib.core.user_agent_factory import UserAgentFactory
from ishareslib.ext.user_agent.human_user_agent_factory import HumanUserAgentFactory


class DummyUserAgentFactory(UserAgentFactory):
    def __init__(self):
        super().__init__()

    def new_user_agent(self) -> str:
        return "New Dummy User Agent"


def test_get_user_agent_factory_with_default():
    config = Config()
    assert isinstance(config.get_user_agent_factory(), HumanUserAgentFactory)


def test_get_user_agent_factory_with_custom():
    config = Config(user_agent_factory=DummyUserAgentFactory())
    assert isinstance(config.get_user_agent_factory(), DummyUserAgentFactory)
