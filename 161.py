from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

class Mixin:
    def __init__(self):
        print(str(self))

    def __str__(self):
        pass

class Product(BaseProduct, Mixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        print(repr(self))

    @classmethod
    def new_product(cls, product):
        return cls(product["name"], product["description"], product["price"], product["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __add__(self, other):
        result = self.__price * self.quantity + other.__price * other.quantity
        if type(other) is not Product:
            raise TypeError('')
        return result

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"



class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    @property
    def products(self):
        products_info = ''
        for product in self.__products:
            products_info += f"{str(product)} + \n"
        return products_info

    @products.setter
    def products(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    def average_price(self):
        try:
            total_price = sum([prod.price for prod in self.__products])
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def middle_price(self):
        return self.average_price()

    def __str__(self):
        total_quantity_count = sum([prod.quantity for prod in self.__products])
        return f'{self.name}, количество продуктов: {total_quantity_count} шт.'