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

    y = int(0)
    sys.stdout = open('output2.txt','wt')
    for i in rules_list:
        data = pd.DataFrame(i)
        df = data.loc[:, data.columns != 'file_path']
        pdtabulate = lambda df:tabulate(df,headers='keys',tablefmt='grid')
        print(meta_list[y])
        y = y + 1
        print(pdtabulate(df))
        print("\n")