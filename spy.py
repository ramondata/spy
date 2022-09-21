#!/usr/bin/env python3

from sys import argv
from sys import stdout
import pandas as pd
import csv

class escolheFrame:


    def __init__(self):
        self.__frame: str = None
        self.__str__()


    def __str__(self):
        return """ Escolha uma das opções
            1 - Módulo csv
            2 - Pandas
            3 - Spark
            """


    def set_frame(self, frame: str) -> str:
        if(frame == "1"):
            self.__frame = "Module csv"
        elif(frame == "2"):
            self.__frame = "Pandas"
        elif(frame == "3"):
            self.__frame = "Spark"
        else:
            self.__str__()


    @property
    def frame(self) -> str:
        return "%s" % self.__frame


class leituraArquivoCsv:


    def __init__(self):
        self.__nomeArquivo: str = None
        self.__header: bool = True
        self.__extensao: str = "csv"
        self.__temSeparador: bool = True
        self.__delimiter: str = ";"
        self.__arq: None = None
        self.__csv_list: list = []


    def csvPy(self):
        self.__arq = open("/Users/ramon/Documents/Dados/aluguel.csv", "r")
        r = csv.reader(self.__arq, delimiter=";")
        for line in r:
            self.__csv_list.append(line)
        self.__arq.close()
        return self.__csv_list


    def csvPd(self):
        self.__arq = pd.read_csv("/Users/ramon/Documents/Dados/aluguel.csv", sep=";")
        return self.__arq


if(__name__ == "__main__"):
    print("classe escolheFrame")
    _a=escolheFrame("ramon_testando")
    print(_a)
    print(_a.frame)
    
    print("classe leituraArquivoCsv")
    _b = leituraArquivoCsv()
    print(_b.csvPy())
    print(_b.csvPd())

