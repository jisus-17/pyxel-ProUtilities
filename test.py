import time

positions = [4, 55, 64, 32, 16, 32, 60, 90]

length = len(positions)

i = 0

while i < length:
    print(positions[i])
    print(positions[i + 1])
    time.sleep(0.5)
    i += 2

# implementar en sensors.py
