# dl/tests/test_q2_simple_nn.py
import unittest
import torch
from dl.problems.q2_simple_nn import create_simple_nn

class TestSimpleNN(unittest.TestCase):
    def test_structure(self):
        model = create_simple_nn(10, 5, 1)
        x = torch.randn(2, 10)
        out = model(x)
        self.assertEqual(out.shape, (2, 1))

if __name__ == '__main__':
    unittest.main()
