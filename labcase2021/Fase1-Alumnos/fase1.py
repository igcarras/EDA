# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from dlist import DList
from dlist import DNode

import csv
import os.path

class Patient:
    """Class to represent a Patient"""
    def __init__(self,name,year,covid,vaccine):
        self.name=name
        self.year=year
        self.covid=covid
        self.vaccine=vaccine
        
    def __str__(self):
        return self.name+'\t'+str(self.year)+'\t'+str(self.covid)+'\t'+str(self.vaccine)


class HealthCenter(DList):
    """Class to represent a Health Center"""
    def __init__(self,filetsv=None):
        super(HealthCenter, self).__init__()

        if filetsv is None or not os.path.isfile(filetsv):
            self.name=''

        else: 
            print('loadimg the data for the health center from the file ',filetsv)
    
            self.name=filetsv.replace('.tsv','')
            tsv_file = open(filetsv)
            read_tsv = csv.reader(tsv_file, delimiter="\t")
    
    
            for row in read_tsv:
                name=row[0]
                year=int(row[1])
                covid=False
                
                if int(row[2])==1:
                    covid=True

                vaccine=int(row[3])
                self.addLast(Patient(name,year,covid,vaccine))
                
    
    def addPatient(self,patient):
        "add a new patient in alphabetic order"
        ...
                

        
        
    def searchPatients(self,year,covid=None,vaccine=None):
       ...
    
    def statistics(self):
        ...

    def merge(self,other):
       ...
    
    
    def minus(self,other):
       ...
    
    def inter(self,other):
        ...
                
    
     
if __name__ == '__main__':
    gst=HealthCenter('data/LosFrailes.tsv')
    print(gst)
    
    #Puedes añadir más llamadas a funciones para probarlas
    