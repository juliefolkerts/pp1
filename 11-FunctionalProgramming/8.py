def ms_to_kmh(ms):
    ms = int(ms)
    mh = ms * (60*60)
    kmh = mh / 1000
    return kmh

print(ms_to_kmh(10))