# ml/tests/test_q2_linear_regression_predict.py
import unittest
import numpy as np
from ml.problems.q2_linear_regression_predict import predict_linear

class TestPredictLinear(unittest.TestCase):
    def test_prediction(self):
        X = np.array([[1, 2], [3, 4]])
        w = np.array([0.5, 1.0])
        b = 1.0
        expected = np.array([1*0.5 + 2*1.0 + 1.0, 3*0.5 + 4*1.0 + 1.0])
        np.testing.assert_array_almost_equal(predict_linear(X, w, b), expected)

if __name__ == '__main__':
    unittest.main()
