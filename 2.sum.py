
def sum_list(the_list):
    total = 0
    for item in the_list:
        total = total + item
    return total


def sum_csv_data(filename):
    # Inizializzo una lista vuota per salvare i valori
    values = []
    # Apro e leggo il file, linea per linea
    my_file = open(filename, 'r')
    for line in my_file:
        # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',')

        # Se NON sto processando l’intestazione...
        if elements[0] != 'Date':
                # Setto la data e il valore
                date  = elements[0]
                value = elements[1]
                # Aggiungo alla lista dei valori questo valore
                values.append(float(value))
    
    values_sum = sum_list(values) 
    return values_sum


csv_data_sum = sum_csv_data('shampoo_saless.csv') 

print(csv_data_sum)