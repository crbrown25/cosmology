#!/usr/bin/env python3
"""
Compute the H eigen-value from the 2.725 K CMB monopole
using the scheme-B lapse  g_tt = 1 – Hr/c.
"""

import math, scipy.constants as sc

# Physical constants (CODATA-19)
kB, ħ = sc.Boltzmann, sc.hbar
c, G  = sc.speed_of_light, sc.gravitational_constant
ℓP    = math.sqrt(ħ * G / c**3)          # Planck length (m)

# Observed CMB monopole
T0 = 2.72548                              # kelvin

# Eq. (14) in the paper
pref  = 4 * math.pi * kB * T0 / ħ
H_si  = pref**2 * (ℓP / c)                # s⁻¹

# Convert to km s⁻¹ Mpc⁻¹
km_per_Mpc = sc.parsec * 1e6 / 1e3
print(f"H = {H_si:.4e} 1/s  = {H_si*km_per_Mpc:.2f} km/s/Mpc")

