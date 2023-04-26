class Product:
    def __init__(self,type,name,price):
        self.type = type
        self.name = name
        self.price = price
        self.income = 0

class ProductStore:
    def __init__(self):
        self.product_list = []
        self.income = 0
        self.info = ()

    def add(self, product, amount):
        for item in self.product_list:
            if product.name == list(item.keys())[0]:
                item[product.name][0] += amount
                return
        self.product_list.append({product.name: [amount, product.type, product.price * 1.3]})

    def set_discount(self, identifier, percent, identifier_type='name'):
        for i in self.product_list:
            if identifier in i:
                i[identifier][2] *= (100-percent)/100
        print(self.product_list)

    def sell_product(self, product_name, sell_amount):
        for i in self.product_list:
            if product_name in i:
                if sell_amount < i[product_name][0]:
                    i[product_name][0] -= sell_amount
                    self.income += sell_amount * i[product_name][2]
                else:
                    raise ValueError("You don't have enough product to sell.")
                return
            # raise ValueError("Try again.")

    def get_income(self):
        print(self.income)
        return self.income

    def get_all_products(self):
        print(self.product_list)
        return self.product_list

    def get_product_info(self, product_name):
        for i in self.product_list:
            if product_name in i:
                self.info = (product_name, i[product_name][0])
                print(self.info)
                return self.info

p = Product('Sport', 'Football T-Shirt', 100)
# p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
# s.add(p2, 300)
s.add(p, 20)
s.add(p, 10)
# s.get_product_info('Football T-Shirt')
# s.sell(‘Ramen’, 10)
# s.set_discount('Ramen',50)
# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
print(s.product_list)

