

class Restaurant:
    restaurants = []
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        Restaurant.restaurants.append(self)
    @classmethod
    def Restaurant_List(cls):
            print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'} \n')
            for restaurant in Restaurant.restaurants:
                print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.status}')
        
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @property
    def status(self):
        return '☑' if self._status else '☐'
    def Alter_state(self):
        self._status = not self._status
