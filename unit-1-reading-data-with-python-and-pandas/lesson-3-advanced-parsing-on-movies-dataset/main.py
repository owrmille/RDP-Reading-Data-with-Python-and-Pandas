import numpy as np
import pandas as pd

from tests.test_budget import test_budget
from tests.test_country import test_country
from tests.test_shape import test_shape


column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

movies = pd.read_csv('files/movies.csv', 
                    delimiter='|',
                    header=None,
                    names=column_names, 
                    na_values='?',
                    thousands=',',
                    index_col='movie_title')

test_shape(movies)
test_budget(movies)
test_country(movies)