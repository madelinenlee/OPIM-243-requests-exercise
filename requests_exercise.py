#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:26:48 2019

@author: madeline
"""

import requests
import json
#from bs4 import BeautifulSoup

#challenge 1
request_url_1 = 'https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products/1.json'
response_1 = requests.get(request_url_1)

parse_1 = json.loads(response_1.text)
print(parse_1['name'])

#challenge 2
request_url_2 = 'https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products.json'
response_2 = requests.get(request_url_2)
parse_2 = json.loads(response_2.text)

print('name: ID')
for i in range(0, len(parse_2)):
    print(parse_2[i]['name'] + ': ' + str(parse_2[i]['id']))
    
#challenge 3
request_url_3 = 'https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json'
response_3 = requests.get(request_url_3)
parse_3 = json.loads(response_3.text)
student_list = parse_3['students']

min_grade = 100
max_grade = 0
avg = 0

for i in range(0, len(student_list)):
    #print(student_list[i]['finalGrade'])
    
    if student_list[i]['finalGrade'] < min_grade :
        min_grade = student_list[i]['finalGrade']
        
    if student_list[i]['finalGrade'] > max_grade:
        max_grade = student_list[i]['finalGrade']
    avg = avg + student_list[i]['finalGrade']

print('min grade: ' + str(min_grade) + '%')
print('max grade: ' + str(max_grade)+ '%')
print('average grade: ' + str(round(avg/len(student_list), 2))+ '%')