# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 06:43:01 2021

@author: pizza
"""

# Se cargan las librerias incluidas PANDAS para la creacion de Data Frames
# Manejo de arreglos con numpy y fechas con datetime
import pandas as pd
import numpy as np
from datetime import datetime

# SE DEFINE EL PRIMER EJERCICIO EN UNA FUNCION
def ejercicio_01():
    # SE CREA UN DATA FRAME AUXILIAR PARA DARLE VALORES DE PRECEDENCIA A LOS STATUS
    status_prio = pd.DataFrame({'status':['PENDING', 'SHIPPED','CANCELLED'],
                            'ord_': [1,2,3]} )
    # SE CARGA LA TABLA DE LAS ORDENES
    customer_ord_lines = pd.read_table("ej1_insumo.txt")
    # MEDIANTE UN MERGE SE AGREGA LA VARIABLE "ord_" A LA TABLA "customer_ord_lines"
    customer_ord_lines = customer_ord_lines[['order_number', 'status']].merge(status_prio, how = 'left', on = 'status' )
    # SE CREAN AGRUPACIONES DE "order number",
    # SE ORDENA LA TABLA DE MANERA ASCENDENTE RESPECTO A "ord_"
    #Y SE TOMAN LOS PRIMEROS VALORES DE CADA GRUPO
    customer_ord_lines = customer_ord_lines.sort_values('ord_').groupby('order_number').first().reset_index().drop(columns = ['ord_'])
    return(customer_ord_lines)

ej_1 = ejercicio_01()
print(ej_1)


# FUNCION CON EL SEGUNDO EJERCICIO
def ejercicio_02():
    # SE CARGA LA TABLA CON LAS FECHAS 
    customer_orders = pd.read_table("ej2_insumo.txt")
    # SE CAMBIAN LOS VALORES DE FECHAS A TIPO "datetime64"
    customer_orders['ORD_DT'] = customer_orders['ORD_DT'].astype('datetime64')
    # CREAMOS LA TABLA "seasons" DONDE ALMACENAMOS LA INFORMACION DE ESTACIONES
    # NOTEMOS QUE EN LOS ANYOS SE DEJO UN VALOR DUMMY "1"
    seasons = pd.DataFrame({'SEASON':['Spring','Summer', 'Fall', 'Winter'], 
                            'PER_1': ['03/19/1', '06/20/1', '09/22/1', '12/21/1'],
                            'PER_2': ['06/19/1', '09/21/1', '12/20/1', '03/18/1'] })
    # DE MANERA ANÁLOGA A LA TABLA "customer_orders" CAMBIAMOS EL TIPO DE LAS 
    # COLUMNAS AL TIPO DE NUMPY "datetime64"
    seasons['PER_1'] = seasons['PER_1'].astype('datetime64')
    seasons['PER_2'] = seasons['PER_2'].astype('datetime64')
    
    # CREAMOS UNA LISTA VACIA PARA ALMACENAR LA ESTACION A LA CUAL PERTENECE
    # CADA DIA EN LA TABLA "customer_orders"
    season_list = list()
    #PARA CADA DIA "i"-esimo EN QUE SE HIZO LA ORDEN
    for i in range(len(customer_orders)):
        
        # SE CAMBIA EL TIPO DEL DIA DE ORDEN AL TIPO datetime
        # UTILIZAMOS ESTA LIBRERIA YA QUE ES MAS SENCILLO HACER
        # LA MANIPULACION Y COMPARACION DE FECHAS
        day_order = customer_orders['ORD_DT'][i]
        # Y SE ALMACENA EN LA VARIABLE "day_new"
        day_new = datetime(2000, day_order.month, day_order.day )    
        print(str(i)+": "+str(day_new) )
        
        # PARA CADA ESTACION DEL AÑO....
        for j in range(4):
            day_01_np = seasons['PER_1'][j]
            day_02_np = seasons['PER_2'][j]
            
            season_str = datetime(2000, day_01_np.month, day_01_np.day)
            season_end = datetime(2000, day_02_np.month, day_02_np.day)
            
            # SE COMPRUEBA EN QUE ESTACION SE ENCUENTRA
            if day_new>=season_str and day_new<=season_end:
                # SE AÑADE LA ESTACION A LA LISTA DE ESTACIONES
                season_list.append( seasons['SEASON'][j] )
                break
            
            if (day_new>=datetime(2000,12,20) or day_new<=datetime(2000,3,18) ):
                season_list.append( 'Winter' )
                #SE UTILIZA BREAK PARA EVITAR EL COMPROBAR LAS DEMAS 
                #POSIBILIDADES CUANDO YA SE ENCONTRO UNA
                break
    # FINALMENTE SE AÑADE LA COLUMNA CON LA ESTACION A LA CUAL PERTENECE EL DIA
    # EN QUE SE HIZO LA ORDEN
    customer_orders['SEASONS'] = season_list
    return(customer_orders)
ej_2 = ejercicio_02()
print(ej_2)

# FUNCION CON EL TERCER EJERCICIO
def ejercicio_03():
    # SE CARGA LA INFORMACION DE CLIMA
    weather = pd.read_table("ej3_insumo.txt")
    #SE FILTRA EL VALOR TRUE PARA LA COLUMNA "was_rainy"
    rainy_weather = weather[weather['was_rainy']==True]
    return(rainy_weather)
ej_3 = ejercicio_03()
print(ej_3)