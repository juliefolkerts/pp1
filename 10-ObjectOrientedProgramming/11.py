class TV():
    def __init__(self,is_on=False,channel_no=1):
        self.is_on = is_on 
        self.channel_no = str(channel_no)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = str(new_channel_no)
    
    def show_status(self):
        if self.is_on == True:
            return 'On, channel ' + self.channel_no
        else:
            return 'Off'
#a     
tv = TV()
#b
print(tv.show_status())
#c
tv.turn_on()
#d
print(tv.show_status())
#e
tv.set_channel(5)
#f
print(tv.show_status())
#g
tv.turn_off()
#h
print(tv.show_status())
