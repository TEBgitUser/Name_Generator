import logging

import mysql.connector
import time
import random
import math

config = {
  'user': 'admin1',
  'password': 'test1234',
  'host': '10.10.10.141',
  'port': '3306',
  'database': 'sakila',
  'raise_on_warnings': True
}

try:
    cnx = mysql.connector.connect(**config)
    logging.info("Połączono " + cnx.get_server_info())
    wybierz=int(input("1-Dodaj użytkownika"+"\n"))

    if(wybierz==1):
        with open("imiona_facetow.txt", 'r', encoding='UTF-8') as plik1:
            with open("imiona_kobiet.txt", 'r', encoding='UTF-8') as plik2:
                with open("nazwiska_facetow.txt", 'r', encoding='UTF-8') as plik3:
                    with open("nazwiska_kobiet.txt", 'r', encoding='UTF-8') as plik4:
                        with open("wygenerowane_imie.txt", 'w', encoding='UTF-8') as wynik:
                            tabm = []
                            tabw = []
                            tabnm = []
                            tabnw = []
                            tabp = ['m', 'w']
                            for wiersz in plik1:
                                wiersz = wiersz.strip().split(' ')
                                tabm.append(wiersz)
                            for wiersz in plik2:
                                wiersz = wiersz.strip().split(' ')
                                tabw.append(wiersz)
                            for wiersz in plik3:
                                wiersz = wiersz.strip().split(' ')
                                tabnm.append(wiersz)
                            for wiersz in plik4:
                                wiersz = wiersz.strip().split(' ')
                                tabnw.append(wiersz)
                            plec = random.choice(tabp)
                            logging.debug(plec)
                            id = random.randint(1,1001)
                            logging.debug(id)
                            if plec == 'm':
                                first_name = random.choice(tabm)
                                logging.debug(first_name)
                                last_name = random.choice(tabnm)
                                logging.debug(last_name)
                                logging.info("Meskie: "+str(id)+ str(first_name) + str(last_name) + '\n')
                            else:
                                first_name = random.choice(tabw)
                                logging.debug(first_name)
                                last_name = random.choice(tabnw)
                                logging.debug(last_name)
                                logging.info("Zenskie: "+ str(id)+str(first_name) + str(last_name))
        cursor = cnx.cursor()
        dodaj_aktora = ("INSERT INTO sakila.actor "
                   "(ID, Imie, Nazwisko) "
                   "VALUES (%s, %s, %s)")
        informacje_aktora=(int(id), str(first_name), str(last_name),)
        logging.info("Dodano użytkownika "+str(informacje_aktora))
        cursor.execute(dodaj_aktora, informacje_aktora)
        cnx.commit()
        cursor.close()
        cnx.close()
except Exception as ex:
    logging.warning("Problem z połączeniem "+str(ex))
