import pyDOE2 as pd
import numpy as np

def effects_table_method(FACTORS, RESULTS):
    image_column = np.ones((2 ** FACTORS, 1))
    factorial_columns = pd.fracfact('a b ab')
    results_column = np.array(RESULTS)
    
    sign_table = np.hstack((image_column, factorial_columns))

    total = [float(np.dot(sign_table[:, i], results_column)/4) for i in range(2 ** FACTORS)]
    return total