import collisions
import setting
import utils
import math

class entity_manager:
    """
    manejo de entidades
    """
    def __init__(self):
        """
        docstring
        """
        self.entity_types = ['playable', 'non_playable', 'static', 'item']
        
    pass

    def playable(self):
        """
        docstring
        """
        pass
    def non_playable(self):
        """
        docstring
        """
        pass
    def static(self):
        """
        docstring
        """
        pass
    def item(self):
        """
        docstring
        """
        pass


class entity(entity_manager):
    """
    base de entidades
    """
    pass


class player(entity):
    """
    docstring
    """
    pass