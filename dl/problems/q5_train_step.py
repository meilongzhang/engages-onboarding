# dl/problems/q5_train_step.py
import torch

def train_step(model, x, y, loss_fn, optimizer):
    """
    Perform one training step: forward → loss → backward → step.

    Args:
        model: nn.Module
        x: input tensor
        y: ground truth tensor
        loss_fn: loss function (e.g. nn.BCELoss)
        optimizer: torch optimizer

    Returns:
        float: loss value (not tensor)
    """
    pass
