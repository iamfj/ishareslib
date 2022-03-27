from typing import Union

from pytest import raises

from ishareslib.core.user_agent_adapter import UserAgentAdapter


class DummyUserAgentAdapter(UserAgentAdapter):
    def __init__(self, user_agents: list[str], regeneration_limit: int = 3):
        super().__init__(regeneration_limit=regeneration_limit)
        self._user_agents = user_agents
        self._call_counter = 0

    def _gen_user_agent(self) -> Union[str, None]:
        if len(self._user_agents) <= self._call_counter:
            return None
        user_agent = self._user_agents[self._call_counter]
        self._call_counter += 1
        return user_agent


def test_get_user_agent():
    adapter = DummyUserAgentAdapter(["first", "second"])
    first_user_agent = adapter.get_user_agent()
    second_user_agent = adapter.get_user_agent()
    assert first_user_agent == second_user_agent


def test_get_user_agent_with_no_data():
    adapter = DummyUserAgentAdapter([])
    with raises(ValueError) as exc_info:
        adapter.get_user_agent()
    exception_raised = exc_info.value
    assert str(exception_raised) == "Could not choose a new user agent"


def test_new_user_agent():
    adapter = DummyUserAgentAdapter(["first", "second"])
    first_user_agent = adapter.get_user_agent()
    second_user_agent = adapter.new_user_agent()
    assert "first" == first_user_agent
    assert "second" == second_user_agent


def test_new_with_get_user_agent():
    adapter = DummyUserAgentAdapter(["first", "second"])
    first_user_agent = adapter.new_user_agent()
    second_user_agent = adapter.get_user_agent()
    third_user_agent = adapter.new_user_agent()
    fourth_user_agent = adapter.get_user_agent()
    assert "first" == first_user_agent
    assert first_user_agent == second_user_agent
    assert "second" == third_user_agent
    assert third_user_agent == fourth_user_agent


def test_new_user_agent_with_same_entities():
    adapter = DummyUserAgentAdapter(["first", "second", "second", "third"])
    first_user_agent = adapter.new_user_agent()
    second_user_agent = adapter.new_user_agent()
    third_user_agent = adapter.new_user_agent()
    assert "first" == first_user_agent
    assert "second" == second_user_agent
    assert "third" == third_user_agent


def test_new_user_agent_with_regeneration_level_exceeded():
    adapter = DummyUserAgentAdapter(
        ["first", "second", "second", "second", "third"], regeneration_limit=2
    )
    adapter.new_user_agent()
    adapter.new_user_agent()
    with raises(ValueError) as exc_info:
        adapter.new_user_agent()
    exception_raised = exc_info.value
    assert str(exception_raised) == "User agent regeneration limit exceeded"
