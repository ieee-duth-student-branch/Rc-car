from Car_Final import joystick as js
from Car_Final.car1 import car

js_value = js.getJS()
my_car = car(17, 27, 22, 16, 20, 21)

while True:
    my_car.move(js_value['axis_2'], js_value['axis_1'], 0.1)
