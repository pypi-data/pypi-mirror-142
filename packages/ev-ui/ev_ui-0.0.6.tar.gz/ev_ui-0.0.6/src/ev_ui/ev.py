#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:54:49 2022

@author: emilydu
"""

__version__ = '0.0.6'

from ml_eis import *
import PySimpleGUI as sg
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use("TkAgg")

#Decide theme of windows
sg.theme('LightBlue2')

# ------------------------------- Figure drawing code -------------------------------

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    '''

    Parameters
    ----------
    canvas : TYPE
        DESCRIPTION.
    fig : TYPE
        DESCRIPTION.
    canvas_toolbar : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    plt.close('all')
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)



# ------------------------------- Toolbar function -------------------------------

class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)










# ------------------------------- Window1 CODE-------------------------------

imagefile = b'iVBORw0KGgoAAAANSUhEUgAAALwAAABSCAYAAADuB75ZAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABaGVYSWZNTQAqAAAACAAGARIAAwAAAAEAAQAAARoABQAAAAEAAABWARsABQAAAAEAAABeASgAAwAAAAEAAgAAATIAAgAAABQAAABmh2kABAAAAAEAAAB6AAAAAAAAAEgAAAABAAAASAAAAAEyMDIyOjAzOjE0IDE4OjI1OjM1AAAOkAAABwAAAAQwMjIxkAMAAgAAABQAAAEokAQAAgAAABQAAAE8kBAAAgAAAAcAAAFQkBEAAgAAAAcAAAFYkBIAAgAAAAcAAAFgkQEABwAAAAQBAgMAkpAAAgAAAAQ5MjkAkpEAAgAAAAQ5MjkAkpIAAgAAAAQ5MjkAoAAABwAAAAQwMTAwoAIABAAAAAEAAAC8oAMABAAAAAEAAABSpAYAAwAAAAEAAAAAAAAAADIwMjI6MDM6MTQgMTg6MjU6MzUAMjAyMjowMzoxNCAxODoyNTozNQAtMDc6MDAAAC0wNzowMAAALTA3OjAwAADdodMvAAAACXBIWXMAAAsTAAALEwEAmpwYAAAHL2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIj4KICAgICAgICAgPHRpZmY6UmVzb2x1dGlvblVuaXQ+MjwvdGlmZjpSZXNvbHV0aW9uVW5pdD4KICAgICAgICAgPHRpZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzI8L3RpZmY6WVJlc29sdXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyPC90aWZmOlhSZXNvbHV0aW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFlEaW1lbnNpb24+MTE0PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6T2Zmc2V0VGltZT4tMDc6MDA8L2V4aWY6T2Zmc2V0VGltZT4KICAgICAgICAgPGV4aWY6RXhpZlZlcnNpb24+MDIyMTwvZXhpZjpFeGlmVmVyc2lvbj4KICAgICAgICAgPGV4aWY6U3Vic2VjVGltZT45Mjk8L2V4aWY6U3Vic2VjVGltZT4KICAgICAgICAgPGV4aWY6U3Vic2VjVGltZURpZ2l0aXplZD45Mjk8L2V4aWY6U3Vic2VjVGltZURpZ2l0aXplZD4KICAgICAgICAgPGV4aWY6Q29tcG9uZW50c0NvbmZpZ3VyYXRpb24+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpPjE8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaT4yPC9yZGY6bGk+CiAgICAgICAgICAgICAgIDxyZGY6bGk+MzwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpPjA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L2V4aWY6Q29tcG9uZW50c0NvbmZpZ3VyYXRpb24+CiAgICAgICAgIDxleGlmOkNvbG9yU3BhY2U+MTwvZXhpZjpDb2xvclNwYWNlPgogICAgICAgICA8ZXhpZjpTdWJzZWNUaW1lT3JpZ2luYWw+OTI5PC9leGlmOlN1YnNlY1RpbWVPcmlnaW5hbD4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjI2MDwvZXhpZjpQ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'


def make_win1():

    buttons = [
        [sg.Button('Visualization', font='Any 13 bold'), sg.Button('Machine Learning',font='Any 13 bold')],
        [sg.Button('Exit', font='Any 12')]
        ]
    
    layout = [[sg.Text('Welcome to Echem Visualizer',size=(30, 1), justification='center', font='Any 20')],
              [sg.Text('Please select one to start:',  font='Any 14')],
              [sg.Column(buttons), sg.Image(imagefile, k='-IMAGE-')]
              ]
   
    window = sg.Window('Echem Visualizer', layout, finalize=True, margins=(20, 20))

    
    return window




# ------------------------------- Window2 code -------------------------------


def make_win2():


    top_col = [
        [sg.T(
'''This program allows the user to plot three different forms of electrochemistry data. The plotted figure can then be adjusted and exported 
as needed. These are the supported file types:
    - Auto-lab EIS data
    - Battery cycling data''', font='Any 12')],

    [sg.T('''User instruction: 
    - EIS plot: Please import your auto-lab EIS file only (other files will not be supported!). Leave the cycling number blank.
    - dQ/dV plot: Please import your cycling data and specify the cycling number.
    - Cycling plot: Please import your cycling data and specify the cycling number.
After importing the data, please click on the plot type. Figure will be shown below with a control panel.''',
             font='Any 12')], #title name
        # [sg.T('')],
        [sg.T('Please select your input file:', font='Any 12 bold'),sg.Input(key='-visual_file-', size=(80, 1)), sg.FileBrowse(font='Any 12')], #file browse
                [sg.T('Cycle Number', font='Any 12 bold'),sg.InputText(key='-number-', size=(80, 1)), sg.T('(Integer Only)') ], #cycle number
                [sg.T('Please select the plot type:', size=(80, 1), font='Any 12 bold')], 
                [sg.Button('EIS', size=(10,1), font='Any 13 bold'), sg.B('dQ/dV', size=(10,1),font='Any 13 bold'), sg.B('Cycling', size=(10,1),font='Any 13 bold')]
                           
                ]



    layout = [ 
        [sg.T('Data Visualization', size=(40, 1), justification='center', font='Any 24 bold'), sg.Image(imagefile, k='-IMAGE-')],
               [sg.Column(top_col, element_justification='left')], 
               [sg.T('Control panel:', font='Any 14 bold')],
                [sg.Canvas(key='controls_cv')],
                [sg.T('Figure:',font='Any 14 bold')],
                [sg.Column(
                    layout=[
                        [sg.Canvas(key='fig_cv',
                                   size=(250 * 2, 250)
                                   )]
                    ],
                    background_color='#DAE0E6',
                    pad=(0, 0)
                )],
               [sg.B('Exit')] 
               
               ]
    
    window = sg.Window('Echem Visualizer', layout, resizable=True, finalize=True)
    

    return window


# ------------------------------- Window3 code -------------------------------

def make_win3():
    
    offline = [
        
        
        [sg.T('Offline Training', font='Any 16 bold')],
        [sg.T('''Offline training model is based on 40 Samsung NMC 111/graphite full cell batteries from the UW Schwartz Lab. 
The program enables the user to predict capacity retention after 200 cycles based on early cycle impedance data.

Offline training enables the user to do a quick capacity classification on the battery grade based on the first 10 cycles of impedance data.''', font='Any 12')],
[sg.T('User instruction:', font = 'Any 12 bold')],
[sg.T('''    - Please select your input data file (auto-lab EIS only!).
    - Please select the desired training model.
    
Capacity retention will be returned with the confidence interval (as a percentage).
''', font='Any 12')],
        [sg.T('Input data file:', font='Any 12 bold'),sg.Input(key = '-file1-'), sg.FileBrowse(font='Any 12')],
        [sg.T('Please select your training model:', font='Any 12 bold'), sg.B('Random Forest Regression Offline', font='Any 13 bold'), sg.B('Gradient Boosting Regression Offline', font='Any 13 bold')],
        [sg.Text('Capacity rentention:', font='Any 14 bold'), sg.Text(size=(15,1), font = 'Any 14 bold',text_color='#003366', key='-OUTPUT_off-'), sg.T('%',font = 'Any 14 bold',text_color='#003366' )],
        [sg.Text('90% Confidence interval:', font='Any 14 bold'), sg.Text(size=(15,1), font = 'Any 14 bold', text_color='#003366', key='-CI_off-'),  sg.T('%',font = 'Any 14 bold',text_color='#003366')]
        ]
    
    
    online = [
        
        
        
        [sg.T('Online Training', font='Any 16 bold')],
        [sg.T('''Online training enables user to explore the machine learning parameters using the 40 Samsung NMC 111/graphite full cell batteries 
from the UW Schwartz Lab.''', font='Any 12')],
[sg.T('User instruction:', font = 'Any 12 bold')],
[sg.T('''    - Please select your input data file (auto-lab EIS only!).
    - Follow the steps below:
        - Random Forest: please specify N estimators and max features.
        - Gradient Boosting: please specify N estimators, learning rate, and max depth.
        
Capacity retention will be returned with the confidence interval (as a percentage).
''', font='Any 12')],

        [sg.T('Input data file:', font='Any 12'),sg.Input(key = '-file2-'), sg.FileBrowse(font='Any 12')],
        [sg.T('If you choose Random Forest, please assign variables below:', font='Any 12 bold')],
        [sg.T('N estimators', font='Any 12'),sg.InputText(key='-R_estimators-'), sg.T('(Integer Only)') ],
        [sg.T('Max features', font='Any 12'),sg.InputText(key='-features-'),  sg.T('(Integer Only)')],
        [sg.T('If you choose Gradient Boosting, please assign variables below:', font='Any 12 bold')],
        [sg.T('N estimators', font='Any 12'),sg.InputText(key='-G_estimators-'), sg.T('(Integer Only)')],
        [sg.T('Learning rate', font='Any 12'),sg.InputText(key='-rate-'),  sg.T('(Between 0.01 to 1)')],
        [sg.T('Max depth', font='Any 12'),sg.InputText(key='-depth-'), sg.T('(Integer Only)')],
        [sg.T('Please select your training model:', font='Any 12'), sg.B('Random Forest Regression Online',font='Any 13 bold'), sg.B('Gradient Boosting Regression Online', font='Any 13 bold')],
        [sg.Text('Capacity rentention:', font='Any 14 bold'), sg.Text(size=(20,1), font = 'Any 14 bold', text_color='#003366', key='-OUTPUT_on-'), sg.T('%',font = 'Any 14 bold',text_color='#003366' )],
        [sg.Text('90% Confidence interval:', font='Any 14 bold'), sg.Text(size=(20,1), font = 'Any 14 bold', text_color='#003366', key='-CI_on-'), sg.T('%',font = 'Any 14 bold',text_color='#003366' )]
        
        
        ]
    
    
    
    layout = [ 
        
        [sg.Text('Machine Learning', size=(40, 1), justification='center', font=('Any 24 bold')), sg.Image(imagefile, k='-IMAGE-')]]
    layout +=[[sg.TabGroup([[  sg.Tab('Offline training', offline),
                              sg.Tab('Online training', online),]
                              ])],
              [sg.B('Exit')] 
              
              ]
    
    
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('Echem Visualizer', layout,  resizable=True, finalize = True)
    window.set_min_size(window.size)
    
    return window





# ------------------------------- Main event loop -------------------------------

def main():
    window1, window2, window3= make_win1(), None, None     # start off with 1 window open

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            if window ==window3:       # if closing win 3, mark as closed
                window3 = None
            if window == window1:     # if closing win 1, exit program
                break



        if event == 'Visualization' and not window2:
            window2 = make_win2()
        
        if window == window2:
    
            if event == 'EIS':
                # draw_figure_w_toolbar(window['fig_cv'].TKCanvas, Nyquist_plot_UI(values[0]),window['controls_cv'].TKCanvas)
                draw_figure_w_toolbar(window['fig_cv'].TKCanvas, Nyquist_plot_UI(values['-visual_file-']),window['controls_cv'].TKCanvas)
           
            elif event == 'dQ/dV':
                # draw_figure_w_toolbar(window['fig_cv'].TKCanvas, diff_cap(values[0], int(values['-number-'])),window['controls_cv'].TKCanvas)
                draw_figure_w_toolbar(window['fig_cv'].TKCanvas, diff_cap(values['-visual_file-'], int(values['-number-'])),window['controls_cv'].TKCanvas)
            elif event == 'Cycling':
                # draw_figure_w_toolbar(window['fig_cv'].TKCanvas,cycling_CCCV(values[0], int(values['-number-'])),window['controls_cv'].TKCanvas)
                draw_figure_w_toolbar(window['fig_cv'].TKCanvas,cycling_CCCV(values['-visual_file-'], int(values['-number-'])),window['controls_cv'].TKCanvas)    
            
            elif event == 'Exit' or event == sg.WIN_CLOSED:
                break
            
            
            
            
        if event == 'Machine Learning' and not window3:
            window3 = make_win3()
        
        if window == window3:
            
            if event == 'Random Forest Regression Offline':
                file_off = values['-file1-']
                output_value_off = str(EIS_to_cap_retention_off_rdf(file_off))
                    
                window['-OUTPUT_off-'].update(output_value_off)
                window['-CI_off-'].update('N/A')
                    
            elif event == 'Gradient Boosting Regression Offline':
                file_off = values['-file1-']
                output_value_gbr = str(EIS_to_cap_retention_off_gbr(file_off)[0])
                lower_off = EIS_to_cap_retention_off_gbr(file_off)[1]
                upper_off = EIS_to_cap_retention_off_gbr(file_off)[2]
                CI_off = str([ lower_off, upper_off])
                window['-OUTPUT_off-'].update(output_value_gbr)
                window['-CI_off-'].update(CI_off)
                    

                
                
            elif event == 'Random Forest Regression Online':
                file_on = values['-file2-']
                N_Estimators_R = int(values['-R_estimators-'])
                Max_features = int(values['-features-'])
                output_value_on = str(EIS_to_cap_retention_onl_rdf(file_on, N_Estimators_R, Max_features))
                window['-OUTPUT_on-'].update(output_value_on)
                window['-CI_on-'].update('N/A')
                
                
            elif event == 'Gradient Boosting Regression Online':
                file_on = values['-file2-']
                N_Estimators_G = int(values['-G_estimators-'])
                Learning_rate = float(values['-rate-'])
                Max_depth = int(values['-depth-'])
                lower_on = EIS_to_cap_retention_onl_gbr(file_on, Learning_rate, N_Estimators_G, Max_depth)[1]
                upper_on = EIS_to_cap_retention_onl_gbr(file_on, Learning_rate, N_Estimators_G, Max_depth)[2]
                output_value_gbr = str(EIS_to_cap_retention_onl_gbr(file_on, Learning_rate, N_Estimators_G, Max_depth)[0])
                CI_on = str([ lower_on, upper_on])
                window['-OUTPUT_on-'].update(output_value_gbr)
                window['-CI_on-'].update(CI_on)
                
                
                
    window.close()

if __name__ == '__main__':
    main()