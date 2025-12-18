from models.restaurant import Restaurant
from models.cardapio.drinks import Drinks
from models.cardapio.dishes import Dish

restaurant_BuguerHero = Restaurant('BurguerHero', 'FastFood')
restaurant_BuguerHero.Alter_state()
drink_suco = Drinks('Suco de melancia', 5.0, 'grande')
Dish_paozinho = Dish('Paozinho',2.00,'O melhor pão da cidade')
restaurant_BuguerHero.Receive_evaluation('Joao', 5)
restaurant_BuguerHero.Receive_evaluation('Roberto', 5)
restaurant_PizzaPlanet = Restaurant('PizzaPlanet', 'Italian')
restaurant_PizzaPlanet.Receive_evaluation('Gilmar', 3)
restaurant_PizzaPlanet.Receive_evaluation('Vilma', 2)
restaurant_ChickenFingers = Restaurant('ChickenFingers', 'Fastfood')
restaurant_ChickenFingers.Alter_state()
restaurant_ChickenFingers.Receive_evaluation('Gerson', 3)
restaurant_ChickenFingers.Receive_evaluation('Roberto', 7)
restaurant_BambooDuro = Restaurant('BambooDuro', 'Chinesa')
restaurant_BambooDuro.Receive_evaluation('Figueiredo', 6)
restaurant_BambooDuro.Receive_evaluation('Fernanda', 2)

def main():
    Restaurant.Restaurant_List()
    
if __name__ == '__main__':
    main()