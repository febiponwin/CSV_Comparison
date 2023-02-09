import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import simpledialog
import sys
import webbrowser

ROOT = tk.Tk()
ROOT.withdraw()
USER_1 = simpledialog.askstring(title="CSV Comparison",
                                  prompt="First folder location")
USER_2 = simpledialog.askstring(title="CSV Comparison",
                                  prompt="Second folder location")
if USER_1 == "":
    USER_1 = None
if USER_2 == "":
    USER_2 = None

if (USER_1 is None) or (USER_2 is None):
    sys.exit("No input is given")

folder1 = USER_1
folder2 = USER_2
file1 = os.listdir(folder1)
file2 = os.listdir(folder2)

# Finding common files
common_files = []
missing_files_a = []
missing_files_b = []
for x in file1:
    if x in file2:
        common_files.append(x)
    else:
        missing_files_a.append(x)
for x in file2:
    if x not in file1:
        missing_files_b.append(x)

list1 = []

for y in common_files:
    value1 = ""
    # print (y)
    firstProductSet = pd.read_csv(folder1+'\\'+y)
    df1 = pd.DataFrame(firstProductSet)


    secondProductSet = pd.read_csv(folder2+'\\'+y)
    df2 = pd.DataFrame(secondProductSet)
    df = pd.DataFrame()

    for i in firstProductSet.columns.tolist():
        df[i+'Match?'] = np.where(df1[i] == df2[i], 'True', 'False')
    value1= y
    for i in firstProductSet.columns.tolist():
        if not df[df[i+'Match?'] == 'False'].index.values.tolist():
            continue
        else:
            value1 = value1+','+"Column_Name-"+i+','
            value1 = value1+''.join(str(df[df[i + 'Match?'] == 'False'].index.values.tolist())).replace(",",";")
    list1.append(value1)
#printing the report
html_head = "<html><head><H1>CSV Comparison</head><body><table border=1 ><tr><td>File Name</td><td>Failure Result</td></tr>"
html_str = ""
for n in list1:
    html_str = html_str+"<tr>"
    html_str1 = ""
    for j in n.split(','):
        html_str1 = html_str1 + "<td>"+j+"</td>"
    html_str = html_str+html_str1+"</tr>"

html_end = "</table></body></html>"

Html_file= open("report.html","w")
Html_file.write(html_head+html_str+html_end)
Html_file.close()

url = 'file:///'+os.getcwd()+'/report.html'
webbrowser.open(url, new=2)
