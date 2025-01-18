import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the inputs and outputs for the fuzzy system
room_temp = ctrl.Antecedent(np.arange(15, 36, 1), 'room_temp')
desired_temp = ctrl.Antecedent(np.arange(15, 31, 1), 'desired_temp')
ac_power = ctrl.Consequent(np.arange(0, 11, 1), 'ac_power')

# Define fuzzy sets for room temperature
room_temp['cold'] = fuzz.trimf(room_temp.universe, [15, 15, 22])
room_temp['comfortable'] = fuzz.trimf(room_temp.universe, [20, 25, 30])
room_temp['hot'] = fuzz.trimf(room_temp.universe, [28, 35, 35])

# Define fuzzy sets for desired temperature
desired_temp['low'] = fuzz.trimf(desired_temp.universe, [15, 15, 20])
desired_temp['medium'] = fuzz.trimf(desired_temp.universe, [18, 23, 28])
desired_temp['high'] = fuzz.trimf(desired_temp.universe, [25, 30, 30])

# Define fuzzy sets for AC power
ac_power['low'] = fuzz.trimf(ac_power.universe, [0, 0, 5])
ac_power['medium'] = fuzz.trimf(ac_power.universe, [3, 5, 8])
ac_power['high'] = fuzz.trimf(ac_power.universe, [6, 10, 10])

# Define fuzzy rules
rule1 = ctrl.Rule(room_temp['cold'] & desired_temp['low'], ac_power['low'])
rule2 = ctrl.Rule(room_temp['cold'] & desired_temp['medium'], ac_power['medium'])
rule3 = ctrl.Rule(room_temp['cold'] & desired_temp['high'], ac_power['high'])
rule4 = ctrl.Rule(room_temp['comfortable'] & desired_temp['low'], ac_power['low'])
rule5 = ctrl.Rule(room_temp['comfortable'] & desired_temp['medium'], ac_power['medium'])
rule6 = ctrl.Rule(room_temp['comfortable'] & desired_temp['high'], ac_power['high'])
rule7 = ctrl.Rule(room_temp['hot'] & desired_temp['low'], ac_power['medium'])
rule8 = ctrl.Rule(room_temp['hot'] & desired_temp['medium'], ac_power['high'])
rule9 = ctrl.Rule(room_temp['hot'] & desired_temp['high'], ac_power['high'])

# Create and simulate the fuzzy control system
ac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
ac_sim = ctrl.ControlSystemSimulation(ac_ctrl)

# Example inputs
ac_sim.input['room_temp'] = 30  # Current room temperature
ac_sim.input['desired_temp'] = 22  # Desired temperature

# Compute the result
ac_sim.compute()

print(f"AC Power Level: {ac_sim.output['ac_power']}")



# Visualize the result
room_temp.view(sim=ac_sim)
desired_temp.view(sim=ac_sim)
ac_power.view(sim=ac_sim)

# Keep the figures open
plt.show()
