print("Part One")

import sys
def get_input():
    if sys.stdin.isatty():
        return input ("Enter data (date, time, store, item, cost, payment) separated by tabs, or press Enter to finish: ")
    else:
        return sys.stdin.readline().strip()
    
while True:
    line = get_input()

    if line =="":
        break

    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print(f"{item}\t{cost}")
        break
    else:
        print("Invalid input. Please eneter 6 values separated by tabs.")

print("Input finished.")

print("Part Two")
from datetime import datetime, timedelta

# Current datetime
now = datetime.now()
print(f"Current datetime: {now}")

# Add timedelta and perform operations
result = now + timedelta(days=1) - timedelta(seconds=60) + timedelta(days=365*2)
print(f"Result: {result}")

print("Part Three")
from datetime import timedelta

delta = timedelta(days=100, hours=10, minutes=13)
print(f"Timedelta: {delta}")
print(f"Total seconds: {delta.total_seconds()}")

print("Part Four")
from datetime import datetime

def height_with_time(feet, inches):
    current_time = datetime.now()
    total_inches = feet * 12 + inches
    return f"Height: {feet}'{inches}\" ({total_inches} inches) - Recorded at {current_time}"

# Example usage
print(height_with_time(5, 1))