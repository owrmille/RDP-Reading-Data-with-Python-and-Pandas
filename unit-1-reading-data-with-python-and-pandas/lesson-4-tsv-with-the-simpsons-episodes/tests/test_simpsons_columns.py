def test_simpsons_columns(simpsons):
    assert list(simpsons.columns) == ['Title', 'Air date', 'IMDB rating']
