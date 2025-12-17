from models.evaluation import Evaluation

class Restaurant:
    restaurants = []
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        self._evaluation = []
        
        Restaurant.restaurants.append(self)
    @classmethod
    def Restaurant_List(cls):
            print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliação'.ljust(25)} | {'Status'} \n')
            for restaurant in Restaurant.restaurants:
                print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.avg_evaluation).ljust(25)} | {restaurant.status}')
        
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @property
    def status(self):
        return '☑' if self._status else '☐'
    def Alter_state(self):
        self._status = not self._status
    
    def Receive_evaluation(self, client, rating):
        if  0 < rating <=5: 
            evaluation = Evaluation(client, rating)
            self._evaluation.append(evaluation)
        
    
    
    @property    
    def avg_evaluation(self):
        if not self._evaluation:
            return '-'
        sum_rating = sum(evaluation._rating for evaluation in self._evaluation)
        rating_quantity = len(self._evaluation)
        avg = round(sum_rating / rating_quantity, 1)
        return avg
