import numpy as np
import pandas as pd


arr3 = np.random.randint(1,20,size=(4,1,2))
print(arr3)
data = pd.DataFrame(arr3)
data.to_csv('data1.csv')