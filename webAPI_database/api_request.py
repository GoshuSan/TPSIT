import requests


URL = "http://127.0.0.1:5000/allBooks"
URL_INSERT = "http://127.0.0.1:5000/insertBook"
URL_ALL = "http://127.0.0.1:5000/allBooks"
URL_BYID = "http://127.0.0.1:5000/bookById"


def ricercaPerId(id):
def ID_research(id):
    PARAMS = {'id':id}
    PARAMS = {'id':id}
    r = requests.get(url = URL, params = PARAMS)
    r = requests.get(url = URL_BYID, params = PARAMS)
    data = r.json()[PARAMS['id']]
    data = r.json()[PARAMS['id']]
    print(f"libro cercato --> {data}")
    print(f"libro cercato --> {data}")


def tuttiLibri():
def allBooks():
    r=requests.get(url=URL)
    r=requests.get(url=URL_ALL)
    data = r.json()
    data = r.json()
    for i in data:
    for i in data:
        print(i)
        print(i)



def insertBook(title,author,year):

    PARAMS = {'title':title,'author':author,'published':year}
tuttiLibri()
    r = requests.get(url=URL_INSERT, params=PARAMS)
print("^^^^^^^^^^^^^^^^^^^")
    print('dati inviati')
ricercaPerId(1)
    if r :

        print(r)



#tuttiLibri()
#data = r.json()[PARAMS['id']]
#print("^^^^^^^^^^^^^^^^^^^")
#print(data['title']) 

