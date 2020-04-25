#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:40:28 2020

@author: chrishornung
"""

#RescueTimeReadProcess.py

# program to read data from Rescue Time Data in Google sheets exported as CSV
# process the data and convert to total minutes/day
# write the new data into a new file
# Make sure CSV file is located in RescueTime Folder within Tracking Folder
# program works as long as an input is not none or in format 1m 52s

import csv
import datetime

def RescueTimeConvert(string):
    #convert string to standard format
    #condition for if string is in format ex. 5h 5m output 305
    if string.__contains__('h') == True:
        Fulltime = str(datetime.datetime.strptime(string, "%Hh %Mm"))
        time = Fulltime[11:16]
        hr = int(time[0:2])
        mins = int(time[3:5])
        total_minutes = hr * 60 + mins
        return(total_minutes)
    #conditions if string contains seconds (5m 5s or 5s)
    elif string.__contains__('s') == True:
            #condition if string is in format 5m 5s

        if string.__contains__('m') == True:
            Fulltime = str(datetime.datetime.strptime(string, "%Mm %Ss"))
            time = Fulltime[11:16]
            mins = int(time[3:5])
            return mins
    #condition if string is in format 5s
        else:
            return 0
    # condition if string is "no time"
    else:
        return 0
    
    
#fucntion to allow day f week to be written in new sheet
# ex 24-Apr-20 outputs Friday
def MedConvertDayWeek(string):
    #convert string to standard format
    FullDate = datetime.datetime.strptime(string, "%d-%b-%y")
    
    DayWeek = FullDate.strftime("%A")
    
    return DayWeek

def ReadWrite(oldfile,newfile):    
    with open(oldfile,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with open(newfile,'w') as new_file:
            fieldnames = ['Date', 'TotalTime','AllProductiveTime',	'AllDistractingTime',
                          'VeryProductiveTime', 'ProductiveTime', 'NeutralTime',
                          'DistractingTime', 'VeryDistractingTime', 'BusinessTime',
                          'CommunicationAndSchedulingTime', 'SocialNetworkingTime',
                          'DesignAndCompositionTime', 'EntertainmentTime', 'NewsTime',
                          'SoftwareDevelopmentTime','ReferenceAndLearningTime',
                          'ShoppingTime','UtilitiesTime','Day_week']
            
            csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
            
            csv_writer.writeheader()
            
        
            for line in csv_reader:
                date = line['Date']
                ttime = RescueTimeConvert(line['TotalTime'])
                apt = RescueTimeConvert(line['AllProductiveTime'])
                adt = RescueTimeConvert(line['AllDistractingTime'])
                vpt = RescueTimeConvert(line['VeryProductiveTime'])
                pt = RescueTimeConvert(line['ProductiveTime'])
                nt = RescueTimeConvert(line['NeutralTime'])
                dt = RescueTimeConvert(line['DistractingTime'])
                vdt = RescueTimeConvert(line['VeryDistractingTime'])
                bt = RescueTimeConvert(line['BusinessTime'])
                cst = RescueTimeConvert(line['CommunicationAndSchedulingTime'])
                snt = RescueTimeConvert(line['SocialNetworkingTime'])
                dct = RescueTimeConvert(line['DesignAndCompositionTime'])
                et = RescueTimeConvert(line['EntertainmentTime'])
                news = RescueTimeConvert(line['NewsTime'])
                sdt = RescueTimeConvert(line['SoftwareDevelopmentTime'])
                rlt = RescueTimeConvert(line['ReferenceAndLearningTime'])
                st = RescueTimeConvert(line['ShoppingTime'])
                ut = RescueTimeConvert(line['UtilitiesTime'])
                dayweek = MedConvertDayWeek(date)
                
                csv_writer.writerow({'Date': date,
                                     'TotalTime':ttime,
                                     'AllProductiveTime':apt,
                                     'AllDistractingTime':adt,
                                     'VeryProductiveTime':vpt,
                                     'ProductiveTime':pt,
                                     'NeutralTime':nt,
                                     'DistractingTime':dt,
                                     'VeryDistractingTime':vdt,
                                     'BusinessTime':bt,
                                     'CommunicationAndSchedulingTime':cst,
                                     'SocialNetworkingTime':snt,
                                     'DesignAndCompositionTime':dct,
                                     'EntertainmentTime':et,
                                     'NewsTime':news,
                                     'SoftwareDevelopmentTime':sdt,
                                     'ReferenceAndLearningTime':rlt,
                                     'ShoppingTime':st,
                                     'UtilitiesTime':ut,
                                     'Day_week':dayweek})
    
def main():
    #input old csv file name
    oldfile = str(input("Input the csv file name you want to read from >> "))
    #input file name you would like to write into
    newfile = str(input("Input the csv file name you want to write to >> "))
    
    ReadWrite(oldfile,newfile)
    
    print("\n\nDone reading, processing, and writing data from", oldfile, "to",
          newfile, "\n\nHappy Tracking!")
    
    
main()
    
    

    
    
    
    
    
    