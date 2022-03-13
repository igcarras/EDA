#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:18:16 2020

@author: isegura
"""

from fase1solOn import HealthCenter
from fase1solOn import Patient

import unittest

class Test(unittest.TestCase):

    mark=0


    def setUp(self):
        pass

    
    def test1_addPatient(self):
        print('\tCase1 addPatient: insert at the beginning')
        
        expected=HealthCenter('data/LosFrailes1.tsv')

        result=HealthCenter('data/LosFrailes.tsv')


        objP=Patient('Abad, Abel',1950,0,1)
        result.addPatient(objP)
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
            
            
        print('\tCase1 addPatientOK\n')

        Test.mark+=0.25
        
    
    def test2_addPatient(self):
        print('\tCase2 addPatient: insert at the END')
        
        expected=HealthCenter('data/LosFrailesLast.tsv')

        result=HealthCenter('data/LosFrailes.tsv')
        objP=Patient('Zen, Chen',1995,1,0)
        result.addPatient(objP)
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase2 addPatient: OK\n')
        Test.mark+=0.25
 
    
    def test3_addPatient(self):
        print('\tCase3 addPatient: try add a patient who already exists')
        
        expected=HealthCenter('data/LosFrailes.tsv')

        result=HealthCenter('data/LosFrailes.tsv')
        objP=Patient('Hoz, Mario',1928,1,0)
        result.addPatient(objP)
        
          
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase3 addPatient OK\n')
        Test.mark+=0.25


    def test4_addPatient(self):
        print('\tCase4 addPatient: add a patient')
        
        expected=HealthCenter('data/LosFrailesMiddle.tsv')
        #Quirante, Pepe	1985	0	0

        result=HealthCenter('data/LosFrailes.tsv')

        objP=Patient('Quirante, Pepe',1985,0,0)
        result.addPatient(objP)
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase4 addPatient OK\n')
        Test.mark+=0.5


    def test5_searchPatients(self):
        print('\tCase5 searchPatients: allpatients')
        
        input=HealthCenter('data/LosFrailes.tsv')
        expected=HealthCenter('data/LosFrailes.tsv')

        result=input.searchPatients(2021,None,None)
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase5 searchPatients OK\n')
        Test.mark+=0.25

        
    def test6_searchPatients(self):
        print('\tCase 6 searchPatients: all patients who were born in or before 1950.')
        
        input=HealthCenter('data/LosFrailes.tsv')
        result=input.searchPatients(1950,None,None)
        expected=HealthCenter('data/LosFrailes1950.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 6 searchPatients: OK\n')
        Test.mark+=0.25

        
    def test7_searchPatients(self):
        print('\tCase 7 searchPatients: all patients who have had covid \n')
        
        input=HealthCenter('data/LosFrailes.tsv')

        result=input.searchPatients(2021,True,None)
        expected=HealthCenter('data/LosFrailesCovid.tsv')
        
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print()
        Test.mark+=0.25
    
    def test8_searchPatients(self):
        print('\tCase 8 searchPatients: all patients who were born in or before than 1925 and have had covid.')
        
        input=HealthCenter('data/LosFrailes.tsv')

        result=input.searchPatients(1950,True,None)
        expected=HealthCenter('data/LosFrailes1950Covid.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 8 searchPatients OK \n')
        Test.mark+=0.25

    def test9_searchPatients(self):
        print('\tCase 9 searchPatients: all patients who have had covid and have been vaccined only with the first dosage.')
        
        input=HealthCenter('data/LosFrailes.tsv')

        result=input.searchPatients(2021,True,1)
        expected=HealthCenter('data/LosFrailesCovid1.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 9 searchPatients OK \n')
        Test.mark+=0.25


    def test_10_searchPatients(self):
        print('\tCase 10 searchPatients: all patients who have already received the two dosages of the vaccine.')
        
        input=HealthCenter('data/LosFrailes.tsv')

        result=input.searchPatients(2021,None,2)
        expected=HealthCenter('data/LosFrailesVaccined2.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 10 searchPatients: OK\n')
        Test.mark+=0.25

        
    def test_11_searchPatients(self):
        print('\tCase 11 searchPatients: all patients who have received the two dosages and were born in or before than 1945.')
        
        input=HealthCenter('data/LosFrailes.tsv')

        result=input.searchPatients(1945,None,2)
        
        expected=HealthCenter('data/LosFrailes1945Vaccined2.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 11 searchPatients: OK\n')
        
        Test.mark+=0.25

        
    def test_12_statistics(self):
        print('\tCase 12 statistics\n')
        
        input=HealthCenter('data/LosFrailes.tsv')

        (numcovid,numcovid1950,novaccine,novaccine1950,numvaccine1,numvaccine2) =input.statistics()
        
        #self.assertEqual(numcovid,0.65,'FAIL: #Percentage of patients who have already had covid.')
        self.assertEqual(numcovid,0.71,'FAIL: #Percentage of patients who have already had covid.')

        #self.assertEqual(numcovid1950,0.38,'FAIL: #Percentage of patients born in or before than 1950, who have had covid.')
        self.assertEqual(numcovid1950,0.67,'FAIL: #Percentage of patients born in or before than 1950, who have had covid.')
        
        #self.assertEqual(novaccine,0.57,'FAIL: #Percentage of patients who have not been vaccined with any dosage of the vaccine.')
        self.assertEqual(novaccine,0.42,'FAIL: #Percentage of patients who have not been vaccined with any dosage of the vaccine.')
        
        #self.assertEqual(novaccine1950,0.23,'FAIL: #Percentage of patients born in or before than 1950, who have not been vaccined with any dosage.')
        self.assertEqual(novaccine1950,0.11,'FAIL: #Percentage of patients born in or before than 1950, who have not been vaccined with any dosage.')
        
        #self.assertEqual(numvaccine1,0.13,'FAIL: #Percentage of patients who have already received the first dosage.')
        self.assertEqual(numvaccine1,0.12,'FAIL: #Percentage of patients who have already received the first dosage.')

        #self.assertEqual(numvaccine2,0.3,'FAIL: #Percentage of patients who have already received the two dosages.')
        self.assertEqual(numvaccine2,0.46,'FAIL: #Percentage of patients who have already received the two dosages.')

        Test.mark+=0.5

    def test_13_merge(self):
        print('\tCase 13 merge.')
        
        input1=HealthCenter('data/LosFrailes.tsv')
        input2=HealthCenter('data/Libertad.tsv')

        result=input1.merge(input2)
        expected=HealthCenter('data/LosFrailes+Libertad.tsv')
    
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 13 merge: OK\n')

        Test.mark+=3
        
    def test_14_minus(self):
        print('\tCase 14 minus.')
        
        input1=HealthCenter('data/LosFrailes.tsv')
        input2=HealthCenter('data/LosFrailesVaccined2.tsv')


        result=input1.minus(input2)

        
        expected=HealthCenter('data/LosFrailes-LosFrailesVaccined2.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
              self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 14 minus: OK\n')
        
        Test.mark+=1.75

        
    def test_15_inter(self):
        print('\tCase 15 inter.')
        
        input1=HealthCenter('data/LosFrailes.tsv')
        input2=HealthCenter('data/LosFrailes3.tsv')


        result=input1.inter(input2)
        
        
        expected=HealthCenter('data/LosFrailesyLosFrailes3.tsv')
        
        self.assertEqual(len(result),len(expected),'FAIL: lenghts are different')
        for i in range(len(result)):
              self.assertEqual(result.getAt(i).name,expected.getAt(i).name,'FAIL: patients are not equal')
        print('\tCase 15 inter\n')
        
        Test.mark+=1.75

    def test_showmark(self):
        print('Total mark is ', Test.mark)
    
#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()