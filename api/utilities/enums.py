from enum import Enum


class Action(Enum):
    EDIT = 'Edit'
    ADD = 'Add'
    DELETE = 'Delete'

    @classmethod
    def get_all(cls):
        """
        Gets all actions status
        Args:
            cls (Action): An instance of the Action object
        Returns:
            set: Collection of actions
        """
        return set(action.value for action in Action)
