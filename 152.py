from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __add__(self, other):
        pass


class MixinInit:
    """Класс примесь описания"""

    def __repr__(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self._Product__price}, {self.quantity})")


class Product(BaseProduct, MixinInit):
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__repr__()


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError

    @classmethod
    def new_product(cls, product: dict):
        name, description, price, quantity = product.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Category:
    """
    Класс для категорий товара
    """
    # list_name = []
    # list_products = []

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        sum_ = 0
        for i in self.__products:
            sum_ += i.quantity

        return f"{self.name}, количество продуктов: {sum_} шт."


    # def add_new_products(self):
    #     return self.__products


    # def add_new_products(self, product):
    #     if isinstance(product, LawnGrass) or isinstance(product, Smartphone) or isinstance(product, Product):
    #         self.__products.append(product)
    #         Category.category_count += 1



    @property
    def products(self):
        str_prod = ''
        for i in self.__products:
            str_prod += f"{i.name}, {i._Product__price} руб. Остаток: {i.quantity} шт.\n"
        return str_prod

    @products.setter
    def products(self, product):
        if isinstance(product, Product) or isinstance(product, Smartphone) or isinstance(product, LawnGrass):
            self.__products.append(product)
            Category.category_count += 1
        else:
            raise TypeError


class Smartphone(Product, MixinInit):
    """Класс описывающий смартфоны"""

    def __init__(self, name: str, description: str, price: int, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity * self._Product__price + other.quantity * other._Product__price
        else:
            raise TypeError

class LawnGrass(Product, MixinInit):
    """Класс описывающий траву"""

    def __init__(self, name: str, description: str, price: int, quantity: int, country: str, germination_period: str,
                     color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity * self._Product__price + other.quantity * other._Product__price
        else:
            raise TypeError