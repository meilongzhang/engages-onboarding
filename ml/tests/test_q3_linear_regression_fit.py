# ml/tests/test_q3_linear_regression_fit.py
import unittest
import numpy as np
from ml.problems.q3_linear_regression_fit import fit_linear_regression

class TestFitLinear(unittest.TestCase):
    def test_fit(self):
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])
        w = fit_linear_regression(X, y)
        np.testing.assert_array_almost_equal(w, [2.0], decimal=5)

if __name__ == '__main__':
    unittest.main()
