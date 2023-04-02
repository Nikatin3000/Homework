name = 'Vadim'
day = str(12.03)

print("Good day", name + '! ' + day,'is a perfect day to learn some python.') # 1 option

name = 'Vadim'
day = 12.03

print(f"Good day {name}! {day} is a perfect day to learn some python.") # 2 option

print("Good day {0}! {1} is a perfect day to learn some python.".format(name,day)) # 3 option

print("Good day %s! %.2f is a perfect day to learn some python." % (name, day)) # 4 option






