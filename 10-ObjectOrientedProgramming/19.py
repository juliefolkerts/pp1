from Thermometer import Therm

therm1 = Therm()
therm1.turn_on()
therm1.measure_temp()
print(therm1.message())
therm1.turn_off()
