country_name = []
country_initials = []
years = []
life_expectancy = []

with open("life-expectancy.csv") as life_expectancy_file:
  for line in life_expectancy_file:

    list_info = line.split(",")
    country_name.append(list_info[0])
    country_initials.append(list_info[1])
    years.append(list_info[2])
    life_expectancy.append(list_info[3].strip("\n"))


index_highest_expectancy = 0
index_lowest_expectancy = 0

value_life = -1
value_life2 = 9999999

for i, value in enumerate(life_expectancy):
  value = float(value)
  if value > value_life:
    value_life = value
    index_highest_expectancy = i
  if value < value_life2:
    value_life2 = value
    index_lowest_expectancy = i



# user_year = input("\nEnter the year of interest: ")

print(f"\nThe overall max life expectancy is: {life_expectancy[index_highest_expectancy]} from {country_name[index_highest_expectancy]} in {years[index_highest_expectancy]}")
print(f"The overall min life expectancy is: {life_expectancy[index_lowest_expectancy]} from {country_name[index_lowest_expectancy]} in {years[index_lowest_expectancy]}")


# index_user_year = years.index(user_year)

# count_years = 0
# count_years_amount = 0

# index_highest_expectancy_year = 0
# index_lowest_expectancy_year = 0

# value_life_year = -1
# value_life2_year = 9999999

# country_name_user = []
# country_initials_user = []
# years_user = []
# life_expectancy_user = []

# for i, value in enumerate(years):
#   if value == user_year:
#     count_years += 1
#     count_years_amount += float(life_expectancy[i])

#     country_name_user.append(country_name[i])
#     country_initials_user.append(country_initials[i])
#     years_user.append(years[i])
#     life_expectancy_user.append(life_expectancy[i])

    
#     value_float = float(value)
#     if value_float > value_life_year:
#       value_life_year = value_float
#       index_highest_expectancy_year = i
#     if value_float < value_life2_year:
#       value_life2_year = value_float
#       index_lowest_expectancy_year = i




# print(f"\nFor the year {user_year}:")
# print(f"The average life expectancy across all countries was {count_years_amount / count_years:.2f}")
# print(f"The max life expectancy was in {country_name[index_highest_expectancy_year]} with {life_expectancy[index_highest_expectancy_year]}")
# print(f"The min life expectancy was in {country_name[index_lowest_expectancy_year]} with {life_expectancy[index_lowest_expectancy_year]}")






