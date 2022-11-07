import numpy as np
import pandas as pd
from tests.test_simpsons_columns import test_simpsons_columns
from tests.test_simpsons_item import test_simpsons_item
from tests.test_simpsons_shape import test_simpsons_shape

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']
             
simpsons = pd.read_csv('files/simpsons-episodes.tsv', 
                        delimiter='\t',
                        names=col_names,
                        usecols=['Title', 'Air date', 'Production code', 'IMDB rating'],
                        na_values='no_val',
                        skiprows=4,
                        index_col='Production code',
                        parse_dates=['Air date'])      

test_simpsons_shape(simpsons)
test_simpsons_columns(simpsons)
test_simpsons_item(simpsons)                   