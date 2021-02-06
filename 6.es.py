#’implementazione del modello
#Implementate il metodo fit() nel modello della lezione precedente. #Il fit deve, come appena descritto, calcolare l’incremento medio su tutto il dataset e salvarlo da qualche parte (es: self.global_avg_increment). Poi modificate il metodo predict() in modo che usi l’incremento medio su tutto il dataset appena calcolato, anche qui come appena descritto

#per graficare i dati e/o la predizione:
#data = [8,19,31,41,50,52,60]
#prediction = 68
#from matplotlib import pyplot
#pyplot.plot(data + [prediction], color='tab:red')
#pyplot.plot(data, color='tab:blue')
#pyplot.show()


#per visualizzare grafici
from matplotlib import pyplot


#classe modello generale
class Model:
    def fit(self, data):
        pass
    def predict(self):
        pass

#classe modello per shampoo (no fit)
class IncrementModel(Model):
    #incremento medio da un dataset di mesi
    def compute_avg_increment(self, prec_months):
        incr= 0
        for i in range(len(prec_months) -1 ):
            incr += prec_months[i+1]- prec_months[i]
        return incr/(len(prec_months)-1)

    def fit (self, data):
        self.global_avg_increment = self.compute_avg_increment(data)

    #predice il valore del mese successivo a quelli passati come parametro nella lista
    def predict (self, prec_months):
        return prec_months[len(prec_months)-1] + self.compute_avg_increment(prec_months) 


class CSVFile:
    def __init__(self, name):
        if type(name)!= str:
            raise Exception ("il nome non è una stringa")
        elif name =='':
          raise Exception("il nome non può essere vuoto")
        else:
            self.name = name
    


    def __str__(self):
        return "file CSV di nome {}.\n".format(self.name)
    
    #restituisce lista di dati float del file
    def get_data(self, start = None, end = None):
        try:
            file = open(self.name, "r")
        except:
            raise Exception ("impossibile aprire il file\n")
        values=[]

        i=start


        #nel file CSV ogni riga è scritta in questo modo: "data, valore float"
        for line in file:
            elements = line.split(",")

            if elements[0] != 'Date':
                date  = elements[0]
                value = elements[1]
            try:
                try:
                    value = float(value)
                except Exception as e:
                    
                    print('Errore nela conversione a float: "{}"'.format(e))
                    continue

                values.append(value)

        my_file.close()


        try:
            print(data[start:end])
            return data[start:end]
        except:
            print("start o end non validi, restituisco file intero")
            return values


#apro il CSV
mio_file = CSVFile("shampoo/shampoo_sales.csv")

#leggo i dati del file
values = mio_file.get_data()

