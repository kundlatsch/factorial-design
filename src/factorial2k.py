import pyDOE2 as pd
import numpy as np


def effects_table_method(factors, results):
    image_column = np.ones((2 ** factors, 1))
    factorial_columns = pd.fracfact("a b ab")
    results_column = np.array(results)

    sign_table = np.hstack((image_column, factorial_columns))

    total = [
        float(np.dot(sign_table[:, i], results_column) / 4) for i in range(2 ** factors)
    ]
    return total


def variation_allocation(effects):
    # The first elements represents q0, and is not important here
    effects.pop(0)

    allocation = [4 * effect * effect for effect in effects]
    total_variation = sum(allocation)

    percentages = [(100 * a) / total_variation for a in allocation]

    return percentages
