from pytest import approx
from src.factorial2k import effects_table_method, variation_allocation

FACTORS = 2
RESULTS = [[15], [45], [25], [75]]


def test_effects():
    effects = effects_table_method(FACTORS, RESULTS)
    assert effects == [40.0, 20.0, 10.0, 5.0]


def test_variation():
    effects = effects_table_method(FACTORS, RESULTS)
    allocation = variation_allocation(effects)
    assert allocation == approx([76, 19, 5], rel=1e-1, abs=1e-1)
