import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define input variables (Size and Weight)
size = ctrl.Antecedent(np.arange(0, 11, 1), 'Size')
weight = ctrl.Antecedent(np.arange(0, 101, 1), 'Weight')

# Define output variable (Quality)
quality = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'Quality')

# Define membership functions for Size
size['Small'] = fuzz.trimf(size.universe, [0, 0, 5])
size['Large'] = fuzz.trimf(size.universe, [0, 10, 10])

# Define membership functions for Weight
weight['Small'] = fuzz.trimf(weight.universe, [0, 0, 50])
weight['Large'] = fuzz.trimf(weight.universe, [0, 100, 100])

# Define membership functions for Quality
quality['Bad'] = fuzz.trimf(quality.universe, [0, 0, 0.5])
quality['Medium'] = fuzz.trimf(quality.universe, [0, 0.5, 1])
quality['Good'] = fuzz.trimf(quality.universe, [0.5, 1, 1])

# Define fuzzy rules
rule1 = ctrl.Rule(size['Small'] & weight['Small'], quality['Bad'])
rule2 = ctrl.Rule(size['Small'] & weight['Large'], quality['Medium'])
rule3 = ctrl.Rule(size['Large'] & weight['Small'], quality['Medium'])
rule4 = ctrl.Rule(size['Large'] & weight['Large'], quality['Good'])

# Create fuzzy control system
quality_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
quality_evaluator = ctrl.ControlSystemSimulation(quality_ctrl)

# Input crisp values for Size and Weight
input_size = 10
input_weight = 100

# Fuzzify the inputs
size_value_small = fuzz.interp_membership(size.universe, size['Small'].mf, input_size)
size_value_large = fuzz.interp_membership(size.universe, size['Large'].mf, input_size)

weight_value_small = fuzz.interp_membership(weight.universe, weight['Small'].mf, input_weight)
weight_value_large = fuzz.interp_membership(weight.universe, weight['Large'].mf, input_weight)

# Evaluate the firing strength of each rule
activation_rule1 = min(size_value_small, weight_value_small)
activation_rule2 = min(size_value_small, weight_value_large)
activation_rule3 = min(size_value_large, weight_value_small)
activation_rule4 = min(size_value_large, weight_value_large)

# Calculate the aggregated membership value for each quality category
aggregated_bad = np.fmin(activation_rule1, quality['Bad'].mf)
aggregated_medium1 = np.fmin(activation_rule2, quality['Medium'].mf)
aggregated_medium2 = np.fmin(activation_rule3, quality['Medium'].mf)
aggregated_good = np.fmin(activation_rule4, quality['Good'].mf)

# Aggregate all the output membership functions together
aggregated = np.fmax(aggregated_bad, np.fmax(aggregated_medium1, np.fmax(aggregated_medium2, aggregated_good)))

# Check if the aggregated fuzzy set has any area under it
if np.sum(aggregated) == 0:
    print("Error: Total area is zero in defuzzification! Adjust input values or membership functions.")
else:
    # Calculate the crisp output using the Center of Gravity (CoG) method
    output_quality_cog = fuzz.defuzz(quality.universe, aggregated, 'centroid')
    print("Center of Gravity (CoG):", output_quality_cog)


   # Calculate the crisp output using the Center of Gravity (CoG) method

# Plot membership functions for Size, Weight, and Quality
size.view()
weight.view()
quality.view()


# Shade the regions for "Good" and "Medium" quality
x = quality.universe
plt.fill_between(x, quality['Good'].mf, color='green', alpha=0.3, label='Good Quality')
plt.fill_between(x, quality['Medium'].mf, color='yellow', alpha=0.3, label='Medium Quality')

# Plot the Center of Gravity (CoG) as a vertical dashed line
plt.axvline(x=output_quality_cog, color='red', linestyle='--', label='Center of Gravity (CoG)')

# Plot the line indicating the area under the aggregated membership functions
plt.plot(quality.universe, aggregated, 'k', linewidth=1.5, label='Aggregated Membership')

# # Plot the horizontal line indicating the CoG value
# plt.axhline(y=fuzz.interp_membership(quality.universe, aggregated, output_quality_cog), color='blue', linestyle='--', label='CoG Value')

# Add legend
plt.legend()

# Show the plot
plt.show()