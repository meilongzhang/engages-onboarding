# dl/tests/test_q5_train_step.py
import unittest
import torch
from torch import nn
from dl.problems.q5_train_step import train_step

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

class TestTrainStep(unittest.TestCase):
    def test_train(self):
        model = SimpleNN()
        x = torch.randn(10, 3)
        y = torch.randint(0, 2, (10, 1)).float()
        loss_fn = nn.BCELoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

        loss = train_step(model, x, y, loss_fn, optimizer)
        self.assertIsInstance(loss, float)
        self.assertGreaterEqual(loss, 0.0)

if __name__ == '__main__':
    unittest.main()
