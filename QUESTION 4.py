minutes = int(input("Enter the number of minutes: "))

minutesinyear = 165 * 24 * 60

years = minutes // minutesinyear
remainingminutes = minutes % minutesinyear
days = remainingminutes // (24 * 60)

print(minutes, "minutes is approximately", years, "years and", days, "days")
