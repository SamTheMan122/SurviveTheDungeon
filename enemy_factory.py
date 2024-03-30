import abc

class EnemyFactory(abc.ABC):
    """
    Abstract class for enemy factories.
    """
    @abc.abstractmethod
    def create_random_enemy(self) -> object:
      pass