import matplotlib.pyplot as plt
import os
import pandas as pd
from pandas import Series, DataFrame

dir_data = '/home/hungjieng/Downloads/'

f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' %(f_app))
app_train = pd.read_csv(f_app)

label = ['A', 'B', 'C']
A = [1, 4, 7]
B = [2, 5, 8]
C = [3, 6, 9]
col = [A, B, C]
data = pd.DataFrame(dict(zip(label, col)))

print(data['A'])
