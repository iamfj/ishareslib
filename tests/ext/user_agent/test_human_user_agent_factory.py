from ishareslib.ext.user_agent.human_user_agent_factory import HumanUserAgentFactory


def test_get_user_agent():
    factory = HumanUserAgentFactory()
    previous_user_agent = factory.get_user_agent()
    current_user_agent = factory.get_user_agent()
    assert previous_user_agent == current_user_agent


def test_new_user_agent():
    factory = HumanUserAgentFactory()
    for i in range(1000):
        previous_user_agent = factory.get_user_agent()
        new_user_agent = factory.new_user_agent()
        assert previous_user_agent != new_user_agent
