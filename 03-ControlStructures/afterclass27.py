instagram = bool(input('Do you have instagram?'))
facebook = bool(input('Do you have facebook?'))
twitter = bool(input('Do you have twitter?'))
if (instagram + facebook + twitter) == True:
    print('You are a good influencer!!')
else:
    print('You are a bad influencer')