from models.restaurant import Restaurant
from models.cardapio.drinks import Drinks
from models.cardapio.dishes import Dish







restaurant_BambooDuro = Restaurant('BambooDuro', 'Chinesa')
drink_suco = Drinks('Suco de melancia', 5.0, 'grande')
drink_suco.apply_discount()
dish_paozinho = Dish('Paozinho',2.00,'O melhor pão da cidade')
dish_paozinho.apply_discount()
restaurant_BambooDuro.add_in_cardapio(drink_suco)
restaurant_BambooDuro.add_in_cardapio(dish_paozinho)


def main():
    restaurant_BambooDuro.show_cardapio
    
    
if __name__ == '__main__':
    main()