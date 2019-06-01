# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:33:21 2017

@author: annawi

plotting of simple x-y plots with focus on chromatograms from GC and HPLC
"""

import os
import ast
import json
import numpy as np
import matplotlib.pyplot as plt

from pandas import DataFrame
import pandas as pd

load_new = False

if load_new:
    folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Calibration\Data_HPLC'
    folders = []
    filenames = {}
    
    for root, subfolders, files in os.walk(folder_path):
        if len(files)==0: continue
        #folders.append(root[-8:])
        folders.append(root[-8:])
        files_this_folder = []
        for filename in files:
            if filename.endswith(".CSV") or filename.endswith(".csv"):
                files_this_folder.append(filename)
                #print(root)
    #    filenames[root[-8:]] = files_this_folder
        filenames[root[-8:]] = files_this_folder
    
    #print(folders)
    print(filenames)
      
    input_folders = input("Enter the folders you want to plot in form of a dictionary: ")
#   print ("You selected " + input_folders) 
    
    plot_folders = ast.literal_eval(input_folders)
    print(plot_folders)
    
    files_to_plot=[]
    for folder, file_list in plot_folders.items():
        for file in file_list:
            files_to_plot.append(file)
        
    print("You selected following files to be plotted:")    
    print(files_to_plot)
    
    # custom labels for data: dictionary correlating filename with label to be assigned:
    input_data_label = input("Enter the datalabels to the files listed above in form of a list: ")
    data_label = dict(zip(files_to_plot, ast.literal_eval(input_data_label)))
    print(data_label)
    
    input_settings = {"folder_path": folder_path, "plot_folders": plot_folders, "data_label": data_label}
    save_settings_as = input("Save settings as ([...]_input.txt): ") + "_input.txt"
    with open(save_settings_as, 'w') as f:
        json.dump(input_settings, f)
        
else:
    settings_file = input("Enter the name of the settings file: ")
    with open(settings_file) as f:
        input_settings=json.load(f)
    print(input_settings)    
    
    

# settings for the plot
plot_settings = {'safeplot': True,
                 'plotname': 'HPLC_AA_AC_500mu_STANDARD',
                 'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                 'grid': True,
                 'second axis':  False,
                 'x_lim': (-1, 31),
                 'y_lim': (-10, 250),
                 'y2_lim': (0.25, 1.5),
                 'top_pad': 0.2,
                 'bottom_pad': 0.1,
                 'l_pad': [],
                 'r_pad': [],
                 'plotsize': (6,4.5) #size of plot in inches
                 }

# legend:
legend_settings = {'position': (0, 1.15),
                   'number_of_cols': 2,
                   'fontsize': 10
                   }

annotation_settings = {}
general_info = {}

def doplot(input_settings, legend_settings, annotation_settings, general_info):
    """
    Chooses what kind of plot to do and refers to that function
    :return: plot
    """
    print(input_settings)
    data(data = extract_data(folder_path=input_settings["folder_path"], 
                             filenames=input_settings['plot_folders'], 
                            data_label=input_settings['data_label'], general_info = general_info), plot_settings=plot_settings,
                legend_settings=legend_settings, annotation_settings=annotation_settings )
    
    
#collect relevant data for plotting in a DataFrame
def extract_data(folder_path, filenames, data_label, general_info):
    """
    Extracts dataframes containing potential and current from multiple dataframes, calculates potential vs RHE and current density using functions
     and stores it in a dataframe, to be accessible for plotting
    :return: data: List of Databases with information about the experiment: filename (string), scanrate (float), E vs ref, E vs RHE
     and I and i (Dataframe), label for plot (string)
    """
    data = []
    #data = {}

    for folder, files in filenames.items():
        for filename in files: #additional for loop to go through list of filenames

#            if folder in folders:
                # print(folder)
                # filepath = folder
                filepath = folder_path + "/" + folder + "/" + filename
                if filename in data_label:
                    label = data_label[filename]
                else:
                    label = filename#[filename.find("Pd"): filename.find("_C0")] + filename[filename.find('_cy'):filename.find('.')]
                
                print("extracting data from " + filepath)
                extracted_data = DataFrame(import_data_from(filepath))
                print(extracted_data)

                data.append({'filename': filename, 'data': extracted_data, 'label': label})
    return data
    
    
def import_data_from(file):
    """opens file and returns data as array
    """
    with open(file) as file:
            data = pd.read_csv(file, header=None, prefix='X')
    return data

def data(data, plot_settings, legend_settings, annotation_settings): #basically all the details that are chosen in the settings part go into this function
    """plot tuples(?) of signal intensity vs retention time
    main function of the program
    input: settings through doplot function
    output: plot
    """
    # prepare for figure with 2 x-axes
    fig = plt.figure(figsize=plot_settings['plotsize'])
    ax1 = fig.add_subplot(111)

    #List of 6 different linestyles to loop through
    # linestyle_list= ['-', (0, (2, 3)), '--', (3, (15, 7.5)) ,'-.',':', '-', (0, (2, 3)), '--', (3, (15, 7.5)),'-.',':',
    #                  '-', (0, (2, 3)), '--', (3, (15, 7.5)), '-.', ':','-', (0, (2, 3)), '--', (3, (15, 7.5)) ,'-.',':']
    linestyle_list = ['-', '-', '-', ':', ':', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    color_list = ['#283593', '#C70039', 'orange', 'g', 'k', 'c', 'm', '0.50',"#538612", '0.75','orange', 'g', 'r', 'b', 'k', 'c', 'm', '0.50',"#538612", '0.75']
    #color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
    #color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
    #print(color_list)
    i=-1
    j=-1

    for each_chromatogram in data:
        if i <= 11:
            i = i+1
        else: 
            i = 0
        j = j +1
        x = data[j]['data']['X0'].values.tolist()
        y = data[j]['data']['X1'].values.tolist()
        #print(x,y)
        print(i)
        plt.plot(x, y, color=color_list[i], linestyle = linestyle_list[i], label=data[j]['label'])
        # find and print the difference in current in the double layer capacitance region
#        current_file=data[j]['filename']
#        e_range = annotation_settings['e_range']
#        find_deltaI_DLcapacitance(e_vs_rhe=x, i_mApscm=y, e_range=e_range, file=current_file)


    #set axis limits according to info given in settings
    ax1.set_xlim(plot_settings['x_lim'])
    ax1.set_ylim(plot_settings['y_lim'])

    #create legend according to settings
    plt.legend(fontsize=legend_settings["fontsize"], loc=legend_settings["position"], ncol=legend_settings["number_of_cols"])

    #grid
    if plot_settings['grid']:
        ax1.grid(True, color="grey")

    #inserts second axis with E vs Ref on top, if selected in settings
    if plot_settings['second axis']:
        ax2 = ax1.twiny()
        ax1Ticks = ax1.get_xticks()
        ax2Ticks = ax1Ticks  # here the scaling of ticks could be changed

#        def tick_function(e_rhe):
#            e_nhe = - e_rhe_ref - 0.059 * ph_ref  # potential vs NHE
#            e_ref = e_rhe - e_nhe - 0.059 * ph
#            return ["%.2f" % z for z in e_ref]
#
#        ax2.set_xticks(ax2Ticks)
#        ax2.set_xbound(ax1.get_xbound())
#        ax2.set_xticklabels(tick_function(ax2Ticks))
#        ax2.set_xlabel("E vs. Hg/Hg$_2$SO$_4$ / V")

    #axis labels
    ax1.set_xlabel("retention time / min")
    ax1.set_ylabel("intensity / a.u.")

    #defines size of padding, important for legend on top, possibility to change space between subplots once implemented
    lpad = plot_settings['l_pad'] if plot_settings['l_pad'] else 0.15
    rpad = plot_settings['r_pad'] if plot_settings['r_pad'] else 0.15
    tpad = plot_settings['top_pad'] if plot_settings['top_pad'] else 0.10
    bpad = plot_settings['bottom_pad'] if plot_settings['bottom_pad'] else 0.15
    # wspace = pt.wspace[r1] if is_set(pt.wspace[r1]) else 0.12
    # hspace = pt.hspace[r1] if is_set(pt.hspace[r1]) else 0.12

    fig.subplots_adjust(left=lpad, right=1 - rpad, top=1 - tpad, bottom=bpad) # hspace=hspace, wspace=wspace)

    #safes figure as png and pdf
    if plot_settings['safeplot']:
        plt.savefig(plot_settings['plotname']+'.png', dpi=800, bbox_inches='tight')
        plt.savefig(plot_settings['plotname']+'.pdf', dpi=400, bbox_inches='tight')
    plt.show()

doplot(input_settings=input_settings, legend_settings=legend_settings, annotation_settings=annotation_settings, general_info=general_info)
