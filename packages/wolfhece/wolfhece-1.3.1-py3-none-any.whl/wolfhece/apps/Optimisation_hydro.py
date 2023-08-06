import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import block
from numpy.testing._private.utils import measure

from .hydrology.Optimisation import Optimisation
from .hydrology.PostProcessHydrology import PostProcessHydrology
from .hydrology.Catchment import *
from .PyParams import*


app = wx.App()

myOpti = Optimisation()

# %% Show  graphs
myOpti.Show()
app.MainLoop()
print("That's all folks! ")