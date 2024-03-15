from rubrica_library import Rubrica

def main():
    r = Rubrica()
    string_output="""
        digita il numero corrispondente alla scelta:
            1) aggiungi contatto
            2) cancella contatto
            3) visualizza tutti i contatti
            4) visualizza tutti i gruppi
            5) cancella tutti contatti di un dato gruppo
            6) visualizza gruppi con numero di contatti
            0) esci
            
    """
    ris=''
    continua=True
    scelta=None
    while continua:
        ris=input("vuoi autenticarti o registrarti? a/r :")
        usr=input("inserisci username:")
        psw=input("inserisci password:")
        if ris=='r':
            print(r.registraUtente(usr,psw))
        if ris=='r' or ris=='a':
            print(r.accedi(usr,psw))
            continua=False
    
    while scelta!="0":
        scelta=input(string_output)
        if scelta=="1":
            nome=input("inserisci il nome:")
            cognome=input("inserisci il cognome:")
            numero=input("inserisci il numero:")
            gruppo=input("inserisci il gruppo (scrivi NO per non metterlo):")
            if gruppo!="NO":
                print(r.addContact(nome,cognome,numero,gruppo)+"\r\n")
            else:
                print(r.addContact(nome,cognome,numero)+"\r\n")
            
        if scelta=="2":
            print("contatti in rubrica: \r\n")
            arr_contacts=r.visualizzaContatti()

            print(printContacts(arr_contacts))
            id=input("inserire l'id del contatto da eliminare (scrivi NO per non cancellare):")
            if id!="NO":
                print(r.deleteContact(id))
        if scelta=="3":
            print("contatti in rubrica: \r\n")
            arr_contacts=r.visualizzaContatti()
            print(printContacts(arr_contacts))
        if scelta=="4":
            print("gruppi in rubrica: \r\n")
            arr_gruppi=r.visualizzaGruppi()
            print(printGroups(arr_gruppi)+"\r\n")
        if scelta=="5":
            print("gruppi in rubrica: \r\n")
            arr_gruppi=r.visualizzaGruppi()
            print(printGroups(arr_gruppi)+"\r\n")
            if len(arr_gruppi)==0:
                continue
            gruppo=input("inserire il gruppo da eliminare (scrivi NO per non cancellare):")
            if gruppo=="NO":
                continue
            print(f"contatti in rubrica del gruppo {gruppo}: \r\n")

            arr_contacts=r.visualizzaContatti(nomeGruppo=gruppo)
            print(printContacts(arr_contacts)+"\r\n")

            conferma=input("vuoi confermare l'eliminazione del gruppo (s/n):")
            if conferma=="n":
                continue
            print(r.deleteContacts(arr_contacts))
        if scelta=="6":
            print(r.printGruppi())
        

def printContacts(arr_contacts):
    s=""
    for c in arr_contacts:
        s+="id: "+str(c["id"])+" nome: "+str(c["nome"])+" cognome: "+str(c["cognome"])+" numero: "+str(c["numero"])
        if c["gruppo"]!=None:
            s+=" gruppo: "+str(c["gruppo"])
        s+="\r\n"
    return s

def printGroups(arr_gruppi):
    s=""
    for g in arr_gruppi:
        s+= "gruppo: " + str(g) +"\r\n"
    
    if len(s)<1:
        return "non vi sono gruppi in rubrica"
    return s

if __name__=="__main__":
    main()