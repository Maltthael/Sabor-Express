from models.cardapio.item_cardapio import ItemCardapio

class Dish(ItemCardapio):
    def __init__(self, name, price, description):
        super().__init__(name, price)#acessa atributos da classe ItemCardapio
        self.description = description
        
    def __str__(self):
        return self._name
    def apply_discount(self):
        self._price -= self._price * 0.08