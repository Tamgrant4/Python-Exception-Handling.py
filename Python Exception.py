# Q1 task 1

while True:
  try:
    # Get user input for temperature
    temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    break  # Exit the loop if input is valid (converted to a float)
  except ValueError:
    print("Invalid input. Please enter a number for the temperature.")

print("You entered:", temperature_fahrenheit, "degrees Fahrenheit.")

# Task 2

def fahrenheit_to_ celsius(temperature_fahrenheit):
  """Converts a temperature in Fahrenheit to Celsius.

  Args:
      temperature_fahrenheit: The temperature in Fahrenheit (float).

  Returns:
      The temperature in Celsius (float).
  """

  temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
  return temperature_celsius

# Task 3

while True:
  try:
    # Get user input for temperature
    temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter a number for the temperature.")

else:
  # Convert temperature if input is valid
  temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
  print("The temperature in Celsius is:", round(temperature_celsius, 2), "degrees.")

finally:
  # Thank the user regardless of exceptions
  print("Thank you for using the weather forecast application!")

def fahrenheit_to_celsius(temperature_fahrenheit):
  """Converts a temperature in Fahrenheit to Celsius.

  Args:
      temperature_fahrenheit: The temperature in Fahrenheit (float).

  Returns:
      The temperature in Celsius (float).
  """

  temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
  return temperature_celsius

# Q2 Task 1

while True:
  try:
    # Get original servings
    original_servings = int(input("Enter the number of servings the recipe is originally for: "))
    if original_servings <= 0:
      raise ValueError("Number of servings must be positive.")

    # Get desired servings
    desired_servings = int(input("Enter the number of servings you want to make: "))
    if desired_servings <= 0:
      raise ValueError("Number of servings must be positive.")
    break  # Exit the loop if both inputs are valid
  except ValueError as e:
    print("Invalid input:", e, ". Please enter positive numbers for servings.")

print("Original servings:", original_servings)
print("Desired servings:", desired_servings)

#Task 2

def adjust_recipe_quantities(original_servings, desired_servings):
  """Calculates the adjustment factor for a recipe based on desired servings.

  Args:
      original_servings (int): The original number of servings the recipe yields.
      desired_servings (int): The desired number of servings.

  Returns:
      float: The adjustment factor to scale the recipe's ingredient quantities.

  Raises:
      ValueError: If either `original_servings` or `desired_servings` is not a positive integer.
      ZeroDivisionError: If `original_servings` is zero.
  """

  if original_servings <= 0:
    raise ValueError("Number of original servings must be positive.")

  if desired_servings <= 0:
    raise ValueError("Number of desired servings must be positive.")

  adjustment_factor = desired_servings / original_servings
  return adjustment_factor

# Get user input for original and desired servings
while True:
  try:
    original_servings = int(input("Enter the number of servings the recipe is originally for: "))
    desired_servings = int(input("Enter the number of servings you want to make: "))
    break  # Exit the loop if both inputs are valid
  except ValueError:
    print("Invalid input. Please enter positive integers for servings.")

# Calculate and display the adjustment factor
try:
  adjustment_factor = adjust_recipe_quantities(original_servings, desired_servings)
  print("Adjustment factor:", adjustment_factor)
except (ValueError, ZeroDivisionError) as e:
  print("Error:", e)

# Optional: Prompt user for further actions (modifying recipe, etc.)
print("How would you like to use the adjustment factor?")
# ... (add options for recipe modification, ingredient scaling, etc.)

# Task 3

def adjust_recipe_quantities(original_servings, desired_servings):
  """Calculates the adjustment factor for a recipe based on desired servings.

  Args:
      original_servings (int): The original number of servings the recipe yields.
      desired_servings (int): The desired number of servings.

  Returns:
      float: The adjustment factor to scale the recipe's ingredient quantities.

  Raises:
      ValueError: If either `original_servings` or `desired_servings` is not a positive integer.
      ZeroDivisionError: If `original_servings` is zero.
  """

  if original_servings <= 0:
    raise ValueError("Number of original servings must be positive.")

  if desired_servings <= 0:
    raise ValueError("Number of desired servings must be positive.")

  adjustment_factor = desired_servings / original_servings
  return adjustment_factor

# Get user input for original and desired servings
while True:
  try:
    original_servings = int(input("Enter the number of servings the recipe is originally for: "))
    desired_servings = int(input("Enter the number of servings you want to make: "))
    break  # Exit the loop if both inputs are valid
  except ValueError:
    print("Invalid input. Please enter positive integers for servings.")

# Calculate and display the adjustment factor
try:
  adjustment_factor = adjust_recipe_quantities(original_servings, desired_servings)
  print("Adjustment factor:", adjustment_factor)

  # Display adjusted recipe quantities
  print("Adjusted Recipe Quantities:")
  for ingredient, quantity in recipe.items():  # Assuming a recipe dictionary
    adjusted_quantity = quantity * adjustment_factor
    print(f"- {ingredient}: {adjusted_quantity:.2f}")  # Format to 2 decimal places

except (ValueError, ZeroDivisionError) as e:
  print("Error:", e)

# Always print a final message
finally:
  print("Happy cooking!")
