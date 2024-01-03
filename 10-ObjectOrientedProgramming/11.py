class TV():
    def __init__(self,is_on=False,channel_no=1,channels=[],volume=0):
        self.is_on = is_on 
        self.channel_no = str(channel_no)
        self.channels = channels
        self.volume = int(volume)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = str(new_channel_no)

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        return self.channels
    
    def vol_up(self):
        if self.volume < 10:
            self.volume = self.volume + 1
        else:
            self.volume = 10

    def vol_down(self):
        if self.volume > 0:
            self.volume = self.volume - 1
        else:
            self.volume = 0

    
    def show_status(self):
        if self.is_on == True and int(self.channel_no) <= int(len(self.channels)) :
            return 'On, channel ' + self.channel_no + f' ({self.channels[int(self.channel_no)-1]})' + f' volume:{str(self.volume)}'
        elif self.is_on == True and int(self.channel_no) > int(len(self.channels)) :
            return 'On, channel ' + self.channel_no + f' volume:{str(self.volume)}'
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
print(tv.show_channels())
#f
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
#g
print(tv.show_channels())
tv.set_channel(1) #if it is 0 it shows discovery how to fix this?
tv.vol_down()
#h
print(tv.show_status())
#i
tv.turn_off()
#j
print(tv.show_status())
