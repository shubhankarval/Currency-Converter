import PySimpleGUI as sg
from info import *
from app import *

sg.theme('Dark Teal 7')

# columns for currencies
col1 = [[sg.Text('From',font='MongolianBaiti')],[sg.Combo(currencyList,default_value=usd,key='from',font='NirmalaUI', readonly=True, size=(30,1))]]
col2 = [[sg.Text('To',font='MongolianBaiti')],[sg.Combo(currencyList,default_value=inr,key='to', font='NirmalaUI', readonly=True, size=(30,1))]]


layout = [[sg.Text('Amount',font='MongolianBaiti'), sg.Input(key='amount',font='NirmalaUI'), sg.Button('Go',key='convert',font='HPSimplified')],
        [sg.Column(col1), sg.Button('', key='switch', image_data=arrow, 
        image_subsample=25,button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0),  
        sg.Column(col2)],
        [sg.Text('',key='result',visible=False,font='MongolianBaiti 15 bold')]]

window = sg.Window('Currency Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == "switch": # switch the two selected currencies
        window['from'].update(values['to'])
        window['to'].update(values['from'])
        values['from'] , values['to'] = values['to'], values['from']

    elif event == "convert": # initiate conversion
        convertFrom, convertTo, amt = values['from'][:3],values['to'][:3],values['amount']
        res = convert(convertFrom, convertTo, amt)
        if res[0] == 'P':
            window['result'].update(text_color='#000000')
        else:
            res=f"{amt} {convertFrom} = {res} {convertTo}"
            window['result'].update(text_color='#FAFAFA')

        window['result'].update(res,visible=True)
    
    print(event, values)

window.close()
