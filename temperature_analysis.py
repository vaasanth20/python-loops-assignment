# Name: Vasanth Dhandapani
# Roll Number: IITP_AIMLTN_2602559
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Start by assuming the first temperature is both the highest and lowest
highest = temperatures[0]
lowest = temperatures[0]

# Loop through each temperature in the list
for temp in temperatures:
    # If current temperature is greater than highest, update highest
    if temp > highest:
        highest = temp
    # If current temperature is less than lowest, update lowest
    if temp < lowest:
        lowest = temp

# Print the results
print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Counter to keep track of hot days
hot_days = 0

# Loop through each temperature in the list
for temp in temperatures:
    # If temperature is 30°C or below, skip it using continue
    if temp <= 30:
        continue         # Jump to the next iteration, ignore the rest of the loop body
    # Only reaches here if temperature is above 30°C
    hot_days += 1        # Count this as a hot day

print(f"Hot Days (>30°C): {hot_days}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

# Counter for hot days found before the alert
hot_days = 0

# Variables to store alert details (None means no alert yet)
alert_day = None
alert_temp = None

# enumerate() gives both the index and value; start=1 makes day count from 1
for day, temp in enumerate(temperatures, start=1):

    # Check for extreme temperature first — if found, trigger alert and stop
    if temp >= 40:
        alert_day = day      # Save which day the extreme temperature occurred
        alert_temp = temp    # Save the extreme temperature value
        break                # Stop the loop immediately, do not check remaining days

    # If temperature is hot (>30°C) but not extreme, count it
    if temp > 30:
        hot_days += 1

# Print how many hot days were found before the alert was triggered
print(f"Hot Days before alert: {hot_days}")

# If an alert was triggered, print the alert message
if alert_day:
    print(f"Alert! Extreme temperature {alert_temp}°C detected on Day {alert_day}")