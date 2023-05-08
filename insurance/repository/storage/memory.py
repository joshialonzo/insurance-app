from insurance.repository.storage import Storage


class MemoryStorage(Storage):
    def __init__(self):
        self.__customers = set()
        self.__agents = set()
        self.__policies = set()
        self.__validities = set()
        self.__payments = set()

    def add_customer(self, customer):
        self.__customers.add(customer)
    
    def get_customers(self):
        return self.__customers

    def add_agent(self, agent):
        self.__agents.add(agent)

    def get_agents(self):
        return self.__agents

    def add_policy(self, policy):
        self.__policies.add(policy)

    def get_policies(self):
        return self.__policies

    def add_validity(self, validity):
        self.__validities.add(validity)
    
    def get_validities(self):
        return self.__validities

    def add_payment(self, payment):
        self.__payments.add(payment)

    def get_payments(self):
        return self.__payments
