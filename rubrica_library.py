import requests

ipaddr="localhost"

class Rubrica:
    def __init__(self):
        self.url_base="http://"+ipaddr+":8080/"
        self.token=""
        pass

    def registraUtente(self,usr,psw):
        url = self.url_base+"regist"
        response=requests.get(url,params={
            "username":usr,
            "password":psw
        })
        data= response.json() #{"status":"error","message":"Utente gi\u00e0 registrato"}
        if data["status"]=="error":
            return data["message"]
        
        return "utente registrato correttamente"
    
    def accedi(self,usr,psw):
        url= self.url_base+"getToken"
        response=requests.get(url,params={
            "username":usr,
            "password":psw
        })
        data= response.json() #{"status":"error","message":"....."}
        if data["status"]=="error":
            return data["message"]
        

        #{"status":"ok","result":{"token":"e7c28cabf7e3b098489c4413ce0faba0"}}

        self.token=data["result"]["token"]
        print(self.token)
        
        return "accesso eseguito correttamente"
    
    def addContact(self,nome,cognome,numero,gruppo=None):
        url= self.url_base+"addContact"

       
        params={
                "token":self.token,
                "nome":nome,
                "cognome":cognome,
                "numero":numero,
                "gruppo":gruppo
        }

        response=requests.get(url,params=params)
        data= response.json() #{"status":"error","message":"....."}
        if data["status"]=="error":
            return data["message"]
        
        return "contatto inserito correttamente"
        
    def visualizzaContatti(self,nomeGruppo=None):
        
        url= self.url_base+"getContacts"
        response=requests.get(url,params={
            "token":self.token,
        })

        data= response.json() #{"status":"error","message":"....."}
        if data["status"]=="error":
            return data["message"]
        
        #{"status":"ok","result":[{"id":157,"nome":"aaa","cognome":"bbb","numero":"123456","gruppo":null},{"id":158,"nome":"manuel","cognome":"provenzi","numero":"3333","gruppo":null}]}
        arr_contacts = []
        if nomeGruppo:
            for c in data["result"]:
                if c["gruppo"]==nomeGruppo:
                    arr_contacts.append(c) 
        else:
            arr_contacts = data["result"]
        
        return arr_contacts
    
    def deleteContact(self,id):
        url= self.url_base+"deleteContact"
        response=requests.get(url,params={
            "token":self.token,
            "id":id
        })

        data= response.json() #{"status":"error","message":"....."}
        if data["status"]=="error":
            return data["message"]
        
        print(response.url)
        return f"contatto {id} eliminato correttamente"        

    def visualizzaGruppi(self):
        
        url= self.url_base+"getGroups"
        response=requests.get(url,params={
            "token":self.token,
        })

        data= response.json() #{"status":"error","message":"....."}
        if data["status"]=="error":
            return data["message"]
        
        #{"status":"ok","result":[null,"abc"]}
        arr_groups =[]

        for g in  data["result"]:
            if g==None | g=="" | g=="null":
                continue
            else:
                arr_groups.append(g)
        
        return arr_groups

    def deleteContacts(self,arr_contacts):
        s=""
        for c in arr_contacts:
            s+=(self.deleteContact(c["id"])+"\r\n")
        
        return s

    def printGruppi(self):
        arr_gruppi=self.visualizzaGruppi()
        if len(arr_gruppi)==0:
            return "non vi sono gruppi in rubrica"
        arr_numero_contatti=[]
        [ arr_numero_contatti.append(len(self.visualizzaContatti(nomeGruppo=g))) for g in arr_gruppi ]

        arr_gruppi,arr_numero_contatti=self.__ordina_decrescente(arr_gruppi,arr_numero_contatti)

        string_output="gruppi - numero contatti:\r\n"
        for i in range(0,len(arr_gruppi)):
            g=arr_gruppi[i]
            n=arr_numero_contatti[i]
            string_output+=g+" - "+str(n)+"\r\n"
        
        return string_output

    def __ordina_decrescente(self,arr_gruppi,arr_numero):
        
        arrSortato=[]
        arrSortato_copia=[]
        arrSortatoGruppi=[]

        [arrSortato.append(n) for n in arr_numero]
        [arrSortato_copia.append(n) for n in arrSortato]

        arrSortato.sort(reverse=True)
        arrSortato_copia.sort(reverse=True)
        

        for i in range(0,len(arr_numero)):
            arrSortatoGruppi.append(None)

        for i in range(0,len(arr_numero)):
            n=arr_numero[i]
            g=arr_gruppi[i]
            pos_sorted=self.__search(arrSortato_copia,n)
            arrSortatoGruppi[pos_sorted]=g
            arrSortato_copia[pos_sorted]=None

        return arrSortatoGruppi,arrSortato
    
    def __search(self,arr,val):
        for i in range(0,len(arr)):
            if arr[i]==val:
                return i
        return None

#test:
#r=Rubrica()

#print(r.registraUtente("manu","manu"))
#print(r.accedi("manu","manu"))
#print(r.addContact("manuel","provenzi","3334","abcd"))
#print(r.addContact("manuel","provenzi","3334","abcd"))
#print(r.addContact("manuel","provenzi","3334","abcde"))
#print(r.addContact("manuel","provenzi","3334","abcde"))
#print(r.addContact("manuel","provenzi","3334","abcde"))
#print(r.addContact("manuel","provenzi","3334","eeee"))
#print(r.addContact("manuel","provenzi","3334","eeee"))
#print(r.addContact("manuel","provenzi","3334","eeee"))
#print(r.addContact("manuel","provenzi","3334","eeee"))



#print(r.deleteContact(158))
#print(r.visualizzaContatti())
#print(r.visualizzaGruppi())
#print(r.printGruppi())
