class Phone():
    def __init__(self,nr,code,battery):
        self.nr = nr
        self.code = code
        self.battery = battery

    def display_battery(self):
        return self.battery+'%'
    
    def display_whole_nr(self):
        return self.code + self.nr
    
    def __str__(self):
        return f"Phone: {self.display_whole_nr()} - Battery: {self.display_battery()}"
    
phone1 = Phone('21265815','+316','80')
phone2 = Phone('21265815','+316','40')
print(phone1.display_battery())
print(phone2.display_whole_nr())

    