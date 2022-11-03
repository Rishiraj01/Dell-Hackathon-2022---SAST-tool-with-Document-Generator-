from libsast import Scanner
import sys
import pandas as pd
import streamlit as st
from tabulate import tabulate
import subprocess

pd.set_option('display.max_columns', None)

options = {
    "ignore_filenames": {
        "bootstrap.min.js",
        ".DS_Store",
        "bootstrap-tour.js",
        "d3.min.js",
        "tinymce.js",
        "codemirror.js",
        "tinymce.min.js",
        "react-dom.production.min.js",
        "react.js",
        "jquery.min.js",
        "react.production.min.js",
        "codemirror-compressed.js",
        "axios.min.js",
        "angular.min.js",
        "raphael-min.js",
        "vue.min.js",
        "sast.py",
    },
    "sgrep_rules": "rule",
    "sgrep_extensions": {"", ".yml"},
    "ignore_extensions": {".7z", ".exe", ".rar", ".zip", ".a", ".o", ".tz"},
    "ignore_paths": {
        "__MACOSX",
        "jquery",
        "fixtures",
        "node_modules",
        "bower_components",
        "example",
        "spec",
    },
    "show_progress": False,
}
paths = ["file/"]
scanner = Scanner(options, paths)

info = scanner.scan()

rules = []

data = info["semantic_grep"]['matches']

for a in info['semantic_grep']['matches']:
    rules.append(a)

rules_list = []

meta_list = []

for a in rules:
    rules_list.append(list(data[a].values())[0])

for a in rules:
    meta_list.append(list(data[a].values())[1])

sys.stdout = open('output2.txt','wt')


print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\tIntegration Architecture Document")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
y = int(0)

print("")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\tINFO:")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
y = 0
db = False
for i in rules_list:
    if "INFO" in rules[y]:
        data = pd.DataFrame(i)
        df = data.loc[:, data.columns != 'file_path']
        pdtabulate = lambda df:tabulate(df,headers='keys',tablefmt='grid')
        print("CODE DEPENDENCIES : {}".format(rules[y]))
        print(meta_list[y])
        print(pdtabulate(df))
        print("Total Dependencies : {}".format(df.shape[0]))
        if 'SQL' in rules[y]:
            db = True
        if 'php' in rules[y]:
            returned_output = subprocess.check_output(["php","-v"])
            print("PHP Version : ",returned_output.decode("utf-8"))
        print("\n")
    y = y + 1

y = 0

print("")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\tRule Violation:")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
if db:
    print("You can only use Mongo as a Database")


print("")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\tWARNINGS:")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
for i in rules_list:
    if "WARNING" in rules[y]:
        data = pd.DataFrame(i)
        df = data.loc[:, data.columns != 'file_path']
        pdtabulate = lambda df:tabulate(df,headers='keys',tablefmt='grid')
        print("Vulnerability Detected : {}".format(rules[y]))
        print(meta_list[y])
        print(pdtabulate(df))
        print("Count of possible Vulnerabilities : {}".format(df.shape[0]))
        if 'php' in rules[y]:
            returned_output = subprocess.check_output(["php","-v"])
            print("PHP Version : ",returned_output.decode("utf-8"))
        print("\n")
    y = y + 1

print("")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\tERRORS:")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
y = 0
for i in rules_list:
    if "ERROR" in rules[y]:
        data = pd.DataFrame(i)
        df = data.loc[:, data.columns != 'file_path']
        pdtabulate = lambda df:tabulate(df,headers='keys',tablefmt='grid')
        print("Vulnerability Detected : {}".format(rules[y]))
        print(meta_list[y])
        print(pdtabulate(df))
        print("Count of Vulnerabilities : {}".format(df.shape[0]))
        if 'php' in rules[y]:
            returned_output = subprocess.check_output(["php","-v"])
            print("PHP Version : ",returned_output.decode("utf-8"))
        print("\n")
    y = y + 1
