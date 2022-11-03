import numpy as np
import pandas as pd

from tests.test_score import test_score
from tests.test_shape import test_shape

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

movies = pd.read_csv('files/movies.csv', 
                                sep='|', 
                                header=None,
                                names=column_names, 
                                skiprows=3)

test_shape(movies)
test_score(movies)