#messaggio d’errore se si cerca di aprire un file non esistente.
#messsaggio d'errore se start o end non validi
#eccezione se il nome del file non è una stringa.


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
