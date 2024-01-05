class TV():
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            return 'TV is on'
        else:
            return 'TV is of'
        
tv = TV()
print(tv.show_status())
tv.turn_on()
print(tv.show_status())
tv.turn_off()
print(tv.show_status())
