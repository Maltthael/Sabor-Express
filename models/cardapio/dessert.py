from models.cardapio.item_cardapio import ItemCardapio

class Dessert(ItemCardapio):
    def __init__(self, name, price, size, description):
        super().__init__(name, price)
        self.size = size
        self.description = description
        
    def __str__(self):
        return self._name
    def apply_discount(self):
        self._price -= self._price * 0.07