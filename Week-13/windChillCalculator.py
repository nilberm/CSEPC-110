temperature = float(input("What is the temperature? "))
typeTemperature = input("Fahrenheit or Celsius (°F/°C)? ").upper()
resultsTemperature = input("The results in Fahrenheit or Celsius (°F/°C)? ").upper()


speeds = [5,10,15,20,25,30,35,40,45,50,55,60]

if typeTemperature == "F":
  for i in speeds:
    windchill = 35.74 + (0.6215 * temperature) - (35.75 * (i ** 0.16)) + (0.4275 * temperature * (i ** 0.16))
    print(f"At temperature {temperature}°F, and wind speed {i} mph, the windchill is: {windchill:.2f}°F")
if typeTemperature == "C" and resultsTemperature == "F":
  temperature = (temperature * (9 / 5) ) + 32
  for i in speeds:
    windchill = 35.74 + (0.6215 * temperature) - (35.75 * (i ** 0.16)) + (0.4275 * temperature * (i ** 0.16))
    print(f"At temperature {temperature}°F, and wind speed {i} mph, the windchill is: {windchill:.2f}°F")
if typeTemperature == "C" and resultsTemperature == "C":
  temperatureF = (temperature * (9 / 5) ) + 32
  for i in speeds:
    windchill = 35.74 + (0.6215 * temperatureF) - (35.75 * (i ** 0.16)) + (0.4275 * temperatureF * (i ** 0.16))
    windchillC = (windchill - 32) * (5 / 9)
    print(f"At temperature {temperature}°C, and wind speed {i} mph, the windchill is: {windchillC:.2f}°C")