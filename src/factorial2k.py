import pyDOE2 as pd
import numpy as np
from itertools import combinations
import string


def effects_table_method(factors, results):

    # This combination string is used to create the factorial_string,
    # because pyDOE2 input is the comlumns that we want to create in
    # the signal table. Here we are using it to generate the 2k^N table,
    # so we need the combination of N comlumns.
    combination_string = ""
    for _, letter in zip(range(0, factors), string.ascii_lowercase):
        combination_string += letter

    _combinations = [
        "".join(l)
        for i in range(len(combination_string))
        for l in combinations(combination_string, i + 1)
    ]

    factors_string = " ".join(_combinations)
    factorial_columns = pd.fracfact(factors_string)

    # Two to the power of factors
    tpf = 2 ** factors

    image_column = np.ones((tpf, 1))
    results_column = np.array(results)

    sign_table = np.hstack((image_column, factorial_columns))

    total = [
        float(np.dot(sign_table[:, i], results_column) / tpf) for i in range(tpf)
    ]

    print(total)
    return total


def variation_allocation(effects):
    # The first elements represents q0, and is not important here
    effects.pop(0)

    allocation = [4 * effect * effect for effect in effects]
    total_variation = sum(allocation)

    percentages = [(100 * a) / total_variation for a in allocation]

    return percentages
