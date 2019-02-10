from abc import ABC
from abc import abstractmethod


class actor(ABC):
    """
    Abstract class that all elements should implement
    """

    @abstractmethod
    def render(self):
        """
        Renders the actor on the screen
        """
        pass

    @abstractmethod
    def get_position(self):
        """
        Returns a tuple of the (x,y) position of the actor
        """
        pass

    @abstractmethod
    def get_asset(self):
        """
        Returns the string location of the actors asset
        """
