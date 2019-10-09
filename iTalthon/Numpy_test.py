"""這裡先簡單示範就好，所以就只是單純用list進行數字存放"""
import numpy as np
score = [38, 29, 53, 17, 8, 49, 11, 9]
np_score = np.array(score)
new_score = (np_score ** 0.5) * 12
print(new_score)
