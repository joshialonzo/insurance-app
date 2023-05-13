from insurance.models import Agent
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import create_agent


def test_create_agent_with_number():
    # initialize the storage
    storage = MemoryStorage()

    # create an agent with a number
    agent_number = 123456789
    agent_name = "John Doe"
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
    )

    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number
    assert len(storage.get_agents()) == 1


def test_create_agent_with_idempotency():
    # initialize the storage
    storage = MemoryStorage()

    # create an agent with a number
    agent_number = 123456789
    agent_name = "John Doe"
    storage, _ = create_agent(
        storage,
        agent_name,
        agent_number,
    )
    storage, agent = create_agent(
        storage,
        agent_name,
        agent_number,
    )

    assert isinstance(agent, Agent)
    assert agent.name == agent_name
    assert agent.number == agent_number
    assert len(storage.get_agents()) == 1
