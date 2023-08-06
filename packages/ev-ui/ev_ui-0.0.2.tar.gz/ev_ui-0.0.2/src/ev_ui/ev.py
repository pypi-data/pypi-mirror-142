#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:56:42 2022

@author: emilydu
"""

__version__ = '0.0.2'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:09:18 2022

@author: emilydu
"""

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
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1.5)


# ------------------------------- Toolbar function -------------------------------

class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)




# ------------------------------- Window1 CODE-------------------------------

# imagefile = b'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'
# , sg.Image(imagefile, k='-IMAGE-')

def make_win1():
    buttons = [
        [sg.Button('Visualization', font='Any 13 bold'), sg.Button('Machine Learning',font='Any 13 bold')],
        [sg.Button('Exit', font='Any 12')]
        ]
    
    layout = [
        [sg.Text('Welcome to Machine Learning based on EIS',size=(40, 1), justification='center', font='Any 20')],
              [sg.Text('Please select one to start:', font='Any 14')],
              [sg.Column(buttons)]
              ]
   
    window = sg.Window('Machine Learning based on EIS', layout, finalize=True, margins=(20, 20))
    # window.set_min_size(window.size)
    
    return window




# ------------------------------- Window2 code -------------------------------


def make_win2():


    top_col = [
        [sg.T('*Needs more instruction', font='Any 14')], #title name
                [sg.T('Please select your input file:', font='Any 12'),sg.Input(key='-visual_file-'), sg.FileBrowse()], #file browse
                [sg.T('Cycle Number', font='Any 12'),sg.InputText(key='-number-')], #cycle number
                [sg.T('Please select the plotting sytle:', font='Any 12')], 
                [sg.Button('EIS', font='Any 13 bold'), sg.B('dqdv', font='Any 13 bold'), sg.B('Cycling', font='Any 13 bold')]
                           
                ]



    layout = [ 
        [sg.T('Data Visualization', size=(50, 1), justification='center', font='Any 20 bold')],
               [sg.Column(top_col, element_justification='left')], 
               [sg.T('Controls panel:', font='Any 14 bold')],
                [sg.Canvas(key='controls_cv')],
                [sg.T('Figure:',font='Any 14 bold')],
                    [sg.Column(
                    layout=[
                        [sg.Canvas(key='fig_cv',
                                   size=(300 * 2, 300)
                                   )]
                    ],
                    background_color='#DAE0E6',
                    pad=(0, 0)
                )],
               [sg.B('Exit')] 
               
               ]
    
    window = sg.Window('Data Visualization', layout, finalize=True)
    

    return window


# ------------------------------- Window3 code -------------------------------

def make_win3():
    
    offline = [
        [sg.T('Offline Training', font='Any 16 bold')],
        [sg.T('Please select your input file:', font='Any 12'),sg.Input(key = '-file1-'), sg.FileBrowse()],
        [sg.T('Please select your training model:', font='Any 12'), sg.B('Random Forest Regression Offline', font='Any 12'), sg.B('Gradient Boosting Regression Offline', font='Any 12')],
        [sg.Text('Output value:', font='Any 14 bold'), sg.Text(size=(50,1), font = 'Any 14 bold',text_color='#003366', key='-OUTPUT_off-')],
        [sg.Text('Confidence interval:', font='Any 14 bold'), sg.Text(size=(50,1), font = 'Any 14 bold', text_color='#003366', key='-CI_off-')]
        ]
    
    
    online = [
        [sg.T('Online Training', font='Any 16 bold')],
        [sg.T('Please select your input file:', font='Any 12'),sg.Input(key = '-file2-'), sg.FileBrowse()],
        [sg.T('If you choose Random Forest, please assign variables below:', font='Any 12')],
        [sg.T('N Estimators', font='Any 12'),sg.InputText(key='-R_estimators-')],
        [sg.T('Max features', font='Any 12'),sg.InputText(key='-features-')],
        [sg.T('If you choose Gradient Boosting, please assign variables below:', font='Any 12')],
        [sg.T('N Estimators', font='Any 12'),sg.InputText(key='-G_estimators-')],
        [sg.T('Learning rate', font='Any 12'),sg.InputText(key='-rate-')],
        [sg.T('Max depth', font='Any 12'),sg.InputText(key='-depth-')],
        [sg.T('Please select your training model:', font='Any 12'), sg.B('Random Forest Regression Online',font='Any 12'), sg.B('Gradient Boosting Regression Online', font='Any 12')],
        [sg.Text('Output value:', font='Any 14 bold'), sg.Text(size=(50,1), font = 'Any 14 bold', text_color='#003366', key='-OUTPUT_on-')],
        [sg.Text('Confidence interval:', font='Any 14 bold'), sg.Text(size=(50,1), font = 'Any 14 bold', text_color='#003366', key='-CI_on-')]
        
        
        ]
    
    
    
    layout = [ 
        [sg.Text('Machine Learning', size=(50, 1), justification='center', font=('Any 20 bold'))]]
    layout +=[[sg.TabGroup([[  sg.Tab('Offline training', offline),
                              sg.Tab('Online training', online),]
                              ])],
              [sg.B('Exit')] 
              ]
    
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('Machine Learning', layout,  resizable=True, finalize = True)
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
           
            elif event == 'dqdv':

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
                output_value_off = str(EIS_to_cap_retention_off_rdf(file_off)[0])
                    
                window['-OUTPUT_off-'].update(output_value_off)
                window['-CI_off-'].update('NA')
                    # window['-CI_off-'].update(CI)
                    
            elif event == 'Gradient Boosting Regression Offline':
                file_off = values['-file1-']
                output_value_gbr = str(EIS_to_cap_retention_off_gbr(file_off)[0][0])
                CI_off = str([EIS_to_cap_retention_off_gbr(file_off)[1][0], EIS_to_cap_retention_off_gbr(file_off)[2][0]])
                window['-OUTPUT_off-'].update(output_value_gbr)
                window['-CI_off-'].update(CI_off)
                    
            # elif event == 'Online training':
                
                
            elif event == 'Random Forest Regression Online':
                file_on = values['-file2-']
                N_Estimators_R = int(values['-R_estimators-'])
                Max_features = int(values['-features-'])
                output_value_on = str(EIS_to_cap_retention_onl_rdf(file_on, N_Estimators_R, Max_features)[0])
                window['-OUTPUT_on-'].update(output_value_on)
                window['-CI_on-'].update('NA')
                
            elif event == 'Gradient Boosting Regression Online':
                file_on = values['-file2-']
                N_Estimators_G = int(values['-G_estimators-'])
                Learning_rate = float(values['-rate-'])
                Max_depth = int(values['-depth-'])
                output_value_gbr = str(EIS_to_cap_retention_onl_gbr(file_on, Learning_rate, N_Estimators_G, Max_depth)[0][0])
                CI_on = str([EIS_to_cap_retention_onl_gbr(file_on, Learning_rate, N_Estimators_G, Max_depth)[1][0], EIS_to_cap_retention_onl_gbr(file_on, Learning_rate, N_Estimators_G, Max_depth)[2][0]])
                window['-OUTPUT_on-'].update(output_value_gbr)
                window['-CI_on-'].update(CI_on)
                
                
                
    window.close()

if __name__ == '__main__':
    main()