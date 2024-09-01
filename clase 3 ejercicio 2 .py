def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = 25
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit:.2f}°F")


print(f"0°C es igual a {celsius_a_fahrenheit(0):.2f}°F")
print(f"100°C es igual a {celsius_a_fahrenheit(100):.2f}°F")
print(f"-40°C es igual a {celsius_a_fahrenheit(-40):.2f}°F")