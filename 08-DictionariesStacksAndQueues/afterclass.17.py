NATO = {
    'A' : 'Alpha', 
    'B': 'Bravo', 
    'C' : 'Charlie',
    'D' : 'Delta', 
    'E' : 'Echo',
    'F' : 'Foxtrot', 
    'G' :'Golf',
    'H' : 'Hotel',
    'I' : 'India',
    'J' : 'Juliett',
    'K' : 'Kilo',
    'L' :'Lima', 
    'M' : 'Mike',
    'N' : 'November',
    'O' : 'Oscar',
    'P' : 'Papa',
    'Q' : 'Quebec',
    'R' : 'Romeo',
    'S'  :'Sierra',
    'T' : 'Tango',
    'U' : 'Uniform',
    'V' : 'Victor',
    'W' : 'Whiskey',
    'X' : 'X-ray',
    'Y' : 'Yankee',
    'Z' : 'Zulu'
}

def spel(txt):
    txt = txt.upper()
    text = []
    txtNATO = []
    for char in txt:
        text.append(char)
    for i in range(0,len(text)):
        for key,value in NATO.items():
            if text[i] == key:
                x = NATO[key]
                txtNATO.append(x)
    result = ' '.join(txtNATO)
    return result



txt = input('Enter word\n')
print(spel(txt))
