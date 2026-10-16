import numpy as np
houses=np.array([
    [3,2000,10],
    [2,1500,20],
    [4,2500,5]
    ])
weight=np.array([50,100,-20])
bias=3000
predicted_prices=np.dot(houses,weight)+bias
print(predicted_prices)
