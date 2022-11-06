def test_country(movies):
    assert '?' not in movies.country.unique()