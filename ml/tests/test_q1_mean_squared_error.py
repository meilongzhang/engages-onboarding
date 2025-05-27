# ml/tests/test_q1_mean_squared_error.py
import unittest
import numpy as np
from ml.problems.q1_mean_squared_error import mean_squared_error

class TestMSE(unittest.TestCase):
    def test_basic(self):
        y_true = np.array([1, 2, 3])
        y_pred = np.array([1, 2, 4])
        self.assertAlmostEqual(mean_squared_error(y_true, y_pred), 0.333, places=3)

    def test_zero(self):
        y_true = np.array([0, 0])
        y_pred = np.array([0, 0])
        self.assertEqual(mean_squared_error(y_true, y_pred), 0.0)

if __name__ == '__main__':
    unittest.main()
