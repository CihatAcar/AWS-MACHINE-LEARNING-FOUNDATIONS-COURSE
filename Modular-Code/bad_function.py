# Bad function example
# In this case functions are badly designed that they are doing more than one thing.
import math
import numpy as np


def flat_curve(arr, n):
    curved_arr = [i + n for i in arr]
    print(np.mean(curved_arr))
    return curved_arr


def square_root_curve(arr):
    curved_arr = [math.sqrt(i) * 10 for i in arr]
    print(np.mean(curved_arr))
    return curved_arr


test_scores = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)
