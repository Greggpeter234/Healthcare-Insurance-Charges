import pandas as pd
import numpy as np


np.random.seed(101)
df = pd.DataFrame(data=np.random.randn(5,4),
                  index=['A', 'B', 'C', 'D', 'E'],  
                  columns=['Col1', 'Col2', 'Col3', 'Col4']
                  )

df [['Col2']] # write your code here
