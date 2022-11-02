from libsast import Scanner
import pprint
import sys
import os
from tabulate import tabulate
import pandas as pd

file_path = input('Enter a file path: ')
pprint.pprint('Entered file path to be scanned: '+ file_path)
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
paths = [file_path]
scanner = Scanner(options, paths)

info = scanner.scan()

choice = int(input("Enter 1 to create a results file : "))
if(choice == 1):
    sys.stdout = open('output2.txt','wt')
    a = list((info['semantic_grep']['matches']['detect-eval-with-expression'].values()))
    b = list((info['semantic_grep']['matches']['API-call'].values()))


    eval = []
    for i in a:
        if type(i) == list:
            for y in i:
                eval.append(y)
            print("\n")
            break
        else:
            data = pd.DataFrame(i)
            df = data.loc[:, data.columns != 'file_path']
            print(df)
            print("\n")
    print("\n")

    api = []
    for i in b:
        if type(i) == list:
            for y in i:
                api.append(y)
            break
        else:
            data = pd.DataFrame(i)
            df = data.loc[:, data.columns != 'file_path']
            print(df)
            print("\n")

    data = pd.DataFrame(eval)
    df = data.loc[:, data.columns != 'file_path']
    pdtabulate = lambda df:tabulate(df,headers='keys',tablefmt='grid')
    print(pdtabulate(df))
    print("\n")

    data = pd.DataFrame(api)
    df = data.loc[:, data.columns != 'file_path']
    pdtabulate = lambda df:tabulate(df,headers='keys',tablefmt='grid')
    print(pdtabulate(df))
    print("\n")



        