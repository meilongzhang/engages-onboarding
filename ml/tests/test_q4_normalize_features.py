# ml/tests/test_q4_normalize_features.py
import unittest
import numpy as np
from ml.problems.q4_normalize_features import normalize_features

class TestNormalize(unittest.TestCase):
    def test_normalization(self):
        X = np.array([[1, 2], [3, 4]])
        X_norm = normalize_features(X)
        np.testing.assert_almost_equal(X_norm.mean(axis=0), [0.0, 0.0], decimal=6)
        np.testing.assert_almost_equal(X_norm.std(axis=0), [1.0, 1.0], decimal=6)

if __name__ == '__main__':
    unittest.main()
