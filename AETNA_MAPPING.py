# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:29:26 2018

@author: YiLuo
"""


import pandas as pd
import pyautogui as pya
import time
import pyperclip

df = pd.read_csv("C:/Users/YiLuo/Documents/Python Scripts/FSAPAetna08162.csv", encoding = "ISO-8859-1")
df.head()

Planid=[]
for i in range(0, len(df["Account Name"])):
    if df["Account Name"][i] == "FSAP - PPO TRADITIONAL PLAN ACTIVE":
        Planid.append("31048")
    elif df["Account Name"][i] == "PETA - PPO TRADITIONAL PLAN ACTIVE":
        Planid.append("31023")
    elif df["Account Name"][i] == "BLANK - PPO TRADITIONAL PLAN ACTIVE":
        Planid.append("31023")
    elif df["Account Name"][i] == "HYBRID HRA - FSAP PPO STANDARD HRA PLAN ACTIVE":
        Planid.append("31047")
    elif df["Account Name"][i] == "HYBRID HRA - PETA PPO STANDARD HRA PLAN ACTIVE":
        Planid.append("31022")
    elif df["Account Name"][i] == "HYBRID HRA - BLANK PPO STANDARD HRA PLAN ACTIVE":
        Planid.append("31022")
    elif df["Account Name"][i] == "FSAP - PPO SAVINGS PLAN ACTIVE":
        Planid.append("31046")
    elif df["Account Name"][i] == "PETA - PPO SAVINGS PLAN ACTIVE":
        Planid.append("31021")
    elif df["Account Name"][i] == "BLANK - PPO SAVINGS PLAN ACTIVE":
        Planid.append("31021")
    elif df["Account Name"][i] == "FSAP - PPO STANDARD DENTAL ACTIVE":
        Planid.append("31050")
    elif df["Account Name"][i] == "PETA - PPO STANDARD DENTAL ACTIVE":
        Planid.append("31024")
    elif df["Account Name"][i] == "BLANK - PPO STANDARD DENTAL ACTIVE":
        Planid.append("31024")
    elif df["Account Name"][i] == "FSAP - PPO ORTHODONTIA DENTAL ACTIVE":
        Planid.append("31051")
    elif df["Account Name"][i] == "PETA - PPO ORTHODONTIA DENTAL ACTIVE":
        Planid.append("31025")
    elif df["Account Name"][i] == "BLANK - PPO ORTHODONTIA DENTAL ACTIVE":
        Planid.append("31025")
    elif df["Account Name"][i] == "FSAP - AETNA VISION PREFERRED ACTIVE":
        Planid.append("31052")
    elif df["Account Name"][i] == "PETA- AETNA VISION PREFERRED ACTIVE":
        Planid.append("31026")
    elif df["Account Name"][i] == "BLANK - AETNA VISION PREFERRED ACTIVE":
        Planid.append("31026")
    else:
        Planid.append("missing")
print(Planid)
len(Planid)


## be careful. state name may be misspelled Oregan-Organ-Oregon, Arizona-Airzona, District-Distric
State=[]
for i in range(0, len(df["Description"])):
    if "VIRGINIA" in df["Description"][i]:
        State.append("VA")
    elif "ALASKA" in df["Description"][i]:
        State.append("AK")
    elif "ARIZONA" in df["Description"][i]:
        State.append("AZ")
    elif "AIRZONA" in df["Description"][i]:
        State.append("AZ")
    elif "CALIFORNIA" in df["Description"][i]:
        State.append("CA")
    elif "COLORADO" in df["Description"][i]:
        State.append("CO")
    elif "CONNECTICUT" in df["Description"][i]:
        State.append("CT")
    elif "DISTRIC OF COLUMBIA" in df["Description"][i]:
        State.append("DC")
    elif "DISTRICT OF COLUMBIA" in df["Description"][i]:
        State.append("DC")
    elif "FLORIDA" in df["Description"][i]:
        State.append("FL")
    elif "GEORGIA" in df["Description"][i]:
        State.append("GA")
    elif "ILLINOIS" in df["Description"][i]:
        State.append("IL")
    elif "KANSAS" in df["Description"][i]:
        State.append("KS")
    elif "MARYLAND" in df["Description"][i]:
        State.append("MD")
    elif "MASSACHUSETTS" in df["Description"][i]:
        State.append("MA")
    elif "MICHIGAN" in df["Description"][i]:
        State.append("MI")
    elif "MISSOURI" in df["Description"][i]:
        State.append("MO")
    elif "NEW HAMPSHIRE" in df["Description"][i]:
        State.append("NH")
    elif "NEW JERSEY" in df["Description"][i]:
        State.append("NJ")
    elif "NEW MEXICO" in df["Description"][i]:
        State.append("NM")
    elif "NEW YORK" in df["Description"][i]:
        State.append("NY")
    elif "NORTH CAROLINA" in df["Description"][i]:
        State.append("NC")
    elif "OHIO" in df["Description"][i]:
        State.append("OH")
    elif "OREGON" in df["Description"][i]:
        State.append("OR")
    elif "ORGAN" in df["Description"][i]:
        State.append("OR")
    elif "OREGAN" in df["Description"][i]:
        State.append("OR")
    elif "PENNSYLVANIA" in df["Description"][i]:
        State.append("PA")
    elif "SOUTH CAROLINA" in df["Description"][i]:
        State.append("SC")
    elif "TENNESSEE" in df["Description"][i]:
        State.append("TN")
    elif "TEXAS" in df["Description"][i]:
        State.append("TX")
    elif "UTAH" in df["Description"][i]:
        State.append("UT")
    elif "VERMONT" in df["Description"][i]:
        State.append("VT")
    elif "WASHINGTON" in df["Description"][i]:
        State.append("WA")
    elif "IOWA" in df["Description"][i]:
        State.append("IA")
    elif "WEST VIRGINIA" in df["Description"][i]:
        State.append("WV")
    elif "LOUISIANA" in df["Description"][i]:
        State.append("LA")
    elif "NEVADA" in df["Description"][i]:
        State.append("NV")
    elif "WISCONSIN" in df["Description"][i]:
        State.append("WI")
    elif "HAWAII" in df["Description"][i]:
        State.append("HI")
    else:
        State.append("missing")
print(State)
len(State)


## Check which state is missing
for j in range(0, len(State)):
    if State[j] == "missing":
        print(j)
        print(df["Description"][j])
        
        
Planlevel=[]
for k in range(0, len(df["Description"])):
    if "EMPLOYEES ONLY" in df["Description"][k]:
        Planlevel.append('"EE"')
    elif "EMPLOYEES AND DEPENDENTS" in df["Description"][k]:
        Planlevel.append('"EECC", "EED", "EEDCC", "EEDDPCC", "EES", "EESCC"')
    else:
        Planlevel.append("missing")
print(Planlevel)
len(Planlevel)

from collections import Counter
Counter(Planlevel)

dffinal =pd.DataFrame({'PlanCode': df['HD04'], 'SubsidiaryId': Planid, 'State Abbr': State, 'PlanLevel': Planlevel})

dfexample = dffinal.head()


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

