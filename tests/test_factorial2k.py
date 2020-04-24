from src.factorial2k import effects_table_method

def test_effects():
    FACTORS = 2
    RESULTS = [[15], [45], [25], [75]]
    assert effects_table_method(FACTORS, RESULTS) == [40.0, 20.0, 10.0, 5.0]


