class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание трех магазинов
store1 = Store("Фрукты", "Ленина, 50")
store2 = Store("Все для дома", "Горького, 10")
store3 = Store("Гастроном", "Калинина,20")

# Добавление товаров
store1.add_item("яблоко", 80)
store1.add_item("Банан", 150)

store2.add_item("наушники", 350)
store2.add_item("зарядка для телефона", 150)


store3.add_item("хлеб белый", 25)
store3.add_item("булка Ромашка", 40)


# Тест добавления товара
store1.add_item("апельсин", 70)
print(f"Товары после добавления апельсинов: {store1.items}")

# Тест обновления цены товара
store1.update_price("яблоко", 70)
print(f"Цены после обновления цены на яблоки: {store1.items}")

# Тест удаления товара
store1.remove_item("bananas")
print(f"Товары после удаления бананов: {store1.items}")

# Тест получения цены товара
price = store1.get_price("яблоко")
print(f"Цена яблок: {price}")