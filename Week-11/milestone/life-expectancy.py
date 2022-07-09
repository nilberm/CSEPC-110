


lowest = 1000
lowestYear = 1000
lowestCountry = ""

higher = -1
higherYear = 1
higherCountry = ""

lowestChoice = 1000
lowestCountryChoice = ""

higherChoice = -1
higherCountryChoice = ""


lowestChoiceCountry = 1000
lowestYearChoiceCountry = 1000

higherChoiceCountry = -1
higherYearChoiceCountry = 1



choiceYear = int(input("Enter the year of interest: "))
choiceCountry = input("Enter the country of interest: ")
average = 0
numChoiceYear = 0


with open("Week-11\milestone\life-expectancy.csv") as lifeFile:
  for line in lifeFile:
    cleanLine = line.strip()
    words = cleanLine.split(",")

    country = words[0]
    code = words[1]
    year = int(words[2])
    lifeExp = float(words[3])

    if higher < lifeExp:
      higher = lifeExp
      higherYear = year
      higherCountry = country
    
    if lowest > lifeExp:
      lowest = lifeExp
      lowestYear = year
      lowestCountry = country

    # Year Choice Code
    if choiceYear == year:
      average += lifeExp
      numChoiceYear += 1

      if higherChoice < lifeExp:
        higherChoice = lifeExp
        higherCountryChoice = country
    
      if lowestChoice > lifeExp:
        lowestChoice = lifeExp
        lowestCountryChoice = country

    # Country Choice Code
    if choiceCountry.lower() == country.lower():
      if higherChoiceCountry < lifeExp:
        higherChoiceCountry = lifeExp
        higherYearChoiceCountry = year
    
      if lowestChoiceCountry > lifeExp:
        lowestChoiceCountry = lifeExp
        lowestYearChoiceCountry = year


print(f"\nThe overall min life expectancy is: {higher} from {higherCountry} in {higherYear}")

print(f"The overall min life expectancy is: {lowest} from {lowestCountry} in {lowestYear}")

print(f"\nFor the year {choiceYear}:")
print(f"The average life expectancy across all countries was {average / numChoiceYear:.2f}")
print(f"\nThe max life expectancy was in {higherCountryChoice} with {higherChoice}")
print(f"The min life expectancy was in {lowestCountryChoice} with {lowestChoice}")

print(f"\nFor the Country {choiceCountry}: ")
print(f"\nThe max life expectancy was in the year {higherYearChoiceCountry} with {higherChoiceCountry}")
print(f"The min life expectancy was in the year {lowestYearChoiceCountry} with {lowestChoiceCountry}")



