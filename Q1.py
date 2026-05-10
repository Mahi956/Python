# print(10)
# print('a')

# b=90

# leap year code
year = 2019
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
print( is_leap_year(year))