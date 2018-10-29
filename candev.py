#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Packages needed:
python3 -m pip install csv pyenchant numpy
'''
import os,re,sys,time
import math,random
import csv,re,enchant
import numpy as np
import ntpath


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#sys.stdin=open('in.txt','r')


def getkeyword():
    if len(sys.argv)<=1:
        return 'OHIDataSet.csv'
    tmp = sys.argv[1]
    for i in range(2,len(sys.argv)):
        tmp+=' '+sys.argv[i]
    print('Key word is \"%s\"'%(tmp))
    return tmp

file_path = getkeyword()
checklist_path = './DataChecklistModules.csv'
checklist_header = []
checklist_data = {}
header = []
data = []
Answer = ['yes','no','not applicable','I don\'t know']
threshold = 60.0

finished_modules = [ '2b_%d'%i for i in range(1,20) ] + \
                    []
results_according_to_modules = []

def load_dataset(f = file_path):
    global header,data, checklist_header, checklist_data
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)[:-1]
        for row in reader:
            data.append(row[:-1])
    print(header)
    print('Total lines in this dataset:', len(data))
    print('A sample line:', data[-1])
    pass
    with open(checklist_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        checklist_header = next(reader)
        for row in reader:
            checklist_data[row[0].replace('-','_')] = row[1:]
    print(checklist_header)
    print('Total lines in this checklist:', len(checklist_data))
    print('A sample line:', checklist_data['9a_15'])



def name_split(s):
    '''
    Split a string by: All possible delimiters; Uppercases; Numbers
    '''
    words = re.findall(r"[A-Za-z0-9']+", s)
    tmp = []
    for i in words:
        tmp += re.sub( r"([A-Z])", r" \1", i).split()
    ret = []
    for i in tmp:
        ret += re.findall('\d+|\D+', i)
    return ret




def _2b_1():
    '''
    2. valuable
    In the case of self-describing digital datasets, is the format either JSON (preferred) or XML-based using a well-known schema (or accompanied by the schema employed)?
    '''
    ans, reason = 1,''
    with open(file_path, 'r') as unknown_file:
        # Remove tabs, spaces, and new lines when reading
        data = re.sub(r'\s+', '', unknown_file.read())
        if (re.match(r'^<.+>$', data)):
            ans,reason = 0, 'This file is XML'
        if (re.match(r'^({|[).+(}|])$', data)):
            ans, reason = 0, 'This file is JSON'
        ans, reason = 1, 'This file is either not XML nor JSON'
    return Answer[ans], reason


def _2b_2():
    '''
    2. valuable
    In the case where the data reside in a relational database, is the database in 3rd normal form?
    '''
    ans, reason = 2,'It is not a database file'
    return Answer[ans], reason


def _2b_3():
    '''
    1. essential
    In the case where the data do not reside in a relational database, are the data files tabular?
    i.e. There is one rectangular table per file, systematically arranged in rows and columns with the headers (column names) in the 1st row.
    Every record (row) has the same column name. Every column contains the same type of data, and only one type of data.
    How: Check the csv file has a header by using has_header from csv package; By checking the number of columns for each row is equal to the column numbers for header;
         By checking the data type of every unit in every row
    '''
    ans, reason = 1, ''
    with open(file_path, 'r') as unknown_file:
        sniffer = csv.Sniffer()
        has_header = sniffer.has_header(unknown_file.read(2048))
        unknown_file.seek(0)

        has_rowcols = False
        reader = csv.reader(unknown_file, delimiter=',')
        num_cols = len(next(reader))

        for row in data:
            if num_cols != len(row):
                has_rowcols = True
                break

        All = all(isinstance(column, (int, str, float)) for column in unknown_file)

        if (has_header == True & has_rowcols == True & All == True):
            ans, reason = 0, 'This data file is tabular.'
        else:
            ans, reason = 1, 'This data is not tabular.'

    return Answer[ans], reason


def _2b_4():
    '''
    1. essential
    Are the field types (column types) used appropriate? (i.e. date field for dates, alphanumeric field for text, numerical field for numbers, etc)
    '''
    ans, reason = 2,'.csv file does not indicate data type.'
    return Answer[ans], reason


def _2b_5():
    '''
    2. valuable
    Was a logical, documented naming convention used for variables (column names)?
    Split the name into letters and numbers. Check if all words appears in the dictionary
    '''
    ans, reason = 1,''
    d = enchant.Dict("en_US")
    warning_column_names = []
    for col in header:
        words = name_split(col)
        if not all(d.check(i) for i in words):
            warning_column_names.append(col)
    if len(warning_column_names)==0:
        ans = 0
    else:
        ans = 1
        reason = '%s columns may not have logical, documented naming convention'%warning_column_names
    return Answer[ans], reason


def _2b_6():
    '''
    0.Yes 1.No
    make sure the header is in the first line.

    '''
    ans, reason = 1,'The header is in line '
    metadata=['scenario', 'goals', 'long_goal', 'dimension', 'region_id', 'region_name', 'value']
    if(metadata==header):
        ans=0
        reason = 'The header is in the first line'
    else:
        ans=1
        for index,i in enumerate(data):
            if i==metadata:
                reason += str(index)

    return Answer[ans], reason


def _2b_7():
    '''
    3. I don\'t know
    '''
    ans, reason = 3,''
    #Your code here

    return Answer[ans], reason


def _2b_8():
    '''
    0.Yes 1.No
    get the extension from the path. if it's .csv, then it can be understand easily both by humans and machines.
    '''
    ans, reason = 1,''
    extension = os.path.splitext(file_path)[1]
    if extension == '.csv':
        ans = 0
        reason = 'this is a .csv'
    else:
        reason ='because this is a '+ extension
    return Answer[ans], reason


def _2b_9():
    '''
    2.not applicable 3. I don\'t know
    '''
    ans, reason = 3,''
    #Your code here

    return Answer[ans], reason


def _2b_10():
    '''
    0.Yes 1.No
    Check if columns in the header equal to ''
    '''
    ans, reason = 1,'Columns'
    marker=[]
    for index, i in enumerate(header):
        if (i==''):
            ans = 1
            marker.append(index)
    if (len(marker)!=0):
        if(len(marker) ==1):
            reason = 'Column '
        for index, i in enumerate(marker):
            marker[index] += 1
            reason += str(marker[index])
            reason += str(',')
        if(len(marker)==1):
            reason += ' is empty'
        else:
            reason +=' are empty'
    else:
        ans = 0
        reason = 'all the columns have a column name.'

    return Answer[ans], reason


def _2b_11():
    '''
    1. essential
    Are the column names consistent with the documentation?
    '''
    ans, reason = 3,'No documentation presented'
    return Answer[ans], reason


def _2b_12():
    '''
    2. valuable
    Where possible, is human understable information preferred over coded information (e.g., "cat", "dog" instead of "1", "2" to represent cat and dog, respectively).
    '''
    ans, reason = 1,''
    excldue = ['id','value','date','number','year','scenario']
    warning_columns = []
    tmp = data[random.randint(0,len(data))]
    for indx,i in enumerate(header):
        skip = False
        for j in excldue:
            if j in i:
                skip = True
        if skip or re.match("^\d+?\.\d+?$", tmp[indx]) is not None:
            continue
        if str(tmp[indx]).isdigit():
            warning_columns.append(indx)
    if len(warning_columns) == 0:
        ans, reason = 0,''
    else:
        ans, reason = 1,'The %s columns may should not be coded information'%warning_columns
    return Answer[ans], reason


def _2b_13():
    '''
    1. essential
    Does each record (row) have a unique identifier?
    '''
    ans, reason = 0,''
    if len(header)>=1: 
        s = {}
        for indx,i in enumerate(data):
            if i[0] in s:
                ans = 1
                reason = 'Identifier in row %d conflicts with row %d'%(indx+2,s[i[0]]+2)
                break
            else:
                s[i[0]] = indx
    return Answer[ans], reason


def _2b_14():
    '''
    1. essential
    Can the tables in a data collection be linked via common fields (columns)?
    '''
    ans, reason = 2,'This tool is only used for single dataset'
    return Answer[ans], reason


def _2b_15():
    '''
    1. essential
    Can the data tables be linked to the metadata via common fields (columns)?
    '''
    ans, reason = 2,'This tool is only used for single dataset'
    return Answer[ans], reason

def _2b_16():
    '''
    2. valuable
    Are the filenames consistent, descriptive, and informative (clearly indicates content) to humans?
    '''
    ans, reason = 0,'The question is subjective, so it would be better to double check it by humans.'
    return Answer[ans], reason

def _2b_17():
    '''
    3. desirable
    Do the filenames follow the convention: less than 70 characters; most unique content at start of filename; no acronyms; no jargon; no organization name?
    '''
    ans, reason = 0, ''
    filename = os.path.splitext(file_path)[-2]
    if(len(filename)>70):
        ans, reason = 1, 'File name should not be longer than 70 characters.'
    else:
        #if there are two or more continuous capitals, there might be acronyms in file name
        has_continuous_capital = False
        for i in range(1,len(filename)):
            if filename[i].isupper() and filename[i-1].isupper():
                has_continuous_capital = True
                break
        if has_continuous_capital == True:
            ans, reason = 1, 'There might be acronyms in file name.'
    return Answer[ans], reason


def _2b_18():
    '''
    2. valuable
    Was a logical, documented naming convention used for file names?
    '''
    ans, reason = 0, 'File names are logical and documented'
    filename = os.path.splitext(file_path)[-2]
    ret = name_split(filename)
    dictionary = enchant.Dict("en_US")
    for str in ret:
        if dictionary.check(str):
            pass
        else:
            ans, reason = 1, 'File names are not logical.'
    return Answer[ans], reason

def _2b_19():
    '''
    3. desirable
    Are standard/controlled vocabularies used within the data?
    '''
    ans, reason = 2,'Standard/controlled criterias are needed.'
    return Answer[ans], reason

def evaluate():
    global results_according_to_modules
    res = [ eval('_%s()'%i) for i in finished_modules ]
    for i in finished_modules:
        print('_%s'%i)
        print( eval("_%s()"%i) )
    print(res)
    results_according_to_modules = res


def task2_overall_rating():
    tmp = [i[0] for i in results_according_to_modules]
    count_result = [ tmp.count(Answer[i])  for i in range(len(Answer))]
    print(count_result)
    output = 'Amongst %d criteria of the checklist'%(len(finished_modules))
    for i in range(len(Answer)):
        output += '\nThere are %d answers are "%s", proportion is %.3f%%'%(count_result[i], Answer[i], count_result[i]*100.0/len(finished_modules))

    tmp = count_result[0]*100.0/len(finished_modules)
    if tmp >= threshold:
        output += '\n\nProportion of \'Yes\' is %.2f%%, which is bigger than the threshold %.2f%%. \nSo the dataset PASSED according to the checklist.'%(tmp, threshold)
    else:
        output += '\n\nProportion of \'Yes\' is %.2f%%, which is smaller than the threshold %.2f%%. \nSo the dataset FAILED according to the checklist.'%(tmp, threshold)
    print(output)
    with open('output.txt','w') as fout:
        fout.write(output)
        fout.flush()
    pass


def task3_R_markdown_report():
    dataset_name = ntpath.basename(file_path)
    summary = [ [0 for j in range(len(Answer))] for i in range(3) ]
    for indx,i in enumerate(finished_modules):
        r = int(checklist_data[i][1][0]) - 1
        col = Answer.index(results_according_to_modules[indx][0])
        summary[r][col] += 1
    for i in summary:
        print(i)

    summary_table = ''
    priority = ['essential', 'valuable', 'desirable']
    for i in range(3):
        tmp = '| x-%d  | number %s | %d |'%(i+1, priority[i], sum(summary[i]))
        for j in range(len(Answer)):
            tmp += ' %d |'%(summary[i][j])
        tmp += '\n'
        summary_table += tmp
    summary_table += '| x-4  | total | %d |'%(len(finished_modules))

    for j in range(len(Answer)):
        summary_table += ' %d |'%( sum([i[j] for i in summary]) )
    summary_table += '\n'

    total = len(finished_modules)*0.01
    for i in range(3):
        tmp = '| x-%d  | percent %s | %.1f%% |'%(i+4, priority[i], sum(summary[i])/total)
        for j in range(len(Answer)):
            tmp += ' %.1f%% |'%(summary[i][j]/total)
        tmp += '\n'
        summary_table += tmp
    summary_table += '| x-7  | total | %.1f%% |'%(len(finished_modules)/total)

    for j in range(len(Answer)):
        summary_table += ' %.1f%% |'%( sum([i[j] for i in summary])/total )
    summary_table += '\n'


    detail_table = ''
    for indx,i in enumerate(finished_modules):
        detail_table += '|%s|%s|%s|%s|%s|%s|\n'%\
        (i,checklist_data[i][0],checklist_data[i][1],checklist_data[i][2],results_according_to_modules[indx][0],results_according_to_modules[indx][1])


    markdown = '''
---
title: "%s"
output: html_document
---

The code below demonstrates an R markdown report containing:

* Overview and summary of the assessment results

* Detailed assessment results

of the given dataset %s.

## Overview and summary of the assessment results

| ID   | Category          | Questions | Answers (yes) | Answers (no) | Answers (not applicable) | Answers (I don't no) |
| ---- | ----------------- | --------- | ------------- | ------------------------ | ------------ | -------------------- |
%s

### Using diagram to show the summary

```{python}
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(9,6))
n = 3
X = np.arange(n)+1
Y = np.array(%s).transpose()
# X = ['essential', 'valuable', 'desirable','essential', 'valuable', 'essential', 'valuable', 'essential']
index_ls = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
plt.bar(X, Y[0], alpha=0.9, width = 0.175, facecolor = 'lightskyblue', edgecolor = 'white', label='yes', lw=1)
plt.bar(X+0.175, Y[1], alpha=0.9, width = 0.175, facecolor = 'yellowgreen', edgecolor = 'white', label='no', lw=1)
plt.bar(X+0.35, Y[2], alpha=0.9, width = 0.175, facecolor = 'orange', edgecolor = 'white', label='not applicable', lw=1)
plt.bar(X+0.525, Y[3], alpha=0.9, width = 0.175, facecolor = 'yellow', edgecolor = 'white', label='I dont know', lw=1)
plt.legend(loc="upper right")
plt.xlabel('essential                                     valuable                                          desirable')
plt.show()
```






## Detailed assessment results

| ID   | Category | Priority for now | Data checklist questions | Answer | Explanation |
| ---- | -------- | ---------------- | ------------------------ | ------ | ----------- |
%s


'''%(dataset_name+' Report', dataset_name, summary_table, summary, detail_table)

    print(markdown)
    with open('RMarkDownReport.Rmd','w') as fout:
        fout.write(markdown)
        fout.flush()
    pass

def main():
    load_dataset()
    #print(_2b_5())
    evaluate()
    task2_overall_rating()
    task3_R_markdown_report()
    pass

if __name__ == '__main__':
    main()
    