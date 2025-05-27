# ml/tests/test_q5_accuracy_score.py
import unittest
import numpy as np
from ml.problems.q5_accuracy_score import accuracy_score

class TestAccuracy(unittest.TestCase):
    def test_accuracy(self):
        y_true = np.array([0, 1, 2, 2, 1])
        y_pred = np.array([0, 2, 2, 2, 1])
        self.assertAlmostEqual(accuracy_score(y_true, y_pred), 0.8)

if __name__ == '__main__':
    unittest.main()
