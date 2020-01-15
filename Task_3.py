class Store:
    def __init__(self):
        self.items = []
        self.overall_price_no_discount = 0
        self.overall_price_with_discount = 0
        self.good_type = Good

    def add_item(self, item):
        if isinstance(item, self.good_type):
            self.items.append(item)
            self.overall_price_no_discount += item.price
            self.overall_price_with_discount += item.discount_price
        else:
            print("This item cannot be added to this store")


    def add_items(self, *items):
        for item in items:
            self.add_item(item)

    def remove_item(self, item):
        self.items.remove(item)
        self.overall_price_no_discount -= item.price
        self.overall_price_with_discount -= item.discount_price


class GroceryStore(Store):
    def __init__(self):
        super().__init__()
        self.good_type = Food


class HardwareStore(Store):
    def __init__(self):
        super().__init__()
        self.good_type = Tool


class Good:
    def __init__(self, price):
        if not isinstance(price, (int,float)):
            raise TypeError("Wrong price type, should be int or float")
        elif price <= 0:
            raise ValueError("Wrong price value, should be positive")

        self._price = price
        self.discount_percentage = 0
        self.discount_price = price


    @property
    def price(self):
        return self._price


    def set_discount(self, percentage):
        self.discount_percentage = percentage
        self.discount_price = self._price * 0.01 * percentage


class Food(Good):
    pass


class Banana(Food):
    pass


class Apple(Food):
    pass


class Ham(Food):
    pass


class Water(Food):
    pass


class Tool(Good):
    pass


class Nail(Tool):
    pass


class Axe(Tool):
    pass


class Saw(Tool):
    pass


class Hammer(Tool):
    pass


belmarket = GroceryStore()
bananas = Banana(6)
apple = Apple(22)
belmarket.add_item(bananas)
belmarket.add_item(apple)
print(belmarket.overall_price_no_discount)

belmarket.remove_item(apple)
apple.set_discount(50)
belmarket.add_item(apple)
print(belmarket.overall_price_no_discount)
print(belmarket.overall_price_with_discount)

hammer = Hammer(50)
belmarket.add_item(hammer)
