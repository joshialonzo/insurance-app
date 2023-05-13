from insurance.models import Agent
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import create_agent

from tests.integration.memory.utils import get_first_line


def test_create_agent_with_line():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve first line from file
    first_line = get_first_line()

    # create agent with line
    agent_number, agent_name, *_ = first_line
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
    )

    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number
    assert len(storage.get_agents()) == 1
