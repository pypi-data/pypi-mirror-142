from typing import Any, Optional

import numpy as np
from joblib import Parallel, delayed

from budgetcb.base import MAB
from budgetcb.helper import _get_ALP_predict, _LinUCBnTSSingle, _sherman_morrison_update


class LinUCB(MAB):
    """
    Constrained LinUCB
    References:
        Li, Lihong, et al. "A contextual-bandit approach to personalized news article recommendation."
        Proceedings of the 19th international conference on World wide web. 2010.
    """

    def __init__(
        self, ndims: int, alpha: float, narms: int, T: int, B: int, dummy_arm: int
    ):
        """
        Args:
            ndims: (int): number of context dimension
            alpha: (float): hyper-parameter in LinUCB,
                            scaling the UCB associated with the models reward estimate
                            within each arm based on the data matrices.
            narms (int): number of arms
            T (int): total global time budget
            B (int): total resource budget
            dummy_arm (int): the arm that does not consume any resource
        """

        super().__init__(narms, T, B, dummy_arm)
        self.ndims = ndims
        self.alpha = alpha
        self.b_tau = self.B
        self.tau = self.T

        self.AaI = {}  # a dict to store the inverse of A for each arm
        self.ba = {}  # a dict to store the `ndims` dimensional vector for each arm

        for arm in range(self.narms):
            self.AaI[arm] = np.eye(self.ndims)
            self.ba[arm] = np.zeros((self.ndims, 1))

    def play(self, tround: int, context: np.ndarray) -> int:
        """
        Args:
            tround (int): the index of rounds, starting from 0
            context (np.ndarray): contexts array in the round
        Returns: the chosen action
        """

        tau = self.T - tround
        avg_remaining_budget = float(self.b_tau) / tau

        if self.b_tau > 0:

            p = np.zeros(self.narms)

            for arm in range(self.narms):
                theta = np.dot(self.AaI[arm], self.ba[arm])
                standard_deviation = np.sqrt(
                    np.dot(np.dot(context.T, self.AaI[arm]), context)
                )
                p[arm] = np.dot(theta.T, context) + self.alpha * standard_deviation

            # select the best arm
            best_arm = np.random.choice(np.where(p == max(p))[0])  # tie-breaking

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
            return self.dummy_arm  # resource is exhausted

    def update(
        self,
        arm: int,
        reward: float,
        context: Optional[np.ndarray] = None,
        tround: Optional[int] = None,
    ) -> Any:

        if context is None:
            raise ValueError("Must supply with context in LinUCB class")

        self.AaI[arm] = _sherman_morrison_update(self.AaI[arm], context)
        self.ba[arm] += reward * context
        return self


class UcbAlp(MAB):
    """
    Constrained UCB-ALP
    References:
        Wu, Huasen, et al. "Algorithms with logarithmic or sublinear regret for constrained contextual bandits."
        Advances in Neural Information Processing Systems. 2015.
    """

    def __init__(
        self, narms: int, T: int, B: int, pai: np.ndarray, gmm: Any, dummy_arm: int
    ):
        """
        Args:
            narms (int): number of arms
            T (int): total global time budget
            B (int): total resource budget
            pai (numpy.ndarray): user class distribution
            gmm (any object): any fitted clustering object but recommend using the Gaussian Mixture Model
            dummy_arm (int): the arm that does not consume any resource
        """
        super().__init__(narms, T, B, dummy_arm)
        self.pai = pai
        self.gmm = gmm
        self.J = len(self.pai)  # number of user clusters
        self.b_tau = self.B
        self.tau = self.T

        # init
        self.C = np.zeros((self.J, self.narms))
        self.mu_bar = np.zeros((self.J, self.narms))
        self.mu_hat = np.ones((self.J, self.narms))
        self.mu_star = np.ones(self.J)

    def play(self, tround: int, context: np.ndarray) -> int:
        """
        Args:
            tround (int): the index of rounds, starting from 0
            context (np.ndarray): contexts array in the round
        Returns: the chosen action
        """

        tau = self.T - tround  # update time budget
        avg_remaining_budget = float(self.b_tau) / tau
        # compute the user class
        j = self.gmm.predict(context.T)[0]
        score_max = np.max(self.mu_hat[j, :])
        best_arm = np.random.choice(
            [i for i, v in enumerate(self.mu_hat[j, :]) if v == score_max]
        )  # tie-breaking
        self.mu_star[j] = score_max

        if self.b_tau > 0:

            alp = _get_ALP_predict(
                self.mu_star, np.array(self.pai), avg_remaining_budget
            )  # choose the best arm with proba
            probs_of_action = alp.x  # type: ignore
            rand = np.random.uniform()
            decision = ["action" if rand < p else "skip" for p in probs_of_action]

            if decision[j] == "skip":
                return self.dummy_arm

            else:
                if best_arm != self.dummy_arm:
                    self.b_tau -= 1
                return best_arm

        else:
            return self.dummy_arm  # resource is exhausted

    def update(
        self,
        arm: int,
        reward: float,
        context: Optional[np.ndarray] = None,
        tround: Optional[int] = None,
    ) -> "UcbAlp":
        """
        Single update
        """

        if context is None:
            raise ValueError("Must supply with context in UcbAlp class")

        j = self.gmm.predict(context.T)[0]
        self.C[j, arm] += 1
        self.mu_bar[j, arm] = (self.mu_bar[j, arm] + reward) / self.C[j, arm]
        self.mu_hat[j, arm] = (
            self.mu_bar[j, arm] + np.sqrt(np.log(tround + 1)) / 2 * self.C[j, arm]  # type: ignore
        )
        best_arm = np.argmax(self.mu_hat[j, :])
        self.mu_star[j] = self.mu_hat[j, best_arm]
        return self


class HATCH(MAB):

    """
    References:
        Yang, Mengyue, et al. "Hierarchical Adaptive Contextual Bandits for Resource Constraint based Recommendation."
        Proceedings of The Web Conference 2020. 2020.
    """

    def __init__(
        self,
        narms: int,
        gmm: any,  # type: ignore
        J: int,
        pai: np.ndarray,
        T: int,
        B: int,
        context_dic: dict,
        alpha: float,
        njobs: int = 1,
        dummy_arm: int = 0,
    ):
        """
        Args:
            narms (int): number of arms
            gmm (any object): any fitted clustering object but recommend using the Gaussian Mixture Model
            J (int): number of segments
            pai (numpy.ndarray): user class distribution
            T (int): total global time budget
            B (int): total resource budget
            context_dic (dict): user class center learned by the clustering object
            alpha: (float): hyper-parameter in LinUCB,
                            scaling the UCB associated with the models reward estimate
                            within each arm based on the data matrices.
            njobs (int): parallel computing parameter, default to 1
            dummy_arm (int): the arm that does not consume any resource
        """

        super().__init__(narms, T, B, dummy_arm)

        self.pai = np.array(pai)
        self.context_dic = context_dic
        self.gmm = gmm
        self.context_dim = len(context_dic.get(dummy_arm))  # type: ignore
        self._add_common_lin(alpha, narms, njobs, J, self.context_dim)  # type: ignore
        self.ustar = [0 for i in range(J)]

        self.b_tau = self.B
        self.tau = self.T
        self.alpha = alpha

    def _add_common_lin(
        self, alpha: float, narms: int, njobs: int, J: int, context_dim: dict
    ) -> None:

        if isinstance(alpha, int):
            alpha = float(alpha)
        assert isinstance(alpha, float)

        self.njobs = njobs
        self.alpha = alpha
        self.narms = narms
        self.J = J
        self._oraclesa = [
            [_LinUCBnTSSingle(1.0, context_dim) for n in range(narms)] for i in range(J)  # type: ignore
        ]
        self._oraclesj = [_LinUCBnTSSingle(1.0, context_dim) for n in range(J)]  # type: ignore
        self.uj = np.array([float(1) for i in range(self.J)])

    def play(self, tround: int, context: np.ndarray) -> int:

        tau = self.T - tround
        avg_remaining_budget = float(self.b_tau) / tau

        pred = np.zeros(self.narms)
        j = self.gmm.predict(context.T)

        for choice in range(self.narms):
            pred[choice] = self._oraclesa[j[0]][choice].predict(context.T)

        best_arm = np.argmax(np.array([pred]), axis=1)[0]

        if self.b_tau > 0:
            acc_percentage = _get_ALP_predict(
                self.uj, np.array(self.pai), avg_remaining_budget
            )

            if np.random.uniform(0, 1) > acc_percentage["x"][j]:  # skip
                return self.dummy_arm

            else:  # retain
                if best_arm != self.dummy_arm:
                    self.b_tau -= 1
                return best_arm
        else:
            return self.dummy_arm

    def update(
        self,
        arm: int,
        reward: float,
        context: Optional[np.ndarray] = None,
        tround: Optional[int] = None,
    ) -> "HATCH":  # type: ignore

        self.ndim = context.shape[1]  # type: ignore
        Xj = np.array(
            list(map(lambda x: self.context_dic[x], list(self.gmm.predict(context))))
        )

        Parallel(n_jobs=self.njobs, verbose=0, require="sharedmem")(
            delayed(self._update_single)(j, context, Xj, arm, reward)
            for j in range(self.J)
        )

        for j in range(self.J):
            self.uj[j] = self._oraclesj[j].predict(np.array([self.context_dic[j]]))

    def _update_single(
        self,
        j: int,
        context: np.ndarray,
        Xj: np.ndarray,
        arm: np.ndarray,
        reward: np.ndarray,
    ) -> None:

        xj = self.gmm.predict(context)
        this_context = xj == j
        self._oraclesj[j].fit(
            Xj[this_context, :], reward[this_context].astype("float64")
        )
        for choice in range(self.narms):
            this_action = arm == choice
            self._oraclesa[j][choice].fit(
                context[this_action, :], reward[this_action].astype("float64")
            )
