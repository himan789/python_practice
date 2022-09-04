import car
cc=car.make_car('toyota','suv',color='white',tow_package='True')
print(cc)

from car import make_car
cc=make_car('toyota','suv',color='white',tow_package='True')
print(cc)

from car import make_car as mc
cc=mc('toyota','suv',color='white',tow_package='True')
print(cc)

import car as cr
cc=cr.make_car('toyota','suv',color='white',tow_package='True')
print(cc)

from car import *
cc=make_car('toyota','suv',color='white',tow_package='True')
print(cc)
