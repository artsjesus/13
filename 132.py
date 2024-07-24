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

    # def add_pordict(self, product):
    # self.__products.append(product)
    # Category.product_count += 1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result


product_data = {
    'name': 'New Product',
    'description': 'New Description',
    'price': 500,
    'quantity': 5
}