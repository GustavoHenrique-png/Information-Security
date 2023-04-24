import urllib.request
import json

#Cabecalho pro print
hostTitle = 'Host details\n'
countryTitle = 'Country details\n'

dotNumber = 70
countryPadding = 50
detailPadding = 40

#Aceitando todos os tipos de formatos de ip disponibilizados peol geojs
ipValidTypes = ['plain', 'json', 'jsonp']
ipPlain = 'http://get.geojs.io/v1/ip'
ipJson = 'http://get.geojs.io/v1/ipjson'
ipLookup = {'plain': ipPlain, 'json': ipJson}

#Aceitando todos os tipos de formatos de pais disponibilizado pelo geojs
countryValidTypes = ['plain', 'json', 'jsonp', 'plainfull']
countryPlain = 'https://get.geojs.io/v1/ip/country'
countryFullPlain = 'https://get.geojs.io/v1/ip/country/full'
countryJson = 'https://get.geojs.io/v1/ip/country/{ip address}.json'
countryLookup = {'plain' : countryPlain, 'plainfull' : countryFullPlain, 'json' : countryJson}

geoJson = 'https://get.geojs.io/v1/ip/geo/{ip address}.json'
ptrPlain = 'https://get.geojs.io/v1/dns/ptr'

def getPlainResponse(url):
    return urllib.request.urlopen(url).read().decode().strip()

def getJsonResponse(url,ipAddress):
    response = urllib.request.urlopen(url.replace('{ip address}',ipAddress)).read().decode

def getIP(returnType = 'plain'):
    if isinstance(returnType,str):
        returnType = returnType.lower()
        if returnType in ipValidTypes:
            if returnType == 'plain':
                return getPlainResponse(ipLookup[returnType])
            else:
                return getJsonResponse(ipLookup[returnType],'')
        else:
            raise ValueError('\'Esse retorno\' Nao pertence aos tipos aceitos ' + str(ipValidTypes))
    else:
        raise TypeError('\'Este retorno\' deveria ser do tipo \'str\'(' + type(returnType).__name__ + ' was given).')

def getCountry(ipAddress, returnType = 'plain'):
    if not isinstance(ipAddress,str):
        raise TypeError('\'ipAddress\' is not an instance of \'str\'('+ type(ipAddress).__name__ + ' was given).')
    if isinstance(returnType,str):
        returnType = returnType.lower()
        if returnType in countryValidTypes:
            if returnType == 'plain':
                return getPlainResponse(countryLookup[returnType] + '/' + ipAddress)
            elif returnType == 'plainfull':
                return getPlainResponse(countryLookup[returnType] + '/' + ipAddress)
            else:
                return getJsonResponse(countryLookup[returnType], ipAddress)
        else:
            raise ValueError('\'returnType\' does not belong in valid types: ' + str(countryValidTypes))
    else:
        raise TypeError('\'returnType\' must be of type \'str\'(' + type(returnType).__name__ + ' was given).')

def getGeoData(ipAddress):
    if isinstance(ipAddress, str):
        return getJsonResponse(geoJson, ipAddress)
    else:
        raise TypeError("\'ipAddress\' is not an instance of list.")

def getPTR(ipAddress):
    if not isinstance(ipAddress, str):
        raise TypeError("\'ipAddress\' is not an instance of list.")
    return getPlainResponse(ptrPlain)

def showCountryDetails(ip=''):
    result = ""
    if ip == '':
        ip = getIP('plain')
    countryData = getCountry(ip, 'json')
    result += '-' * dotNumber + '\n'
    result += (dotNumber//2 - len(countryTitle)//2) * ' ' + countryTitle
    result += '-' * dotNumber + '\n'
    for key, value in countryData.items():
        cleanKey = key.replace('_',' ').capitalize() + ':'
        cleanKey = cleanKey.ljust(countryPadding, ' ')
        result += cleanKey + str(value) + '\n'
    result += '-' * dotNumber + '\n'
    print(result)

def showIpDetails(ip=''):
    result = ""
    if ip == '':
        ip = getIP('plain')
    country = getCountry(ip, 'plainFull')
    result += '-' * dotNumber + '\n'
    result += (dotNumber//2 - len(hostTitle)//2) * ' ' + hostTitle
    result += '-' * dotNumber + '\n'
    result += 'Country: '.ljust(countryPadding,' ') + country + '\n'
    geoData = getGeoData(ip)
    ptrData = getPTR(ip)
    for key, value in geoData.items():
        cleanKey = key.replace('_',' ').capitalize() + ':'
        cleanKey = cleanKey.ljust(countryPadding,' ')
        result += cleanKey + str(value) + '\n'
    result += '-' * dotNumber + '\n'
    print(result)

ip = getIP()
print(ip)

country = getCountry(ip, 'plain')
print(country)

country = getCountry(ip, 'json')
print(country)

geoData = getGeoData(ip)
print(geoData)

ptrData = getPTR(ip)
print(ptrData)

showIpDetails('216.239.32.0')

showCountryDetails('216.239.32.0')