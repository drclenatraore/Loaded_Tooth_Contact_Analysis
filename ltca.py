import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

working_center_distance = 0.5
teeth_number_pinion = 10
teeth_number_gear = 44
module = 0.8
pressure_angle = 20
normal_profile_shift_coefficient_pinion = 0.1
normal_profile_shift_coefficient_gear = -0.1 
working_pressure_angle = 
actual_profile_shift_coefficient_pinion = normal_profile_shift_coefficient_pinion / np.cos(working_pressure_angle)
actual_profile_shift_coefficient_gear = normal_profile_shift_coefficient_gear / np.cos(working_pressure_angle)
face_width = 15
addendum_coefficient = 1
dedendum_coefficient = 1.25
root_radius_factor = 0.38
youngs_modulus = 210e9
poissons_ratio = 0.3
input_torque = 100

def bending_stress(teeth_number_pinion, teeth_number_gear, pressure_angle):
    # Implementation for bending stress calculation
    pass

def contact_ratio(teeth_number_pinion, teeth_number_gear, pressure_angle):
    pitch_diameter_pinion = module * teeth_number_pinion
    pitch_diameter_gear = module * teeth_number_gear
    base_radius_pinion = pitch_diameter_pinion / 2 * np.cos(working_pressure_angle)
    base_radius_gear = pitch_diameter_gear / 2 * np.cos(working_pressure_angle)
    
    addendum_pinion = addendum_coefficient * module
    dedendum_pinion = dedendum_coefficient * module
    addendum_gear = addendum_coefficient * module
    dedendum_gear = dedendum_coefficient * module
    
    path_length = (addendum_pinion + dedendum_gear) / np.sin(working_pressure_angle)
    
    return path_length / (np.pi * module)


def involute_profile(base_radius, start_angle, end_angle, num_points=100):
    angles = np.linspace(start_angle, end_angle, num_points)
    x = base_radius * (np.cos(angles) + angles * np.sin(angles))
    y = base_radius * (np.sin(angles) - angles * np.cos(angles))
    return x, y

def tooth_thickenness_half_angle(teeth_number):
    
    return np.pi / (2 * teeth_number)
