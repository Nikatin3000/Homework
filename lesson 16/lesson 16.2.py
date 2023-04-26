class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, number):
        self.number = number
        return [num**2 for num in number]

    def remove_positives(self,num):
        self.num = num
        return [i for i in num if i<0]


    def filter_leaps(self,years):
        self.years = years
        return [year for year in years if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]


number = [7, 11, 5, 4]
num = [26, -11, -8, 13, -90]
years = [2001, 1884, 1995, 2003, 2020]
m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]