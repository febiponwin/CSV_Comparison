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


import tkinter as tk
from datetime import datetime

def update_range(val):
    # Get the selected range
    start = times[int(val)]
    end = times[int(val) + slider_length.get()]
    print(f"Selected range: {start} - {end}")
    start_label.config(text=start.strftime('%Y-%m-%d %H:%M:%S'))
    end_label.config(text=end.strftime('%Y-%m-%d %H:%M:%S'))

# Load the time values from the file into a list
with open("times.txt", "r") as f:
    times = [datetime.strptime(line.strip(), '%Y-%m-%dT%H:%M:%S') for line in f.readlines()]

root = tk.Tk()
root.title("Time Slider")

# Create a variable to store the length of the range
slider_length = tk.IntVar()
slider_length.set(1)

# Create the time slider
time_slider = tk.Scale(root, from_=0, to=len(times) - slider_length.get() - 1, orient="horizontal", label="Time", command=update_range, showvalue=False)
time_slider.pack()

# Create labels to display the start and end times
start_label = tk.Label(root, text=times[0].strftime('%Y-%m-%d %H:%M:%S'))
start_label.pack()
end_label = tk.Label(root, text=times[slider_length.get()].strftime('%Y-%m-%d %H:%M:%S'))
end_label.pack()

# Create a scale to select the range length
length_slider = tk.Scale(root, from_=1, to=len(times), orient="horizontal", label="Range Length", command=lambda x: time_slider.config(to=len(times) - int(x) - 1), variable=slider_length)
length_slider.pack()

root.mainloop()
