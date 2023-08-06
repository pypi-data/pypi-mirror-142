import numpy as np
from scipy import optimize


def _sherman_morrison_update(Ainv: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Using Sherman morrison formula to compute the inverse of the rank one update to A, A + x * x^T.
    """
    return Ainv - np.linalg.multi_dot([Ainv, x, x.T, Ainv]) / (
        1.0 + np.linalg.multi_dot([x.T, Ainv, x])
    )


def _get_ALP_predict(
    mu_star: np.ndarray, pai: np.ndarray, avg_remaining_budget: float
) -> np.ndarray:

    c = np.multiply(mu_star, pai.T)
    A = np.array([pai])
    b = np.array([avg_remaining_budget])
    bound = [(0, 1) for i in range(len(pai))]
    assert b.shape[0] == 1
    res = optimize.linprog(-c, A, b, bounds=bound)
    return res


class _LinUCBnTSSingle:
    def __init__(self, alpha: float, context_dim: int):
        self.alpha = alpha
        if "Ainv" not in dir(self):
            self.Ainv = np.eye(context_dim)
            self.b = np.zeros((context_dim, 1))

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        if len(X.shape) == 1:
            X = X.reshape((1, -1))
        self.Ainv = np.eye(X.shape[1])
        self.b = np.zeros((X.shape[1], 1))

        self.partial_fit(X, y)

    def partial_fit(self, X: np.ndarray, y: np.ndarray) -> None:
        if len(X.shape) == 1:
            X = X.reshape((1, -1))
        if "Ainv" not in dir(self):
            self.Ainv = np.eye(X.shape[1])
            self.b = np.zeros((X.shape[1], 1))
        sumb = np.zeros((X.shape[1], 1))
        for i in range(X.shape[0]):
            x = X[i, :].reshape((-1, 1))
            r = y[i]
            sumb += r * x
            self.Ainv = _sherman_morrison_update(self.Ainv, x)

        self.b += sumb

    def predict(self, X: np.ndarray) -> None:
        if len(X.shape) == 1:
            X = X.reshape((1, -1))

        pred = self.Ainv.dot(self.b).T.dot(X.T).reshape(-1)

        for i in range(X.shape[0]):
            x = X[i, :].reshape((-1, 1))
            cb = self.alpha * np.sqrt(np.linalg.multi_dot([x.T, self.Ainv, x]))
            pred[i] += cb[0]

        return pred
