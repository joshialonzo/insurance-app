from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def get_customers(self):
        pass

    @abstractmethod
    def add_agent(self, agent):
        pass

    @abstractmethod
    def get_agents(self):
        pass

    @abstractmethod
    def add_policy(self, policy):
        pass

    @abstractmethod
    def get_policies(self):
        pass

    @abstractmethod
    def add_validity(self, validity):
        pass

    @abstractmethod
    def get_validities(self):
        pass

    @abstractmethod
    def add_payment(self, payment):
        pass

    @abstractmethod
    def get_payments():
        pass
