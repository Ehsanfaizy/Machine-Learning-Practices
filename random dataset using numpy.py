# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:18:32 2022

@author: BOSS
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(1, 10, 525)
plt.hist(x, 5)
plt.show()