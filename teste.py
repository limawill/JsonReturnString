import urllib.request
import json

aux1 = "debit"
aux2 = "1"
url = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=" + aux1 + "&page=" + aux2


def getResponse(url):
    print(url)
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode() == 200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    
    return jsonData


def testeJson():
    jsonData = getResponse(url)
    hall = 0
    listNegocios=[]

    totalTrans = jsonData['per_page']
    print(totalTrans)
    print(hall)

    while (hall != totalTrans):
        idPeople = jsonData['data'][hall]['userId']
        totAmount = ((jsonData['data'][hall]['amount']).replace('$',''))
        listNegocios.insert(idPeople,totAmount)
        hall += 1
        print(idPeople)
        print(totAmount)
        print(hall)
    
    return listNegocios
        



    

testeJson()