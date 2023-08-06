import matplotlib.pyplot as plt
import numpy as np
from thermo import *
from fluids.numerics import logspace

ethanol_psat = VaporPressure(Tb=351.39, Tc=514.0, Pc=6137000.0, omega=0.635, CASRN='64-17-5')
methods = ['WAGNER_MCGARRY', 'DIPPR_PERRY_8E', 'COOLPROP'] if coolprop.has_CoolProp() else ['WAGNER_MCGARRY', 'DIPPR_PERRY_8E']

ethanol_psat.plot_T_dependent_property(Tmin=400, Tmax=500, methods=methods, pts=30)
