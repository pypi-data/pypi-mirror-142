from typing import Optional

import numpy as np

from budgetcb.base import MAB


class EpsGreedy(MAB):
    """
    Constrained Context-Free Epsilon Greedy MAB
    References:
        - Follow the same update rule as described in [1]
        - Follow the similar resource constraint strategy in the HATCH paper [2],
            i.e. the best choice is executed with the probability that is associated with the remaining budget.
        - It is a context-free approach therefore no contexts will be passed
    [1] Sutton & Barto Book: Reinforcement Learning: An Introduction Chapter 2 page 32
    [2] https://arxiv.org/pdf/2004.01136.pdf
    """

    def __init__(self, epsilon: float, narms: int, T: int, B: int, dummy_arm: int):
        """
        Args:
            epsilon (float): probability of exploration
            narms (int): number of arms
            T (int): total global time budget
            B (int): total resource budget
            dummy_arm (int): the arm that does not consume any resource
        """
        super().__init__(narms, T, B, dummy_arm)
        self.epsilon = epsilon
        self.b_tau = self.B  # changing resource budget
        self.Na = np.zeros(self.narms, np.int)  # type: ignore
        self.Qa = np.zeros(self.narms)

    def play(self, tround: int, context: Optional[np.ndarray] = None) -> int:
        """
        Args:
            tround (int): the index of rounds, starting from 0
            context (np.ndarray): contexts array in the round
        Returns: the chosen action
        """

        tau = self.T - tround
        avg_remaining_budget = float(self.b_tau) / tau

        if self.b_tau > 0:

            if np.random.uniform() > self.epsilon:
                best_arm = np.random.choice(np.where(self.Qa == self.Qa.max())[0])

                # take the best arm with the probability due to the resource constraint
                rand = np.random.uniform()

                if rand < avg_remaining_budget:
                    # take action
                    if best_arm != self.dummy_arm:
                        self.b_tau -= 1
                    return best_arm

                else:
                    # skip
                    return self.dummy_arm

            else:
                random_arm = np.random.randint(self.narms)

                if random_arm != self.dummy_arm:
                    self.b_tau -= 1
                return random_arm
        else:
            return self.dummy_arm  # resource is exhausted

    def update(
        self,
        arm: int,
        reward: float,
        context: Optional[np.ndarray] = None,
        tround: Optional[int] = None,
    ) -> "EpsGreedy":

        self.Na[arm] += 1
        step_size = 1 / float(self.Na[arm])
        self.Qa[arm] += step_size * (reward - self.Qa[arm])
        return self
