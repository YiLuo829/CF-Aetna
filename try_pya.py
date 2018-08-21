# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:20:28 2018

@author: YiLuo
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pyautogui as pya
import time
import pyperclip


df = pd.read_excel('C:/Users/YiLuo/Documents/Python Scripts/0821_FSAP_Aetna_Matching.xlsx', 0) #second sheet, first column

dfexample = df.head()


plancodelist = dfexample["PlanCode"].tolist()
subsiidlist = dfexample["SubsidiaryId"].tolist()
statelist = dfexample["State Abbr"].tolist()
planlevellist = dfexample["PlanLevel"].tolist()
print("first column contains: " + str(len(plancodelist)) + " cells.")
print("second column contains: " + str(len(subsiidlist)) + " cells.")
print("third column contains: " + str(len(statelist)) + " cells.")
print("fourth column contains: " + str(len(planlevellist)) + " cells.")
if (len(plancodelist) != len(subsiidlist) != len(statelist) != len(planlevellist) ):
    print("WARNING: column lengths do not match! ")

for CODE in plancodelist:
    pya.click(pya.position())
    
for x in range(3): 
    pya.press('tab')

for CODE in plancodelist: # loops through dflist and populates conditionals according to code
	
	#pya.typewrite( "{{SubsidiaryPlanId}} = " )

	pyperclip.copy("{{SubsidiaryPlanId}} = ")  #copies code into clipboard
	pya.hotkey('ctrl', 'v') # pastes the code 

	pya.press('tab')

	pyperclip.copy('"' + CODE + '"') #
	pya.hotkey('ctrl', 'v')
	#pya.typewrite('"' + CODE + '"')

	if CODE != plancodelist[len(plancodelist)-1]: #if it's not the last code, navigate down to the next conditional
		for x in range(3): pya.press('tab')
            
print("Navigate to first if statement, you have 5 seconds")
time.sleep(10)





#################################

for a in range(0, len(plancodelist)):
    pya.click(pya.position())
    
for x in range(3): 
    pya.press('tab')
    
for i in range(0, len(plancodelist)): # loops through dflist and populates conditionals according to code

    pyperclip.copy("{{SubsidiaryPlanId}} = " + str(subsiidlist[i]) + "AND {{Parent_State}} IN " + statelist[i] )  #copies code into clipboard
    pya.hotkey('ctrl', 'v') # pastes the code 
    
    pya.press('tab')

    pyperclip.copy('"' + plancodelist[i] + '"') #
    pya.hotkey('ctrl', 'v')
	

    if CODE != plancodelist[len(plancodelist)-1]: #if it's not the last code, navigate down to the next conditional
        for x in range(3): pya.press('tab')
            
print("Navigate to first if statement, you have 5 seconds")
time.sleep(10)