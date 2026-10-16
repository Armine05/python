import numpy as np
heights=np.array([150,160,170,180,190])
weights=np.array([50,60,65,80,90])
print("heights:", heights)
print("Weights:",weights)
heights_in_meters=heights/100
print("Heights in meters:", heights_in_meters)
scaled_weights=weights*2
print("Scaled Weights(multiplued by 2):" , scaled_weights )
combined=heights*weights
print("Combined:",combined)
