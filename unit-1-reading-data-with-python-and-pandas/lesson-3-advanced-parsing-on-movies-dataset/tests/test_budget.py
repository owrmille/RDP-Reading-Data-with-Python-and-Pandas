def test_budget(movies):
    assert movies.loc[:, 'budget'].min() == 105000000.0
