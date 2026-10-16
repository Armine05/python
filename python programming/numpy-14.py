import numpy as np
houses=np.array([
    [3,2000,10],
    [2,1500,20],
    [4,2500,5]
    ])
updated_bedrooms=houses[:,0]+1
print("updated bedrroms afetr boradcasting:\n",updated_bedrooms)
updated_age=houses[:,2]-5
print("updated hpuse ages after broadcasting:\n",updated_age)
adjusted_size=houses[:,1]*1.1
print("updated house sizes after broadcasting:\n",adjusted_size)
