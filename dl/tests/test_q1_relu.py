# dl/tests/test_q1_relu.py
import unittest
import torch
from dl.problems.q1_relu import relu

class TestReLU(unittest.TestCase):
    def test_relu(self):
        x = torch.tensor([-1.0, 0.0, 2.0])
        out = relu(x)
        expected = torch.tensor([0.0, 0.0, 2.0])
        self.assertTrue(torch.equal(out, expected))

if __name__ == '__main__':
    unittest.main()
