# Get access to wolfram Alpha, where it ask you something and give you an answer.
import wolframalpha
client = wolframalpha.Client('V4L279-552P4V4JW3')
#Importing Wikipedia 
import wikipedia
# Next is creating a User interface which is a GUI that will make it appear on a window and not in a console.
import PySimpleGUI as sg


sg.theme('DarkBlue')
# All the stuff inside your window.
layout = [[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Jarvis', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    res = client.query(values[0])
    wolfram_res = next(res.results).text
    wiki_res =  wikipedia.summary(values[0], sentences=2)
    #Importing speech 
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(wolfram_res)
    engine.say(wiki_res)
    sg.PopupNonBlocking("Wolfram Results :" +wolfram_res, "Wikepedia Result: " +wiki_res)
    engine.runAndWait() 

    
    print(values[0])

window.close()



