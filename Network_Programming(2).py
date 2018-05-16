import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.facebook.com/dyi/?x=AdkZoO2GQNigIwe-&tab=all_archives&referrer=notif&notif_id=1526488266354079&notif_t=dyi')
for line in fhand:
    print(line.decode().strip())


