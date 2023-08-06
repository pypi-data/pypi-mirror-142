from typing import Any, Dict, Optional

import numpy as np


class ReplayEvaluator(object):
    """
    The Replay off-policy evaluation method developed by Li et al. [WSDM 2011]
    to obtain an unbiased evaluation of a bandit algorithm when the arms are presented randomly
    """

    def __init__(
        self,
        policy: Any,
        arms: np.ndarray,
        rewards: np.ndarray,
        contexts: Optional[np.ndarray] = None,
        batch_size: int = 1,
    ):
        """
        Args:
            policy (object): the CB policy
            arms (np.ndarray): observed arms with shape (n_events, )
            rewards (np.ndarray): observed rewards with shape (n_events, )
            contexts (np.ndarray): observed contexts with shape (n_events, context_dim)
            batch_size: batch size for updates, default to 1
        """

        self.policy = policy
        self.arms = arms
        self.rewards = rewards
        self.contexts = contexts
        self.batch_size = batch_size

    def evaluate(self) -> Dict:

        event_index = 0
        self.match_num = 0
        self.match_arms = []
        self.payoff_records = []
        out_dict = {}
        ix_chosen = list()

        for i in range(self.arms.shape[0]):
            arm = np.int(self.arms[i])  # type: ignore
            xt = (
                self.contexts[i, :].reshape(-1, 1)
                if self.contexts is not None
                else None
            )
            would_choose = self.policy.play(tround=self.match_num, context=xt)

            if would_choose == arm:
                ix_chosen.append(i)
                self.match_arms.append(arm)
                self.payoff_records.append(self.rewards[event_index])

                if self.batch_size == 1:
                    self.policy.update(
                        arm=arm,
                        reward=self.rewards[event_index],
                        context=xt,
                        tround=self.match_num,
                    )
                else:
                    # batch update
                    if (self.match_num % self.batch_size) == 0:
                        ix_fit = np.array(ix_chosen)
                        self.policy.update(
                            arm=self.arms[ix_fit],
                            reward=self.rewards[ix_fit],
                            context=self.contexts[ix_fit, :],  # type: ignore
                            tround=self.match_num,
                        )

                self.match_num += 1

            event_index += 1

        out_dict["avg_payoff"] = np.sum(self.payoff_records) / len(self.payoff_records)
        return out_dict

    def get_details(self) -> Dict:
        details: Dict[str, Any] = {}
        details["match_num"] = self.match_num
        details["payoff_records"] = self.payoff_records
        details["match_arms"] = self.match_arms
        return details
