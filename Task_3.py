class Store:
    def __init__(self, name):
        self.name = name


class GroceryStore(Store):
    def __init__(self, name):
        super().__init__(name)


class HardwareStore(Store):
    def __init__(self, name):
        super().__init__(name)


class Good:
    def __init__(self, price):
        self.price = price
        self.discount_percentage = 0
        self.discount_price = price

    def set_discount(self, percentage):
        self.discount_percentage = percentage
        self.discount_price = self.price * 0.01 * percentage


class Food(Good):
    def __init__(self, price):
        super().__init__(price)


class Banana(Food):
    def __init__(self):
        super().__init__()
        pass


class Apple(Food):
    def __init__(self):
        super().__init__()
        pass


class Ham(Food):
    def __init__(self):
        super().__init__()
        pass


class Water(Food):
    def __init__(self):
        super().__init__()
        pass


class Tool(Good):
    def __init__(self, price):
        super().__init__(price)


class Nail(Good):
    def __init__(self):
        super().__init__()
        pass


class Axe(Good):
    def __init__(self):
        super().__init__()
        pass


class Saw(Good):
    def __init__(self):
        super().__init__()
        pass


class Hammer(Good):
    def __init__(self):
        super().__init__()
        pass


