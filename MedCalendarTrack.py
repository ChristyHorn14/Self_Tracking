#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:04:07 2020

@author: chrishornung
"""

# MedCalendarTrack.py
# program that asks for two CSV files, one for reading, the other for writing.
# CSV files from IFTTT output to Google sheets for event tracking in gMail
# make sure the fields of the read CSV matches the code

import datetime
import csv

# function to convert the time in Google sheet to minutes
# ex in April 23, 2020 at 04:00PM out 960

def converttime(string):
    
    #convert string to standard format
    FullDate = datetime.datetime.strptime(string, "%B %d, %Y at %I:%M%p")
    print(FullDate)
    
    #convert variable to string
    FullDate = str(FullDate)
    
    #slice out time
    time = FullDate[11:16]
    print(time)
    
    #convert time to minutes
    hr = int(time[0:2])
    print(hr)
    mins = int(time[3:5])
    print(mins)
    minutes = hr * 60 + mins
    print(minutes)
    return minutes

# function to convert date from sheet to diffferent format
# ex in  April 23, 2020 at 03:00PM, out 2020-04-23
def convertdate(string):
    
    #convert string to standard format
    FullDate = datetime.datetime.strptime(string, "%B %d, %Y at %I:%M%p")
    print(FullDate)
    
    #convert variable to string
    FullDate = str(FullDate)
    
    #slice out date
    date = FullDate[0:10]
    print(date)
    return date
    
#function to write in day of week into new csv file
# ex in 2020-23-04 out Thursday
def MedConvertDayWeek(string):
    #convert string to standard format
    FullDate = datetime.datetime.strptime(string, "%Y-%m-%d")
    print(FullDate)
    
    DayWeek = FullDate.strftime("%A")
    print(DayWeek)
    
    return DayWeek


def ReadWrite(oldfile,newfile):
    #get string
    
    with open(oldfile,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        #required fieldnames (header cells) in row 1 of csv file
        with open(newfile,'w') as new_file:
            fieldnames = ['Title', 'Description', 'Location', 'Start', 'End',
                          'Date', 'Duration_minutes','Day_week']
            
            csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
            
            #write fieldnames of new csv file
            csv_writer.writeheader()
            
        
            for line in csv_reader:
                title = line['Title']
                des = line['Description']
                loc = line['Location']
                start = line['Start']
                end = line['End']
                date = convertdate(end)
                end1 = converttime(end)
                start1 = converttime(start)
                #calculates duration from time between start and end time
                duration = end1 - start1
                print(duration)
                dayweek = MedConvertDayWeek(date)
                csv_writer.writerow({'Title': title, 'Description':des,
                                     'Location':loc, 'Start':start,'End':end,
                                     'Date' : date, 'Duration_minutes' : duration,
                                     'Day_week': dayweek})
                
def main():
    #use testdata1.csv
    oldfile = str(input("Input csv file name you would like to get data from >> "))
    #us new_testdata1.csv
    newfile = str(input("Input csv file name you would like to write data to >> "))
    
    ReadWrite(oldfile,newfile)
    
    print("\n\n\nRead, processed and transferred date from", oldfile, "to", newfile,
          "happy tracking!")
    
main()