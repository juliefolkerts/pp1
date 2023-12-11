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

with open('ICAO.txt', 'w') as file:
    for key, value in NATO.items():
        file.write(f'{key} {value}\n')

with open('ICAO.txt', 'r') as file:
    content = file.read()
    print(content.strip())