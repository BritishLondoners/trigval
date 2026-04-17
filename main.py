import math #importing module

# Ask the user to enter an angle in degrees
angle_degrees = float(input("Enter angle in degrees: "))

# Convert degrees to radians (math functions use radians)
angle_radians = math.radians(angle_degrees)

# Calculate sin, cos, and tan
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)

# Handle tan separately to avoid division by zero
try:
    tan_value = math.tan(angle_radians)
except:
    tan_value = "Undefined"

# Display results
print(f"sin({angle_degrees}) = {sin_value}")
print(f"cos({angle_degrees}) = {cos_value}")
print(f"tan({angle_degrees}) = {tan_value}")