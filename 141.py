class Product:
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product):
        name, description, price, quantity = product.values()
        return cls(name, description, price, quantity)

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    def __len__(self):
        return self.quantity


class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(self.products)
        Category.category_count += 1

    def __str__(self):
        total_products_count = sum([p.quantity for p in self.__products])
        return f'{self.name}, количество продуктов: {total_products_count} шт.'

    def add_porduct(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result