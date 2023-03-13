# hw classes
# #1
# import random
#
# class variable:
#     def __init__(self,var1,var2):
#         self.var1 = var1
#         self.var2 = var2
#
#     def print(self):
#         print(self.var1)
#         print(self.var2)
#
#     def Random(self):
#         self.var1 = random.randint(1,101)
#         self.var2 = random.randint(1,101)
#         print(self.var1)
#         print(self.var2)
#
#     def sum(self):
#         print(self.var1 + self.var2)
#
#     def maxvar(self):
#         if (self.var1 > self.var2):
#             print(f'max:'+ (str(self.var1)))
#         else:
#             print(f'max:' + (str(self.var2)))
#
# v = variable(2,4)
# v.print()
# v.Random()
# v.sum()
# v.maxvar()

# 2
# class Counter:
#     current = 0
#     def __init__(self, start=None, end=None):
#         self.start = start
#         self.end = end
#
#     def increase(self):
#         if self.current < self.end:
#             self.current +=1
#             return self.current
#         else:
#             return 'out of range'
#
#     def decrease(self):
#         if self.current < self.end:
#             self.end -=1
#             return self.end
#         else:
#             return 'out of range'
#
#
# count = Counter(start = 0, end = 4)
#
# print(count.decrease())
# print(count.decrease())
# print(count.decrease())
# print(count.decrease())
# print(count.decrease())
# print(count.increase())
# print(count.increase())
# print(count.increase())
# print(count.increase())

#3
class Product:
    def __init__(self, prod_name: str):
        self.prod_name = prod_name

    def __repr__(self) -> str:
        return f'{self.prod_name}'

class Shop:
    def __init__(self, *products: Product):
        self.products = list(products)

    def app_prod(self, product: Product):
        self.products.append(product)

    def remove_prod(self, product: Product):
        self.products.remove(product)

my_shop = Shop(Product('молоко'))
my_shop.app_prod(Product('хлеб'))
print(my_shop.products)