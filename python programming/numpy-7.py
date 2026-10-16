import numpy as np
arr_2d=np.array([[150,23],
                 [23,45],
                 [243,89],
                 [18,38],
                 [33,64]])
selected_rows=arr_2d[[0,2,4],:]
print(selected_rows)
