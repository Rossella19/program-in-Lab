#messaggio d’errore se si cerca di aprire un file non esistente.

#classe per leggere file csv
class CSVFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception('messaggio di errore')
        self.name = name
    


    def __str__(self):
        return "file CSV di nome {}.\n".format(self.name)
    
    #restituisce lista di dati float del file
    def get_data(self):
        try:
            file = open(self.name, "r")
        except:
            raise Exception ("impossibile aprire il file\n")
        values=[]
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
        return values
