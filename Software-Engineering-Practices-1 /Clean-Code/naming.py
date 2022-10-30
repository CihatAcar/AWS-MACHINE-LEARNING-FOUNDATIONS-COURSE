# Bad naming examples

s = [88, 92, 79, 93, 85]  # Student test scores
print(sum(s) / len(s))  # print mean of test scores

s1 = [x ** 0.5 * 10 for x in s]  # curve scores with square root method and store in new list
print(sum(s1) / len(s1))  # print mean of curved test scores

# Better code
import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_scores))


#  bad naming
def count_unique_values_of_names_list_with_set(names_list):
    return len(set(names_list))


# better
def count_unique_values(arr):
    return len(set(arr))
