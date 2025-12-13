# Functions: Exercise 6 (Arbitrary Arguments with Keyword Arguments)
# Program Description: Car Maker

def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    print(car_info)

make_car("toyota", "corolla", color='black', trunk=True)