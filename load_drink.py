from app import app, db  # Adjust the import based on your app structure
from models import Drink

# List of drinks to add
drinks_to_add = [
    {'drink_name': 'gls house red', 'drink_cost': 2.00},
    {'drink_name': 'gls house white', 'drink_cost': 2.00},
    {'drink_name': 'gls Chapeau Melon Blanc', 'drink_cost': 2.00},
    {'drink_name': 'gls Picpoul', 'drink_cost': 2.00},
    {'drink_name': 'gls rose cantina', 'drink_cost': 2.00},
    {'drink_name': 'gls Semillon', 'drink_cost': 2.00},
    {'drink_name': 'gls Prosecco', 'drink_cost': 2.00},
    
    {'drink_name': 'gls Malbec', 'drink_cost': 3.00},
    {'drink_name': 'gls Diamarine', 'drink_cost': 3.00},
    {'drink_name': 'gls Chablis', 'drink_cost': 3.00},
    {'drink_name': 'gls Sauvignon Bob', 'drink_cost': 3.00},
    
    {'drink_name': 'gls Roland Bauchet', 'drink_cost': 5.00},
    {'drink_name': 'gls Exton Park', 'drink_cost': 5.00},
    
    {'drink_name': 'Coca Cola', 'drink_cost': 1.00},
    {'drink_name': 'Diet Coke', 'drink_cost': 1.00},
    {'drink_name': 'Fever-Tree', 'drink_cost': 1.00}
]


def load_drinks():
    with app.app_context():
        for drink in drinks_to_add:
            new_drink = Drink(drink_name=drink['drink_name'], drink_cost=drink['drink_cost'])
            db.session.add(new_drink)
        db.session.commit()
        print("Drinks loaded successfully!")

if __name__ == '__main__':
    load_drinks()