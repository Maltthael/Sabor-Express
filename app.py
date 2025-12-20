from models.restaurant import Restaurant
from models.cardapio.drinks import Drinks
from models.cardapio.dishes import Dish
from models.cardapio.dessert import Dessert



restaurant_BambooDuro = Restaurant('BambooDuro', 'Chinesa')
drink_suco = Drinks('Suco de melancia', 5.0, 'grande')
drink_suco.apply_discount()
dish_paozinho = Dish('Paozinho',2.00,'O melhor pão da cidade')
dish_paozinho.apply_discount()
dessert_bolo = Dessert('Bolo de uva', 5.0, '45 cm', 'Muito gostoso')
dessert_bolo.apply_discount()
restaurant_BambooDuro.add_in_cardapio(drink_suco)
restaurant_BambooDuro.add_in_cardapio(dish_paozinho)
restaurant_BambooDuro.add_in_cardapio(dessert_bolo)


def main():
    restaurant_BambooDuro.show_cardapio
    
    
if __name__ == '__main__':
    main()