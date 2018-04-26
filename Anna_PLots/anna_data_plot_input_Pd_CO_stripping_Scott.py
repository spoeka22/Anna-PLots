# -*- coding: utf-8 -*-
"""
Created on Tue Oct  18 19:25:46 2016

@author: Anna

Plotting of CV and CA data recorded with EC-lab and safed as .mpt file

Settings for the data to plot are inserted here. The data plotting is done using functions stored in anna_data_plot_functions.
"""

from pandas import DataFrame
import anna_data_plot_functions as dpf
import json
from collections import OrderedDict
import matplotlib as plt
import numpy as np

load_new_data = True #False if saved set of data files should be used.
input_plot_settings = True #False if saved settings for plot (size, colours etc.) should be used.
savesettings = False #True if the new input settings should be saved.

# general information  if applicable, otherwise comment
# temperature
temperature = 25  # C

# reference electrode
e_rhe_ref = -0.685  # V #new:-0.724, pH=1.2
ph_ref = 0

# electrolyte
info = "1 M HClO_{4}"  # to be printed in annotations (not implemented)
ph = 0

# electrode area in cm2
electrode_area_geom = 0.196349541# cm2
electrode_area_ecsa = 0.196349541  # cm2 flat electrode per definition

# ohmic drop in Ohm over cell measured with EIS
ohm_drop_corr = False  # to turn on/off ohmic drop correction
ohmicdrop = 50

# insert filename in list if starting time is notzero, AND should be plotted as nonzero (ie NOT BE CHANGED)
no_timezero = {}

if not load_new_data:
    settings_file = 'import_settings/' + input("Enter the name of the file containing data path and settings: ")
    with open(settings_file) as f:
        data_load_settings = json.load(f)
    print(data_load_settings)
    folder_path = data_load_settings[0]
    folders = data_load_settings[1]
    filenames = data_load_settings[2]
    filespec_settings = data_load_settings[3]

elif load_new_data:
    #folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Au electrodes'
    folder_path = r'\\dtu-storage\annawi\Desktop\Projects\Propene oxidation\Experiments\Pd-electrodes\CO-stripping on stub'
    # folder_path = r'\\dtu-storage\annawi\Desktop\Projects\Propene oxidation\Experiments\Pd-electrodes\Systematic Study NovDec2017'

    OrderedDict([("ub\\Scott's data", ['02_cycles_02_CVA.mpt'])])

    folders = ["Scott's data"
    ]  # list of folders from which data is going to be plotted

    filenames = OrderedDict([("Scott's data", ['02_cycles_02_CVA.mpt'])

    ])




    # custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
    #electrode area (geom and ecsa), ohmic drop to correct for

    filespec_settings = {
                        '02_cycles_02_CVA.mpt': {'label': "CO strip pc Pd",
                                                               'cycles to extract': [24,25],
                                                               'electrode area geom': 0.196349541,
                                                               'electrode area ecsa': 0.196349541,
                                                               # 'individual ohmicdrop': 43.3
                                                           },

                         }
    if savesettings:
        data_load_settings = [folder_path, folders, filenames, filespec_settings]

        save_settings_as = input("Save data input settings as ([...]_input.txt): ") + "_input.txt"
        with open('import_settings/'+save_settings_as, 'w') as f:
            json.dump(data_load_settings, f)

#TODO: automatically detect which is the CO strip and the reference cycle based on the potential holde period in the cycle??

if not input_plot_settings:
    plotsettings_file = 'plot_settings/'+ input("Enter the name of the settings file for the plot: ")
    with open(plotsettings_file) as f:
        plot_load_settings = json.load(f)
    print(plot_load_settings)
    plot_settings = plot_load_settings[0]
    legend_settings = plot_load_settings[1]
    annotation_settings = plot_load_settings[2]

else:
    # settings for the plot - CV settings
    plot_settings = {'safeplot': True,
                     'plotname': "20180425_CV_pcPd_COstrip_50mVps",
                     'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                     'grid': False,
                     'second axis':  False,
                     'x_lim': (0.2, 1.5),
                     'y_lim': (-0.6, 0.5),
                     'y_logscale': False,
                     'y2_lim': (0, 0.025),
                     'top_pad': 0.2,
                     'bottom_pad': 0.1,
                     'l_pad': [],
                     'r_pad': [],
                     'colors': ['0.25',[0.03137255, 0.20853518, 0.4497501, 1.], 'b', 'grey','k', 'r', '#4a235a', 'c', '#538612', 'c', 'm', '0.50',"#538612", '0.75'],
                     # 'colors': [ '#bd4de0' , 'k', 'orange', 'g', 'b', 'r', '#d816ff', "#ff8a16"],
                     # 'colors': ['#bd4de0', 'k', '#6b12ad', 'g', '#266f0e', 'grey'],
                     # 'colors': ['#bd4de0', 'orange', '#d816ff', "#ff8a16"],
                     'linestyle': ['-', '-'],
                     'colors2': ['0.25', 'grey', '0.75'],
                     'linestyle2': ['--','--','--'],
                     # color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
                     # color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
                     #options to select which data is plotted
                     'plot type': "cv", #possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
                     #custom column selection, will overrule plottype, if given. Possibilities are all data column names,
                     #most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
                     # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
                     'x_data':"EvsRHE/V",
                     'y_data':"i/mAcm^-2_geom",
                     'x_data2':"", #not implemented yet
                     "y_data2":"",
                     "aspect": 0.95,
                     "axis label size": 16,
                     "tick label size": 14
                     }

    #settings for the plot - CA settings
    # plot_settings = {'safeplot': False,
    #                  'plotname': "20180413_Comparison_095V_foamvsfoil",
    #                  'coplot_evsrhe': False,
    #                  # for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
    #                  'grid': False,
    #                  'second axis': False,
    #                  'x_lim': (-10, 3700),
    #                  'y_lim': (-0.1, 10),
    #                  'y_logscale': False,
    #                  'y2_lim': (0, 0.025),
    #                  'top_pad': 0.2,
    #                  'bottom_pad': 0.15,
    #                  'l_pad': 0.2,
    #                  'r_pad': [],
    #                  'colors': ['g', 'b', 'grey', 'orange', 'r', '#4a235a', 'k', 'c', '#538612', 'c', 'm', '0.50',
    #                             "#538612", '0.75'],
    #                  # 'colors': [ '#bd4de0' , 'k', 'orange', 'g', 'b', 'r', '#d816ff', "#ff8a16"],
    #                  # 'colors': ['#bd4de0', '#6b12ad', #purple
    #                  #            'grey', 'k',
    #                  #            'g', '#266f0e'
    #                  #            ],
    #                  # 'colors': ['#bd4de0', 'orange', '#d816ff', "#ff8a16"],
    #                  # 'colors': plt.cm.gist_earth(range(255, 10, 10)),
    #                  # 'colors': #plt.cm.Blues([50,100,150,200,250,255]),
    #                  #         [
    #                  #          [0.10249904, 0.40868897, 0.68289121, 1.],  #0.9 73
    #                  #          # [0.59215688, 0.77708575, 0.87643215, 1.],  #0.8 76
    #                  #          # [0.03137255, 0.20853518, 0.4497501, 1.],  # 1.0 78
    #                  #
    #                  #          # [0.03137255, 0.1882353, 0.41960785, 1.],
    #                  #
    #                  #          [0.30611305, 0.60484431, 0.79492504, 1.],   #0.85 85
    #                  #          # "grey",  #Ar #0.9 Ar 107
    #                  #          [0.81707037, 0.88589005, 0.95078816, 1.], #0.7 112
    #                  #          [0.03137255, 0.1882353, 0.41960785, 1.],  # 0.95 115
    #                  #             #1.1 118 (missing!!)
    #                  #          [0, 0, 0, 1.],  #black 1.2 119
    #                  #
    #                  #          ],
    #
    #
    #                  # 'linestyle': ['-', '-','-', '-','-', '-','-', '-'],
    #                  'linestyle': ['-', '-', '--', '-', '-', '-', '-', '-'],
    #                  'colors2': ['0.25', 'grey', '0.75'],
    #                  'linestyle2': ['--', '--', '--'],
    #                  # color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
    #                  # color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
    #
    #                  # options to select which data is plotted
    #                  'plot type': "ca",
    #                  # possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
    #                  # custom column selection, will overrule plottype, if given. Possibilities are all data column names,
    #                  # most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
    #                  # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
    #                  'x_data': "time/s",
    #                  # 'y_data': "<I>/mA",
    #                  'y_data': "i/mAcm^-2_ECSA",
    #                  'x_data2': "",  # not implemented yet
    #                  "y_data2": "",
    #                  # "aspect": 100,
    #                  "axis label size": 16,
    #                  "tick label size": 14
    #                  }
    #

    # legend:
    legend_settings = {'position1': (0, 1.05),
                       'position2': (0, -0.2), #position of the legend for the second y axis
                       'number_of_cols': 2,
                       'fontsize': 8
                       }

    # annotations: dictionary of annotation plus relevant properties in list form CURRENTLY NOT USED!?!?
    annotation_settings = {'annotation 1': ["scanrate"],
                           #E-range for finding the delta i in the capacitance region for estimation of surface area
                           'e_range': [0.99, 1.01] #works only if scan starts at lowest potential
                           }

    if savesettings:
        plot_load_settings = [plot_settings, legend_settings, annotation_settings]

        save_plotsettings_as = 'plot_settings/'+input("Save plot settings as ([...]_plot_settings.txt): ") + "_plot_settings.txt"
        with open(save_plotsettings_as, 'w') as f:
            json.dump(plot_load_settings, f)

# todo: subplot possibility


def main():
    # f load_new_settings:
    #create list of data dictionaries for plotting
        #loop through datafiles
        #import data
    # list of dictionaries for each file/loop that was chosen to be plotted, each containing filename(+cycle), DataFrame of all extracted data (all data columns), and file specific settings (unaltered) as given in input as "settings".
    #actual data in form of DataFrame for further treatment with the functions from data plot. if sync metadata is to be implemented the conversion has to be moved to later stage

    # print(folder_path)
    # print(filenames)
    # print(folders)
    # print(filespec_settings)
    datalist = dpf.extract_data(folder_path, filenames, folders, filespec_settings)
    # print(datalist)
    print("Data extraction finished.")

    # #treat data (now functions from data plot, future sync metadata from EC_MS package?, also depending of data-type)
    for file in datalist:
        #ohmic drop correction
        if ohm_drop_corr:
            print("Carrying out ohmic drop correction")
            file['data'] = file['data'].add(dpf.ohmicdrop_correct_e(file, ohmicdrop), fill_value=0)
            # print(file['data'])

        #conversion to rhe scale TODO: make it possible to choose pH and reference individually!
        file['data'] = file['data'].add(DataFrame([dpf.convert_potential_to_rhe(file['data']['Ewe/V'], e_rhe_ref=e_rhe_ref, ph_ref=ph_ref, ph=ph)],
                                                  index=['EvsRHE/V']).T, fill_value=0)
        if ohm_drop_corr:
            file['data'] = file['data'].add(DataFrame([dpf.convert_potential_to_rhe(file['data']['E_corr/V'], e_rhe_ref=e_rhe_ref, ph_ref=ph_ref, ph=ph)],
                                                      index=['E_corr_vsRHE/V']).T, fill_value=0)
        # print(file['data'])
        # print(file['filename'])

        #conversion to current density
        file['data'] = file['data'].add(dpf.convert_to_current_density(file, electrode_area_geom, electrode_area_ecsa),
                                        fill_value=0)

        #set time at start of file to 0, if not 0 (and not selected in 'no_timezero'
        if file['data']['time/s'].ix[0] >= 20 and not file['filename'] in no_timezero:
            file['data']['time/s'] = file['data']['time/s'] - file['data']['time/s'].ix[0]
        # print(file['data']['time/s'])

        # TODO: update find and print the difference in current in the double layer capacitance region
        # current_file = cv_data[j]['filename']
        # e_range = annotation_settings['e_range']
        # find_deltaI_DLcapacitance(e_vs_rhe=x, i_mApscm=y, e_range=e_range, file=current_file)

     #TODO: find set potential in CA and print it/annotate it in plot


    #CALCULATE ESCA: type="CO_strip": difference between the first 2 cycles in list of data, rest of list is ignored.
    #type="oxide_red": finds oxide red charge and calculates ESCA with given charge_p_area for each item in list, also
    #plots the calculated data as bar chart
    esca_data = dpf.calc_esca(datalist[0:17], type='CO_strip', scanrate=20, charge_p_area=1, makeplot=False)
    # print(esca_data)



    #PLOT THE DATA FROM THE LIST OF DATA DICTIONARIES
    # esca_data=[] #uncomment if no calculation of esca to avoid error in EC_plot
    # print(datalist)
    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr, esca_data)
    #
    #PLOT THE CURRENT AT A GIVEN TIME AS A FUNCTION OF POTENTIAL
    # dpf.current_at_time_plot(datalist, times=[60, 600, 3300], I_col="i/mAcm^-2_ECSA")


    #INTEGRATE (find difference in Q-Qo) the first peak in a CA after a given starting time (assumed 0 if not given) and plot
    # currently as a function of electrode area as given in input file
    # dpf.integrate_cas(datalist, t_start=20, t_end=700, makeplot=True)

    #TEST of the select_data function:
    # print("Original" + str(datalist[0]))
    #
    # select_data_conditions={"EvsRHE/V": [lambda x: x > 0.4, lambda x: x <= 0.8],
    #                         "ox/red": [lambda x: x == 0]}
    # cut_dict=dpf.select_data(datalist[0], select_data_conditions)
    # print("cut" + str(cut_dict))
    # print(cut_dict["data"]["<I>/mA"].tail(1))
    print("FINISHED")

if __name__ == "__main__":
    main()



