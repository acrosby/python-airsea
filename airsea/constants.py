"""
Physical constants
==================
"""

# 9.7803 in COARE FIXME: change to sw.grav
g = 9.8  # Acceleration due to gravity [m s :sup:`-2`].

# Stefan-Boltzmann constant [W m :sup:`-2` K :sup:`-4`].
sigmaSB = 5.6697e-8

# Molecular weight ratio [water air :sup:`-1`].
eps_air = 0.62197

# Conversion factor for [:math:`^\\circ` C] to [:math:`^\\circ` K].
CtoK = 273.16  # 273.15

# Gas constant for dry air [J kg :sup:`-1` K :sup:`-1`].
gas_const_R = 287.04  # NOTE: 287.1 in COARE.


"""
Meteorological constants
========================
"""


# von Karman's constant.
kappa = 0.4  # NOTE: 0.41

# Charnock constant. For determining roughness length at sea given friction
# velocity, used in Smith formulas for drag coefficient and also in Fairall
# and Edson.  Ese alpha = 0.011 for open-ocean and alpha = 0.018 for
#  fetch-limited (coastal) regions.
charn = Charnock_alpha = 0.011  # NOTE: 0.018

# Limiting roughness Reynolds for aerodynamically smooth flow.
R_roughness = 0.11


"""
Defaults for boundary-layer studies
===================================
"""


# Heat capacity of air [J kg :sup:`-1` K :sup:`-1`].
cp = 1004.7

# Saturation specific humidity coefficient reduced by 2% over salt water.
Qsat_coeff = 0.98


"""
Short-wave flux calculations
============================
"""

Solar_const = 1368.0
""" The solar constant [W/m^2] represents a mean of satellite measurements
made over the last sunspot cycle (1979-1995) taken from Coffey et al (1995),
Earth System Monitor, 6, 6-10."""


"""
Long-wave flux calculations
===========================
"""

# Long-wave emissivity of ocean from Dickey et al (1994), J. Atmos. Oceanic
# Tech., 11, 1057-1076
emiss_lw = 0.985

# Default values.
P_default = 1020.
