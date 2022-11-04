import PySimpleGUI as sg
import os

working_directory = os.getcwd()

layout = [  
            [sg.Text("Choose a folder:")],
            [sg.InputText(key="-FILE_PATH-"), 
            sg.FolderBrowse(initial_folder=working_directory)],
            [sg.Button('Submit'), sg.Exit()]
        ]

window = sg.Window("Integrated Architecture Document Generator", layout)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Submit":
        folder_address = values["-FILE_PATH-"]
        os.system('.\output2.txt')
window.close()