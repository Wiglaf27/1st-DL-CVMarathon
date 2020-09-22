from pandas import DataFrame
import numpy as np
import pandas as pd
import random

country = ['A', 'B', 'C']
population = []

for i in range(3):
        population.append(random.randint(1000, 100000000))

list_labels = ['country', 'population']
list_columns = [country, population]

zipped = list(zip(list_labels, list_columns))

mostpopulation = pd.DataFrame(dict(zipped))

print(mostpopulation)

