class Pizza:
    """Класс который описывает экземпляр пиццы(в одном параметре - название,описание и цена)
    Пиццу можно заказать - записать в список
    пиццу можно удалить из списка покупок
    и можно оформить заказ,указав сумму клиента"""

    def __init__(self,name,description,price):
        self.name = name
        self.desc = description
        self.price = price
        self.list = []

    def __repr__(self):
        return f'Пицца {self.name}'

    def order(self,pizza):
        self.list.append(pizza)


    def delete(self):
        self.list.pop()

    def get_order(self,money):
        if money >= self.price:
            result = money-self.price
            if result == 0:
                return 'Ваш заказ оформлен'
            else:
                return f'Ваша сдача : {result}'
        else:
            return "Недостаточно средств"

pizza1 = Pizza('Pepperoni','сырная',450)
pizza2 = Pizza('Chili','с перцем',480)
pizza1.order(pizza1)
print(pizza1.list)
pizza2.order(pizza2)
print(pizza2.list)







