# dl/problems/q4_binary_cross_entropy.py
import torch

def binary_cross_entropy(y_pred, y_true):
    """
    Compute binary cross-entropy loss.

    Formula:
        BCE = -[y*log(p) + (1-y)*log(1-p)]

    Args:
        y_pred: torch.Tensor of predicted probs (values in (0,1)), shape (n,)
        y_true: torch.Tensor of true labels (0 or 1), shape (n,)

    Returns:
        torch scalar (mean BCE)
    """
    pass
