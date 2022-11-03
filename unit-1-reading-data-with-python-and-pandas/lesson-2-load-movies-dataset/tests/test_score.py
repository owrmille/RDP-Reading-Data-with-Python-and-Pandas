def test_score(movies):
    assert movies.loc[:, 'imdb_score'].max() == 9
