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

load_new_data = True #False if saved set of data files should be used.
input_plot_settings = True #False if saved settings for plot (size, colours etc.) should be used.
savesettings = False #True if the new input settings should be saved.

# general information  if applicable, otherwise comment
# temperature
temperature = 25  # C

# reference electrode
e_rhe_ref = -0.7240  # V
ph_ref = 1.2

# electrolyte
info = "0.1 M HClO_{4}"  # to be printed in annotations (not implemented)
ph = 1.2

# electrode area in cm2
electrode_area_geom = 2  # cm2
electrode_area_ecsa = 1  # cm2

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

    folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Pd electrodes\EC and product analysis'

    folders = ['20171005_Pd_049',
               # '20170901_Pd_040',
               # '20170831_Pd_039',
               # '20170916_Pd_046',
               # '20171003_Pd_047',
               # '20171003_Pd_048',
               '20171006_Pd_050',
               '20171010_Pd_051',
               '20171011_Pd_052'
    ]  # list of folders from which data is going to be plotted

    filenames = {'20171005_Pd_049': [#'20171005_AW_Pd049_2ndtry_04_CVA_C01.mpt',
                                     # '20171005_AW_Pd049_3rd_onlyAr_04_CVA_C01.mpt',
                                     '20171005_AW_Pd049_2ndtry_05_CVA_C01.mpt',
                                     # '20171005_AW_Pd049_2ndtry_07_CA_C01.mpt',
                                     # '20171005_AW_Pd049_3rd_onlyAr_01_CA_C01.mpt',
                                     # '20171005_AW_Pd049_3rd_onlyAr_06_CA_C01.mpt',
                                     # '20171005_AW_Pd049_02_CA_C01.mpt',
                                     # '20171005_AW_Pd049_2ndtry_06_CA_C01.mpt'
                                     ],
                 '20171006_Pd_050': [#'20171006_AW_Pd050_onlyAr_restart_02_CA_C01.mpt',
                                     # '20171006_AW_Pd050_onlyAr_restart_03_CA_C01.mpt',
                                     #'20171006_AW_Pd050_onlyAr_02_CA_C01.mpt',
                                     #'20171006_AW_Pd050_onlyAr_04_CVA_C01.mpt',
                                     '20171006_AW_Pd050_onlyAr_05_CVA_C01.mpt'
                                     ],
                 '20171010_Pd_051': [#'20171010_AW_Pd051_06_CA_C01.mpt',
                                     # '20171010_AW_Pd051_08_CVA_C01.mpt',
                                     # '20171010_AW_Pd051_02_CA_C01.mpt',
                                     # '20171010_AW_Pd051_04_CVA_C01.mpt',
                                     '20171010_AW_Pd051_05_CVA_C01.mpt'
                                     ],
                 '20171003_Pd_048': ['20171003_AW_Pd048_COstripping_test_04_CVA_C01.mpt',
                                     '20171003_AW_Pd048_COstripping_test_02_CVA_C01.mpt',
                                     '20171003_AW_Pd048_COstripping_test_05_CVA_C01.mpt'
                                     ],
                 '20171011_Pd_052': [#'20171011_AW_Pd_052_2ndgo_08_CVA_C01.mpt',
                                     # '20171011_AW_Pd_052_2ndgo_06_CA_C01.mpt',
                                     # '20171011_AW_Pd_052_2ndgo_07_CA_C01.mpt',
                                     '20171011_AW_Pd_052_2ndgo_05_CVA_C01.mpt',
                                     # '20171011_AW_Pd_052_2ndgo_04_CVA_C01.mpt',
                                     # '20171011_AW_Pd_052_2ndgo_01_SPEIS_C01.mpt',
                                     # '20171011_AW_Pd_052_2ndgo_02_CA_C01.mpt'
                                     ]

    }

    # custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
    #electrode area (geom and ecsa), ohmic drop to correct for

    filespec_settings = {'20171005_AW_Pd049_2ndtry_05_CVA_C01.mpt':{'label': "Pd_049 CO-strip",
                                                     'cycles to extract': [1],
                                                     'electrode area geom': 2, 'electrode area ecsa': 97.9},
                         '20171006_AW_Pd050_onlyAr_05_CVA_C01.mpt': {'label': "Pd_050 CO-strip",
                                                                     'cycles to extract': [1],
                                                                     'electrode area geom': 2,
                                                                     'electrode area ecsa': 55.1},
                         '20171010_AW_Pd051_05_CVA_C01.mpt':{'label': "Pd_051 CO-strip",
                                                                     'cycles to extract': [1],
                                                                     'electrode area geom': 2,
                                                                    'electrode area ecsa': 83.5},
                         '20171011_AW_Pd_052_2ndgo_05_CVA_C01.mpt':{'label': "Pd_052 CO-strip",
                                                                     'cycles to extract': [1],
                                                                     'electrode area geom': 2,
                                                                    'electrode area ecsa': 78.9
                                                                    }
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
    # settings for the plot
    plot_settings = {'safeplot': False,
                     'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                     'grid': True,
                     'second axis':  False,
                     'x_lim': (0.2, 1.6),
                     'y_lim': (-3, 2),
                     'y2_lim': (0.6, 2.6),
                     'top_pad': 0.2,
                     'bottom_pad': 0.1,
                     'l_pad': [],
                     'r_pad': [],
                     'colors': ['r', 'orange','g', 'r', 'b', 'k', 'g', 'orange', 'r', 'b', 'k', 'c', 'm', '0.50',"#538612", '0.75'],
                     'linestyle': ['-', '--'],
                     'colors2': ['k', 'grey'],
                     'linestyle2': ['-','--'],
                     # color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
                     # color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
                     #options to select which data is plotted
                     'plot type': "cv", #possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
                     #custom column selection, will overrule plottype, if given. Possibilities are all data column names,
                     #most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
                     # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
                     'x_data':"",
                     'y_data':"",
                     'x_data2':"", #not implemented yet
                     "y_data2":""
                     }

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
            json.dump(data_load_settings, f)

# todo: subplot possibility


def main():
    # f load_new_settings:
    #create list of data dictionaries for plotting
        #loop through datafiles
        #import data
    # list of dictionaries for each file/loop that was chosen to be plotted, each containing filename(+cycle), DataFrame of all extracted data (all data columns), and file specific settings (unaltered) as given in input as "settings".
    #actual data in form of DataFrame for further treatment with the functions from data plot. if sync metadata is to be implemented the conversion has to be moved to later stage
    datalist = dpf.extract_data(folder_path, filenames, folders, filespec_settings)
    # print(datalist)
    print("Data extraction finished.")

    # #treat data (now functions from data plot, future sync metadate from EC_MS package?, also depending of data-type)
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


    #Calculate ESCA from a list of 2 data dictionaries (all further items in the list will be disregarded).
    esca_data = dpf.calc_esca(datalist[0:4], type='oxide_red')
    print(esca_data)

    # esca_data=[] #uncomment if no calculation of esca to avoid error in EC_plot
    #plot the data from the list of data dictionaries
    # print(datalist)
    esca_data=[]
    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr, esca_data)

    # try:
    # except IndexError:

    print("FINISHED")

if __name__ == "__main__":
    main()



