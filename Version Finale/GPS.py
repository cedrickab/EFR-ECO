import requests
def getLoca():
    loca=[]
    res= requests.get('https://ipinfo.io/')
    data=res.json()
    location = data['loc'].split(',')
    latitude=location[0]
    loca.append(latitude)
    longitude=location[1]
    loca.append(longitude)
    return loca