# -*- coding: utf-8 -*-
"""
Created on Tue Oct  18 19:25:46 2016

@author: Anna

Working part of the data plotting programme, that contains all the functions
"""
import numpy as np
import matplotlib.pyplot as plt

from pandas import DataFrame
import pandas as pd
from anna_data_plot_input_original import e_rhe_ref, ph_ref, ph

import Data_Importing
import EC


# def import_data(datatype, filenames, general_info):
#     if datatype == "cv":
#         extract_cv_data(filenames, general_info)
#     else:
#         print("Error: plottype not available. Please check plottype")

def find_deltaI_DLcapacitance(e_vs_rhe, i_mApscm, e_range, file):
    #print(e_vs_rhe.index(max(e_vs_rhe)))

    #divide CV into oxizing and reducing half
    ox_part = DataFrame(data=[e_vs_rhe[:e_vs_rhe.index(max(e_vs_rhe))], i_mApscm[:e_vs_rhe.index(max(e_vs_rhe))]],
                        index=["EvsRHE", "imA/cm^2"]).transpose()
    red_part = DataFrame(data=[e_vs_rhe[e_vs_rhe.index(max(e_vs_rhe)):], i_mApscm[e_vs_rhe.index(max(e_vs_rhe)):]],
                         index=["EvsRHE", "imA/cm^2"]).transpose()

    #find indices corresponding to the selected e-range
    #print(e_range)
    ox_current=[]
    for eachvalue in ox_part.itertuples():
        if e_range[0]<= eachvalue[1] and e_range[1] >= eachvalue[1]:
           ox_current.append(eachvalue[2])
    #print(ox_current)
    red_current=[]
    for eachvalue in red_part.itertuples():
        if e_range[0] <= eachvalue[1] and e_range[1] >= eachvalue[1]:
            red_current.append(eachvalue[2])
    #print(red_current)
    #print(file)
    delta_i=np.mean(ox_current)-np.mean(red_current)
    print(str(file)+": The difference between oxidation and reduction current in the potential region " +str(e_range) + " = " + str(delta_i) +
          " mA/cm2")





#def import_data_from(file):
#    """opens file and extracts information about the number of header lines as
#        given in the second row, then removes headerlines accordingly, and
#        returns data as array
#    """
#    if ".mpt" in file:
#        with open(file) as file:
#            for line in file:
#                if "header" in line:
#                    headernumber = int(line[line.find(": ") + 2:])
#                    break
#            #load the columns containing data and converting them to rows
#            data = pd.read_table(file, skiprows=headernumber-3, decimal=',')
#    else:
#        with open(file) as file:
#            data = pd.read_table(file, decimal=',')
#    return data

def import_data_from(file):
    """opens file by using Scott's set of function from EC-MS package, to make 
    imported data compatible with his functions.
    file is then converted to form that can be used by standard functions for plotting here.
    PLENTY TO DO HERE!!!
    """
    import_data(file, verbose)

    data=DataDict


    # if ".mpt" in file:
    #     with open(file) as file:
    #         for line in file:
    #             if "header" in line:
    #                 headernumber = int(line[line.find(": ") + 2:])
    #                 break
    #         #load the columns containing data and converting them to rows
    #         data = pd.read_table(file, skiprows=headernumber-3, decimal=',')
    # else:
    #     with open(file) as file:
    #         data = pd.read_table(file, decimal=',')
    return data


# def import_data(full_path_name='current', title='get_from_file',
#                 data_type='EC', N_blank=10, verbose=1):
#     file_lines = import_text(full_path_name, verbose)
#     DataDict = text_to_data(file_lines, title, data_type, N_blank, verbose)
#     DataDict = numerize(DataDict)
#
#     return DataDict


#def function(value):
#        new_value = value+5
#        return new_value


def convert_potential_to_rhe(e_ref):
    """
    Converts potential vs reference electrode to potential vs RHE
    using parameters defined in the settings
    :param e_ref: measured potential from data(frame)
    :return: e_rhe: potential vs RHE
    """
    e_nhe = - e_rhe_ref - 0.059 * ph_ref  # potential vs NHE
    e_rhe = e_ref + e_nhe + 0.059 * ph
    print("Potential converted to RHE scale at pH=" + ph)
    return e_rhe

def ohmicdrop_correct_e(data, ohmicdrop):
    """
    Corrects for the Ohmic drop in the setup
    :param e_rhe: potential vs RHE, ohmicdrop: ohmic resistance of the setup (in Ohms)
    :return: e_rhe_corr
    """
    e_rhe = data['Ewe/V']
    I = data['<I>/mA']
    #print(e_rhe, I)
    #from anna_data_plot_input_original import ohmicdrop
    e_rhe_corr = e_rhe - I/1000 * ohmicdrop
   #print(e_rhe_corr)
    print("Data has been corrected for an ohmic drop of" + ohmicdrop)
    return e_rhe_corr


def convert_to_current_density(I, general_info, filename):
    """
    Converts current into current density using the electrode surface area given in the settings
    TODO: possibility to choose "real" or electrochemically active surface area
    :param I: measured current from data(frame)
    :return: current density
    """
#    from anna_data_plot_input_original import electrode_area_geom
    if filename in general_info.value['electrode_area_geom_special']:
        i=I/general_info.value['electrode_area_geom_special'][filename]
        print("Current for file: " + filename + " has been normalized to an area of " + electrode_area_geom_special)
    else:    
        i = I/general_info.value['electrode_area_geom']
        print("Current has been normalized to an area of " + electrode_area_geom)
    return i


#collect relevant data for plotting CVs in a DataFrame
def extract_cv_data(folder_path, filenames, data_label, folders, general_info):
    """
    Extracts dataframes containing potential and current from multiple dataframes, calculates potential vs RHE and current density using functions
     and stores it in a dataframe, to be accessible for plotting
    :return: cv_data: List of Databases with information about the experiment: filename (string), scanrate (float), E vs ref, E vs RHE
     and I and i (Dataframe), label for plot (string)
    """
    cv_data = []
    #cv_data = {}

    for folder, files in filenames.items():
        for filename in files: #additional for loop to go through list of filenames

            if folder in folders:
                # print(folder)
                # filepath = folder
                filepath = folder_path + "/" + folder + "/" + filename
                if filename in data_label:
                    label = data_label[filename]
                else:
                    label = filename[filename.find("Pd"): filename.find("_CVA")] + filename[filename.find('_cy'):filename.find('.')]

                extracted_e_and_i = DataFrame(import_data_from(filepath)[['Ewe/V', '<I>/mA']])

                                #print(general_info.value['ohm_drop_corr'])

                if general_info.value['ohm_drop_corr']:
                    if filename in general_info.value['ohmicdrop_filename']:
                        ohmicdrop = general_info.value['ohmicdrop_filename'][filename]
                    else:
                        ohmicdrop = general_info.value['ohmicdrop']
                    print(ohmicdrop)
                    ohmicdropcorrected_e = DataFrame(data = [extracted_e_and_i.apply(ohmicdrop_correct_e, axis=1, ohmicdrop=ohmicdrop)],
                                                    index = ['E_corr/V']).T
                    #print(ohmicdropcorrected_e)
                    converted_e_and_i = DataFrame(data=[ohmicdropcorrected_e['E_corr/V'].apply(convert_potential_to_rhe),
                                                        extracted_e_and_i['<I>/mA'].apply(convert_to_current_density, general_info=general_info, filename=filename)],
                                                  index=["EvsRHE/V", "i/mAcm^-2"])
                else:
                    converted_e_and_i = DataFrame(data = [extracted_e_and_i['Ewe/V'].apply(convert_potential_to_rhe),
                                              extracted_e_and_i['<I>/mA'].apply(convert_to_current_density, general_info=general_info, filename=filename)],
                                              index = ["EvsRHE/V", "i/mAcm^-2"]) #this part should be simplified
                e_and_i = extracted_e_and_i.add(converted_e_and_i.T, fill_value=0)

               #cv_data[filename] = {'scanrate': find_scanrate(filepath), 'data': e_and_i, 'label': label}
               # cv_data.append({'filename':filename, 'scanrate': find_scanrate(filepath), 'data': e_and_i, 'label': label})
                cv_data.append({'filename': filename, 'data': e_and_i, 'label': label})
    return cv_data

#collect relevant data for plotting chronoamperometry data in a DataFrame
def extract_ca_data(folder_path, filenames, data_label, folders, general_info):
    """
    Extracts dataframes containing potential and current from multiple dataframes, calculates potential vs RHE and current density using functions
     and stores it in a dataframe, to be accessible for plotting
    :return: ca_data: List of Dictionaries with information about the experiment: filename (string), scanrate (float), E vs ref, E vs RHE
     and I and i (Dataframe), label for plot (string)
    """
    #ca_data = {}
    ca_data = []
    for folder, files in filenames.items():
        for filename in files: #additional for loop to go through list of filenames
            if folder in folders:
                # print(folder)
                # filepath = folder
                filepath = folder_path + "/" + folder + "/" + filename
                if filename in data_label:
                    label = data_label[filename]
                else:
                    label = filename[filename.find("Pd"): filename.find("_C0")] #+ filename[filename.find('_C')-5:filename.find('_C')-2]

                extracted_t_and_i = DataFrame(import_data_from(filepath)[['time/s', '<I>/mA', '(Q-Qo)/C', 'Ewe/V']])
                converted_i = DataFrame(data = [extracted_t_and_i['<I>/mA'].apply(convert_to_current_density, general_info=general_info, filename=filename)],
                                              index = ["i/mAcm^-2"]) #this part should be simplified
                
                if extracted_t_and_i['time/s'].ix[0] >= 20 and not filename in general_info.value['no_timezero']:
                    extracted_t_and_i['time/s'] = extracted_t_and_i['time/s'] - extracted_t_and_i['time/s'].ix[0]
                 
                   
                if filename in general_info.value['ohmicdrop_filename']:
                   ohmicdrop = general_info.value['ohmicdrop_filename'][filename]
                else:
                   ohmicdrop = general_info.value['ohmicdrop']
                #print(ohmicdrop)
                ohm_drop_corrected_e = DataFrame(data = [extracted_t_and_i.apply(ohmicdrop_correct_e, axis=1,ohmicdrop=ohmicdrop).apply(convert_potential_to_rhe)],
                                             index=['E_corr/V']).T
                #print(ohm_drop_corrected_e.T)
                t_and_i = extracted_t_and_i.add(converted_i.T, fill_value=0)
                #print(t_and_i)
                t_and_i_and_u = t_and_i.add(ohm_drop_corrected_e, fill_value=0)
                #print(t_and_i_and_u)
                #ca_data[filename]= {'potential': find_set_potential(filepath), 'data': t_and_i, 'label': label}
                if ".mpt" in filename:
                    ca_data.append(
                    {'filename': filename, 'potential': find_set_potential(filepath), 'data': t_and_i_and_u, 'label': label})
                else:
                    ca_data.append(
                        {'filename': filename, 'data': t_and_i_and_u,'label': label})
#    print(ca_data)
    return ca_data


def find_scanrate(file):
    """finds scanrate in header and saves in a float
    """
    with open(file) as file:
       for line in file:
           if "dE/dt" in line and not "dE/dt unit" in line:
               scanrate = float(line[line.find("dE/dt")+16:])
               #print(scanrate)
               break
    return scanrate

def find_set_potential(file):
    """finds set potential in header, converts to E vs RHE and saves in a float
    """
    with open(file) as file:
       for line in file:
           if "Ei (V)" in line and not "dE/dt unit" in line:
               e_vs_ref = float(line[line.find("Ei (V)")+14:].replace(',','.'))
               e_vs_rhe = convert_potential_to_rhe(e_vs_ref)
               print(e_vs_ref, e_vs_rhe)
               break
    return e_vs_rhe

def cv_plot(cv_data, plot_settings, legend_settings, annotation_settings): #basically all the details that are chosen in the settings part go into this function
    """plot tuples of current/voltage
    main function of the program
    input: settings from anna_data_plot_settings through doplot function
    output: cv_plot
    """
    #print CV data for check
    #print(cv_data)



    # prepare for figure with 2 x-axes
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    #List of 6 different linestyles to loop through
    # linestyle_list= ['-', (0, (2, 3)), '--', (3, (15, 7.5)) ,'-.',':', '-', (0, (2, 3)), '--', (3, (15, 7.5)),'-.',':',
    #                  '-', (0, (2, 3)), '--', (3, (15, 7.5)), '-.', ':','-', (0, (2, 3)), '--', (3, (15, 7.5)) ,'-.',':']
    linestyle_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#    linestyle_list = [ ':', ':', ':', ':', ':', '-', '-', '-', '-', '-', '-']
    color_list = ['g', 'orange', 'r', 'b', 'k', 'g', 'orange', 'r', 'b', 'k', 'c', 'm', '0.50',"#538612", '0.75','orange', 'g', 'r', 'b', 'k', 'c', 'm', '0.50',"#538612", '0.75']
    #color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
    #color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
    #print(color_list)
    i=-1
    j=-1

    for each_cv in cv_data:
        if i <= 11:
            i = i+1
        else: 
            i = 0
        j = j +1
        x = cv_data[j]['data']['EvsRHE/V'].values.tolist()
        y = cv_data[j]['data']['i/mAcm^-2'].values.tolist()
        #print(x,y)
        print(i)
        plt.plot(x, y, color=color_list[i], linestyle = linestyle_list[i], label=cv_data[j]['label'])
        # find and print the difference in current in the double layer capacitance region
        current_file=cv_data[j]['filename']
        e_range = annotation_settings['e_range']
        find_deltaI_DLcapacitance(e_vs_rhe=x, i_mApscm=y, e_range=e_range, file=current_file)


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

        def tick_function(e_rhe):
            e_nhe = - e_rhe_ref - 0.059 * ph_ref  # potential vs NHE
            e_ref = e_rhe - e_nhe - 0.059 * ph
            return ["%.2f" % z for z in e_ref]

        ax2.set_xticks(ax2Ticks)
        ax2.set_xbound(ax1.get_xbound())
        ax2.set_xticklabels(tick_function(ax2Ticks))
        ax2.set_xlabel("E vs. Hg/Hg$_2$SO$_4$ / V")

    #axis labels
    ax1.set_xlabel("E vs. RHE / V")
    ax1.set_ylabel("i / mA cm$^{-2}$")

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
        plt.savefig(plot_settings['plotname']+'.png', dpi=400, bbox_inches='tight')
        plt.savefig(plot_settings['plotname']+'.pdf', dpi=400, bbox_inches='tight')
    plt.show()

def ca_plot(ca_data, plot_settings, legend_settings, annotation_settings): #basically all the details that are chosen in the settings part go into this function
    """plot tuples of current/time
    input: settings from anna_data_plot_settings through doplot function
    output: ca_plot
    """
    # prepare for figure with 2 x-axes, not really necessary, but also opens possibilty for subplots
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    if plot_settings['coplot_evsrhe']:
        ax2 = ax1.twinx() #adds second y axis with the same x-axis

    #List of 6 different linestyles to loop through
    #linestyle_list = ['-', '-', '--','--', '-.','-.', ':', ':', (0, (2, 3)), (0, (2, 3)),  (3, (10, 5)),  (3, (10, 5))]
    #color_list = ['orange', 'orange', 'g', 'g', 'r', 'r', 'b', 'b', 'k', 'k', 'c', 'c']

#    linestyle_list = ['-', '--', '-.', ':', (0, (2, 3)), (3, (10, 5))]
    linestyle_list = ['-', '-', '-', '-', '-', '-']
    color_list = ['orange','g', 'r', 'b', 'k', 'c']

    i=-1
    j=-1

    for each_ca in ca_data:
        if i <= 10: i = i+1
        else: i=0
        j = j+1

        x = ca_data[j]['data'][['time/s']].values.tolist()
        #x = ca_data[each_ca]['data'][['time/s']].values.tolist()
        y = ca_data[j]['data'][['i/mAcm^-2']].values.tolist()
        #y = ca_data[each_ca]['data'][['i/mAcm^-2']].values.tolist()
        #print(x,y)
        #print(i)
        ax1.plot(x, y, color=color_list[i], linestyle = linestyle_list[i], label=ca_data[j]['label'])
        if plot_settings['coplot_evsrhe']:
            y2 = ca_data[j]['data'][['E_corr/V']].values.tolist()
            ax2.plot(x, y2, color=color_list[i], linestyle=linestyle_list[i+1], label=ca_data[j]['label']+'_E_corr')

    #set axis limits according to info given in settings
    ax1.set_xlim(plot_settings['x_lim'])
    ax1.set_ylim(plot_settings['y_lim'])
    

    #create legend according to settings
    ax1.legend(fontsize=legend_settings["fontsize"], loc=legend_settings["position"], ncol=legend_settings["number_of_cols"])

    #grid
    if plot_settings['grid']:
        ax1.grid(True)

    #axis labels
    ax1.set_xlabel("time / s")
    ax1.set_ylabel("i / mA cm$^{-2}$")
    
    
    #settings for 2nd axis if chosen
    if plot_settings['coplot_evsrhe']:
        ax2.set_ylim(plot_settings['y2_lim'])
        ax2.set_ylabel("E_corr vs. RHE / V")
        

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
        plt.savefig(plot_settings['plotname']+'.png', dpi=400, bbox_inches='tight')
        plt.savefig(plot_settings['plotname']+'.pdf', dpi=400, bbox_inches='tight')
    plt.show()




def doplot(plottype, folder_path, filenames, folders, data_label, plot_settings, legend_settings, annotation_settings, general_info):
    """
    Chooses what kind of plot to do and refers to that function
    :param plottype: kind of plot to do
    :return: plot
    """
    if plottype == "cv":
        cv_plot(cv_data = extract_cv_data(folder_path=folder_path, filenames = filenames, folders=folders, data_label=data_label, general_info = general_info), plot_settings=plot_settings,
                legend_settings=legend_settings, annotation_settings=annotation_settings )

    if plottype == "ca":
        ca_plot(ca_data = extract_ca_data(folder_path=folder_path, filenames = filenames, folders=folders, data_label=data_label, general_info=general_info), plot_settings=plot_settings,
                legend_settings=legend_settings, annotation_settings=annotation_settings )



