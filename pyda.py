 Get access to wolfram Alpha, where it ask you something and give you an answer.
import wolframalpha
client = wolframalpha.Client('V4L279-552P4V4JW3')

# Next is creating a User interface which is a GUI that will make it appear on a window and not in a console.
import PySimpleGUI as sg

sg.theme('DarkPurple')
# All the stuff inside your window.
layout = [  [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Jarvis', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    res = client.query(values[0])


    print(next(res.results).text)

window.close()