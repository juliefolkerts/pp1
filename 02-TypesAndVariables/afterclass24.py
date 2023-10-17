vehicle_registration_no  = input('Enter vehicle registraionnumber:\n')
if (vehicle_registration_no[0] == ('K')) and (vehicle_registration_no[1] == ('K') or vehicle_registration_no[1] == 'R'):
    print('Car from Kraków: True')
else:
    print('Car from Kraków: False')