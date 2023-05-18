"""
Storage interface is an abstract class that defines the methods that must be implemented by a storage class.
Storage child classes must implement the following methods:

    - add_customer
    - get_customers
    - add_agent
    - get_agents
    - add_policy
    - get_policies
    - add_validity
    - get_validities
    - add_payment
    - get_payments

The Storage class and the Storage implementations must be declared.
Both are an application of the Bridge design pattern.
Both classes are in the Repository layer.
"""


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
