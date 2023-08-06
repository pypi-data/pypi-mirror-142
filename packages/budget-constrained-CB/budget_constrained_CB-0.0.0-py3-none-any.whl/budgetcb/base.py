from abc import ABC, abstractmethod
from typing import Optional

import numpy as np


class MAB(ABC):
    """
    Base class to implement the online Constrained Multi-Armed Bandits algorithms
    """

    def __init__(self, narms: int, T: int, B: int, dummy_arm: int):
        """
        Args:
            narms (int): number of arms
            T (int): total global time budget
            B (int): total resource budget
            dummy_arm (int): the arm that does not consume any resource
        """

        self.narms = narms
        self.T = T
        self.B = B
        self.dummy_arm = dummy_arm

    @abstractmethod
    def play(self, tround: int, context: Optional[np.ndarray]) -> int:
        """
        Analogy to "predict" function in supervised learning setting
        Args:
            tround (int): round t
            context (np.ndarray or None): observed contexts features observed at this round, default to None
        Returns:
            the best arm at each round
        """

        pass

    @abstractmethod
    def update(
        self,
        arm: int,
        reward: float,
        context: Optional[np.ndarray] = None,
        tround: Optional[int] = None,
    ) -> "MAB":
        """
        Analogy to "fit" function in supervised learning setting
        Args:
            arm (int): observed action at this round
            reward (float): observed reward at this round
            context (np.ndarray or None): observed contexts features observed at this round, default to None
            tround (int or None): round t, default to None
        Returns:
            self
        """

        pass
