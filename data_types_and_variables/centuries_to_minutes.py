centuries = int(input())
years = centuries * 100
days = int(365.2422 * years)
hours = int(days * 24)
minutes = int(hours * 60)
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")