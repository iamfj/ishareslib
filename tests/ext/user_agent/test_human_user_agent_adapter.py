from ishareslib.ext.user_agent.human_user_agent_adapter import HumanUserAgentAdapter


def test_get_user_agent():
    adapter = HumanUserAgentAdapter()
    user_agent = adapter.get_user_agent()
    assert user_agent.__contains__("Mozilla")
