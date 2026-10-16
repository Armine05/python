import numpy as np
arr_2d=np.array([[150,23],
                 [23,45],
                 [243,89],
                 [18,38],
                 [33,64]])
heights=arr_2d[:,0]
tall_people=heights[heights>170]
print(tall_people)
