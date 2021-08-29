tempurature = float(input("Enter tempurature: "))
temperature_scale = input("Enter C or F: ")

if temperature_scale == 'C' or temperature_scale == 'c':
    print("Convert to F...")
    result = ((float(float(tempurature))) * (float(1.8)) + (float(32)))
    print(str(tempurature) + ' C = ' + (str(result)) + ' F')

elif temperature_scale == 'F' or temperature_scale == 'f':
    print("Convert to C...")
    result = ((float(tempurature)) - (float(32))) / (float(1.8))
    print(str(tempurature) + ' F = ' + (str(result)) + ' C')
