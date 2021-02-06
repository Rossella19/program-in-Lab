#libreria per estrarre i nomi dei file
from os import path


class ExamException(Exception):
    pass
         
class CSVTimeSeriesFile:

    #qui controlli di base
    def __init__(self, name):  
        
        # Setto il nome del file
        if not isinstance(name, str):
            raise ExamException('Il nome del file deve essere una stringa')
        #path.exists mi dice se il file con quel nome esiste
        if not path.exists(name):
            raise ExamException("Il file che hai indicato non esiste")

#il nome che gli passo diventa l'attributo della classe       
        self.name = name  

#funzione per la media
    def mean(self,array):
        sum=0
        for el in array:
            sum=sum+el
        return (sum/len(array))


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
 
            #non lo è la prima riga
            if data !="epoch" and valore != "temperature": 
                try:
                    # fai casting cioe cambio il tipo di avriabile
                    if valore != "" and valore is not None: 
                        data=int(data)
                        valore=float(valore)
                        if previous_data < data:
            #se sono in ordine temporale crescente li appende senno no

                            values.append(data)
                            values.append(valore)
                            response.append(values)
                except:
                    pass
                previous_data = data  #prendo il valore precedente

        my_file.close()
        return response

    def daily_stats(self,time_series): 
        """
        La funzione daily_stats prende in ingresso una lista di coppie di valori: [timestamp, misura_temperatura].
        Restituisce come output:
            [
                [valore_min_giorno_1, valore_max_giorno_1, valore_medio_giorno_1],
                [valore_min_giorno_2, valore_max_giorno_2, valore_medio_giorno_2],
            ]
        """
        response=[]   #lo ridefinisco
        day=[]        #mi contiene i valori tra ogni giorno

#time_series è quello che restituisce la get data, l'output
        for i in range(len(time_series)): 
            date= time_series[i][0]
            #valore della temperature
            value= time_series[i][1]  
            if i < len(time_series) -1:
                next=time_series[i+1]
            else:
                next=[0]   #mi serve per il passaggio successivo
            if next[0]%86400==0:
                #array che mi contiene min,max e media
                stats=[ min(day),max(day),self.mean(day) ] 
                response.append(stats)
            #se inizia un nuovo giorno azzaero array day e appendo il valore corrente altrimenti se non è divisbile appendo semplicemente il valore
            if date % 86400==0:  
                day=[]
                day.append(value)
            else:
                day.append(value)
        return response




csv=CSVTimeSeriesFile("date.csv")  #csv è il nome dell'istanza
time_series=csv.get_data()         #è la lista di liste
stats=csv.daily_stats(time_series)
print(stats)


