# dl/tests/test_q3_forward_pass.py
import unittest
import torch
from torch import nn
from dl.problems.q3_forward_pass import forward_pass

class DummyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1)

    def forward(self, x):
        return self.linear(x)

class TestForwardPass(unittest.TestCase):
    def test_forward(self):
        model = DummyModel()
        x = torch.randn(5, 3)
        out = forward_pass(model, x)
        self.assertEqual(out.shape, (5, 1))

if __name__ == '__main__':
    unittest.main()
