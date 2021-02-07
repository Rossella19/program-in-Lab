#libreria per estrarre i nomi dei file
from os import path

#le eccezioni da alzare in caso di input non corretti o casi limite devono essere istanze di una specifica classe ExamException
class ExamException(Exception):
    pass


#classe creata estendendo la classe CSVFile che ho fatto in classe    
class CSVTimeSeriesFile:

    def __init__(self, name):  
        
        # Setto il nome del file
        if not isinstance(name, str):
            raise ExamException('Il nome del file deve essere una stringa')
        #path.exists mi dice se il file con quel nome esiste
        if not path.exists(name):
            raise ExamException("Il file che hai indicato non esiste")

#la classe deve essere istanziata sul nome del file tramite la variabile name
#il nome che gli passo diventa l'attributo della classe       
        self.name = name  

#funzione per la media, mi prende l'array e mi fa la media dei suoi elementi e me la ritorna con il return
    def mean(self,array):
        sum=0
        for el in array:
            sum=sum+el
        return (sum/len(array))

# la classe CSVTimeSeriesFile ha un metodo get_data che deve tornarmi una lista di liste dove il primo elemento delle liste annidate è l'epoch(numero secondi passati) e il secondo elemento è la temperatura
    def get_data(self):
       
    
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None  
            # ad esempio se è file con password o corrotto

        #contiene la lista di liste da restituire alla fine di get data
        response=[] 
#è =0 perche mi serve per il primissimo confronto per verificare che lordine delle date sia crescente
#mi stampo le varie temperature nelle ore della giornata  
        previous_data = 0 
        for line in my_file:
            data, valore=line.split(",")
            # Inizializzo una lista vuota per salvare i valori
            values = []         
 
            #non lo è la prima riga. Quello che voglio dopo lo fa solo se non mi trovo alla prima riga del mio file, ossia quella con su scritto "epoch,temperature",
            if data !="epoch" and valore != "temperature": 
                try:
                    # fai casting cioe cambio il tipo di variabile, solo se come chiesto nella consegna i valori di temperatura(che ho chiamato valore), che leggo dal file CSV, non li voglio di tipo non numerico, oppure vuoto o nullo ma sono da aspettarsi di tipo numerico (intero o floating point)
                    if valore != "" and valore is not None: 
                        #I timestamp epoch (i miei data) che leggete da file sono di tipo intero. Se per caso dovessero esserci dei timestamp epoch floating point, vanno convertiti silenziosamente ad interi (tramite cast diretto con int(), non tramite arrotondamento) 
                        data=int(data)
                        #come appena detto i valori della temperatura li voglio di tipo numerico
                        valore=float(valore)
                        if previous_data < data:
            #se sono in ordine temporale crescente li appende senno no
            #appendo pian piano ogni data e ogni valore(ossia la mia temperatura)all'array che ho creato che si chiama values, che ha dentro le mie date e le mie temperature, tranne la prima riga del mio file ossia quella dove c'è scritto "epoch,temperature" che non la voglio

                            values.append(data)
                            values.append(valore)
            #poi dopo aver inserito nel mio array values la mia data e il mio valore della temperatura, appendo ossia "aggiungo" il mio array values, contenente data e valore (ossia la temperatura), nell'altro array creato prima che si chiama response e che quindi è un array contenente l'array values
                            response.append(values)
                except:
                    pass
                    #cosi ogni volta confronto con il precedente per essere sicura che siano in ordine crescente perchè se così non fosse non li appendo e passo avanti, questo me lo fa ogni fine del ciclo
                previous_data = data  
                
        
        #chiudo il mio file
        my_file.close()

        #il metodo get_data alla fine mi restituisce, mi da come output l'array response, un array che mi contiene l'array values dove trovo le date e i valori della temperatura
        return response


#Per calcolare le statistiche giornaliere dovete invece creare una funzione a sé stante (cioè posizionata non nella classe CSVTimeSeriesFile ma direttamente nel corpo principale del programma), di nome daily_stats.
#La funzione dovrà ritornare (tramite un return) in output sempre una lista di liste, dove però ogni lista annidata rappresenta la statistica giornaliera di un dato giorno, ovvero la tripletta di temperatura minima, massima e media.
# time_series è quello che restituisce get_data, l'output
    def daily_stats(self,time_series): 
        """
        La funzione daily_stats prende in ingresso una lista di coppie di valori: [timestamp, misura_temperatura]
        Restituisce come output:
            [
                [valore_min_giorno_1, valore_max_giorno_1, valore_medio_giorno_1],
                [valore_min_giorno_2, valore_max_giorno_2, valore_medio_giorno_2],  ...........
            ]
        """
        #lo ridefinisco, è l'array di array che alla fine mi conterrà i dati divisi per giornate
        response=[]  
        #array che mi conterrà i valori (values) della giornata..dopo farò il amx,min e media dei valori in day e li metto in un altro array
        day=[]   

       #faccio il processo tot volte fino a quando l'indice i ha la lunghezza di time_series, in questo modo mi "studio" tutte le righe
        for i in range(len(time_series)): 
            #con il mio for guardo pian piano tutte le righe, grazie all'indice i che ogni giro cresce fino a raggiungere la lunghezza di time-series, e la data sarà sempre l'elemento nella prima colonna (quindi [0])
            #me lo vedo un pò come una matrice in cui ogni giro del for mi guardo una riga diversa, quella dopo, ma comunque sula prima colonna ho sempre le date
            date= time_series[i][0]
            #value (ossia il valore della temperature) sarà invece sempre l'elemento nella seconda colonna(quindi [1])
            value= time_series[i][1]

            #lunghezza -1 perchè gli dico che c'è il next(ossia il valore successivo) ma solo se non è l'ultimo
           #se non mi trovo all'ultima riga
            if i < len(time_series) -1:
                next=time_series[i+1]
            else:
                next=[0]   
           
            #se next è divisibile per 86400 vuol dire che il valore attuale sarà l'ultimo valore del giorno corrente mentre il prossimo valore(next)sarà l'inizio di un nuovo giorno e quindi dal prossimo valore dovrò inserire i dati in un nuovo array
            #devo capire quando inizia il prossimo giorno in modo che possa aggiungere correttamente il giorno nell'array giusto.
            if next[0]%86400==0:

                #stats è l'array che mi contiene min,max e media della giornata; in pratica sotto ho fatto si che l'array day mi contenga i valori delle temperature di un giorno e ora in stats, conoscendo i valori presenti nell'array day, ne trovo il valore massimo e minimo, grazie alla funzione di python che mi dati i valori me li trova lui con la funzione, e poi la media che invece la trovo grazie alla funzione che ho creato io mean
                stats=[ min(day),max(day),self.mean(day) ] 
                 #una volta creato l'array stats lo devo anche aggiungere alla lista di liste (response) che conterrà i dati suddivisi per giornate 
                response.append(stats)

            #se "date" è divisibile per 86400 vuol dire che è mezzanotte e che inizia un nuovo giorno, allora se succede questo devo azzerare il mio array day dato che è un nuovo giorno e in esso ci appendo pian piano i miei value, ossia i valori delle temperature e quando rinizia la giornata azzererò di nuovo l'array day e pian piano ci metterò i value di quel giorno. 
            if date % 86400==0:  
                day=[]
                day.append(value)
            #altrimenti se non è divisbile appendo semplicemente il valore perchè mi trovo ancora in quel giorno e quindi continuo a metetrci i miei value di quel giorno
            else:
                day.append(value)

        #La funzione dovrà ritornare (tramite un return) in output sempre una lista di liste, dove però ogni lista annidata rappresenta la statistica giornaliera di un dato giorno, ovvero la tripletta di temperatura minima, massima e media.   
        return response



#time_series_file è il nome dell'istanza
time_series_file=CSVTimeSeriesFile("data.csv")  
time_series=time_series_file.get_data()      
stats=time_series_file.daily_stats(time_series)
print(stats)



