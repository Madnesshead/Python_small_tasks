class Store:
    def __init__(self, name):
        self.name = name


class GroceryStore(Store):
    def __init__(self, price):
        super().__init__(price)


class HardwareStore(Store):
    def __init__(self, price):
        super().__init__(price)


class Good:
    def __init__(self, price, discount_percentage):
        self.price = price
        self.discount_percentage = discount_percentage

    def set_discount(self, price, discount_percentage):
        discount_price = price * 0.01 * discount_percentage
        return discount_price


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


