import csv
import json

def clima():
    resultado = {}
    
    with open('data_nuevo.csv', 'w', newline='') as file_csv:
        encabezados = ['id','location','temperature','pressure','above_avg_temp','above_avg_pres']
        writer = csv.DictWriter(file_csv,fieldnames=encabezados,delimiter=',')
        writer.writeheader()

    with open('data.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)

        temp = []; press=[]; temp2=[];press2=[];temp3 = []; press3 = []; temp4 = []; press4 = []; temp5 = []; press5 = []

        for linea in reader:
            if linea[1] == '1':
                temp.append(int(linea[2]))
                press.append(int(linea[3]))
            elif linea[1] == '2':
                temp2.append(int(linea[2])) 
                press2.append(int(linea[3]))
            elif linea[1] == '3':
                temp3.append(int(linea[2])) 
                press3.append(int(linea[3]))
            elif linea[1] == '4':
                temp4.append(int(linea[2])) 
                press4.append(int(linea[3]))
            elif linea[1] == '5':
                temp5.append(int(linea[2])) 
                press5.append(int(linea[3]))
        
        lista1=[]; lista2=[]; lista3=[]; lista4=[]; lista5=[];

        lista1.append(round(sum(temp)/len(temp),1))
        lista1.append(round(sum(press)/len(press),1))
        resultado['1'] = lista1

        lista2.append(round(sum(temp2)/len(temp2),1))
        lista2.append(round(sum(press2)/len(press2),1))
        resultado['2'] = lista2

        lista3.append(round(sum(temp3)/len(temp3),1))
        lista3.append(round(sum(press3)/len(press3),1))
        resultado['3'] = lista3

        lista4.append(round(sum(temp4)/len(temp4),1))
        lista4.append(round(sum(press4)/len(press4),1))
        resultado['4'] = lista4

        lista5.append(round(sum(temp5)/len(temp5),1))
        lista5.append(round(sum(press5)/len(press5),1))
        resultado['5'] = lista5

        datos = json.dumps(resultado) # Variable a retornar dentro del vpl
        with open('datos_json.json', 'w') as file_json:
            json.dump(resultado,file_json, indent=2)


    def comparar(a,b,c,d):
        temp = ''
        press = ''
        if a > b: temp = 'SI'
        elif a < b: temp = 'NO'
        elif a == b: temp = 'IGUAL'

        if c > d: press = 'SI'
        elif c < d: press = 'NO'
        elif c == d: press = 'IGUAL'

        return temp, press

    with open('data.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)

        with open('data_nuevo.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            for linea in reader: 
                if linea[1] == '1':   
                    above_temp,above_press = comparar(int(linea[2]),resultado['1'][0],int(linea[3]),resultado['1'][1])
                elif linea[1] == '2':
                    above_temp,above_press = comparar(int(linea[2]),resultado['2'][0],int(linea[3]),resultado['2'][1])
                elif linea[1] == '3':
                    above_temp,above_press = comparar(int(linea[2]),resultado['3'][0],int(linea[3]),resultado['3'][1])
                elif linea[1] == '4':
                    above_temp,above_press = comparar(int(linea[2]),resultado['4'][0],int(linea[3]),resultado['4'][1])
                elif linea[1] == '5':    
                    above_temp,above_press = comparar(int(linea[2]),resultado['5'][0],int(linea[3]),resultado['5'][1])

                writer.writerow([linea[0],linea[1],linea[2],linea[3],above_temp,above_press])
  
    return datos