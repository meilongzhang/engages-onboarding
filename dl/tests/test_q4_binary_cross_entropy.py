# dl/tests/test_q4_binary_cross_entropy.py
import unittest
import torch
from dl.problems.q4_binary_cross_entropy import binary_cross_entropy

class TestBCELoss(unittest.TestCase):
    def test_bce(self):
        y_pred = torch.tensor([0.9, 0.1])
        y_true = torch.tensor([1.0, 0.0])
        loss = binary_cross_entropy(y_pred, y_true)
        self.assertAlmostEqual(loss.item(), 0.105, places=2)

if __name__ == '__main__':
    unittest.main()
