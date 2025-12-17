from models.restaurant import Restaurant

restaurant_BuguerHero = Restaurant('BurguerHero', 'FastFood')
restaurant_BuguerHero.Alter_state()
restaurant_BuguerHero.Receive_evaluation('Joao', 10)
restaurant_BuguerHero.Receive_evaluation('Roberto', 3)
restaurant_PizzaPlanet = Restaurant('PizzaPlanet', 'Italian')
restaurant_ChickenFingers = Restaurant('ChickenFingers', 'Fastfood')
restaurant_ChickenFingers.Alter_state()
restaurant_PizzaPlanet = Restaurant('BambooDuro', 'Chinesa')

def main():
    Restaurant.Restaurant_List()
    
if __name__ == '__main__':
    main()