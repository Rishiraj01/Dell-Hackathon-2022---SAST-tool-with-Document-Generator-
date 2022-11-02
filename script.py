from libsast import Scanner
import pprint
import sys
import pandas as pd
import streamlit as st

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
    "sgrep_rules": "/mnt/c/Users/bhavi/OneDrive/Documents/Cp lab/Current/rule",
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
paths = ["/mnt/c/Users/bhavi/OneDrive/Documents/Cp lab/Current/file/aws.js"]
scanner = Scanner(options, paths)



info = scanner.scan()

result = '\n'.join(f'{key}: {value}' for key, value in info.items())

#sys.stdout = open('output2.txt','wt')

temp = list(result)
for i in range(0,len(result)):
    if temp[i].isnumeric() and temp[i+1] == ",":
        temp[i+1] = ' -'

result = "".join(temp)

chars_to_remove = ["{", "}", "'"]
chars_to_indent = [","]
for char in chars_to_remove:
    result = result.replace(char, " ")
for char in chars_to_indent:
        result = result.replace(char,"\n")

print(result)

        