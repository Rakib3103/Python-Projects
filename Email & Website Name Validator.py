# -*- coding: utf-8 -*-
"""20101408_05_Mazharul Islam Rakib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P1Gum7chWEokhjr0z61P1MlfXLV9DnDJ
"""

# TAKING INPUT FROM FILE
input_file = open('inp_lab2.txt')
a = input_file.read()
sample_input = a.split('\n')

#print(sample_input)
email = sample_input[1]
web = sample_input[2]
###################################### CHECKING EMAIL ####################################################
def check_email(email):
    k,j,d = 0,0,0
    if len(email)>=6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@')==1): 
                if (email[-4] == '.') ^ (email[-3] == '.'): 
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == '_' or i == '.' or i == '@':
                            continue
                        else:
                            d = 1
                    print('Email',',',sample_input.index(email))
########################## ALL INVALID CONDITIONS ########################################################
                    if k == 1 or j == 1 or d == 1:
                        print('Invalid5')
                else:
                    print('Invalid4')
            else:
                print('Invalid3')
        else:
            print('Invalid2')
    else:
        print('Invalid1')
#email = str(input())
check_email(email)

######################################## CHECKING WEB ######################################################
def check_web(web):
    #x = web.split('.')
    l,m,n= 0,0,0
    if len(web)>=3:
        if web.startswith("www."):
            if web[-1].isalpha() == True:
                for i in web:
                    if i == i.isdigit():
                        l = 1
                    elif i == i.isspace():
                        m = 1
                    elif i == i.upper():
                        continue
                    elif ('.' in web) and (web.count('.')<=5):
                        continue
                    else:
                        n = 1
                print('Web',',',sample_input.index(web))
##################### ALL INVALID CONTITIONS ###############################################################
                if l == 1 or m == 1:
                    print('invalid4')
            else:
                print('invalid3')
        else:
            print('invalid2')
    else:
        print('invalid1')
#web = str(input())
check_web(web)