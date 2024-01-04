import random
class Therm():
    def __init__(self,temp=0):
        self.temp = temp
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temp(self):
        temperature = round(random.uniform(34.0,42.0), 1)
        self.temp = temperature

    def message(self):
        if self.temp < 37.0:
            return f'Temperatur: {self.temp}c'
        elif 41.0 > self.temp > 37.0:
            return f'Temperatur: {self.temp}c (fever)'
        else:
            return f'Temperatur: {self.temp}c (CRITICAL TEMPERATURE!)'

