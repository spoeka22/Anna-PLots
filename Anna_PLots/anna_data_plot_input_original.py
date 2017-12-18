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

load_new_data = True #False if saved set of data files should be used.
input_plot_settings = True #False if saved settings for plot (size, colours etc.) should be used.
savesettings = False #True if the new input settings should be saved.

# general information  if applicable, otherwise comment
# temperature
temperature = 25  # C

# reference electrode
e_rhe_ref = -0.721  # V #new:-0.724, pH=1.2
ph_ref = 1.14

# electrolyte
info = "0.1 M HClO_{4}"  # to be printed in annotations (not implemented)
ph = 1.14

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

    folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Pd electrodes\Systematic Study NovDec2017'

    folders = [ #'20171122_Pd_064',
                # '20171123_Pd_065',
                # '20171123_Pd_066'
                # '20171127_Pd_068b'
                # '20171203_Pd_069',
                # '20171203_Pd_070',
                '20171212_Pd_073',
                # '20171213_Pd_074',
                # '20171213_Pd_075',
                # '20171214_Pd_076',
                # '20171214_Pd_077',
                # '20171214_Pd_078'
    ]  # list of folders from which data is going to be plotted

    filenames = {'20171212_Pd_073': ['20171212_AW_Pd_073_02_CA_C01.mpt',
                                                  '20171212_AW_Pd_073_04_CA_C01.mpt',
                                                  '20171212_AW_Pd_073_05_CA_C01.mpt',
                                                  # '20171212_AW_Pd_073_SA_eval_04_CVA_C01.mpt'
                                                  ]}

    # filenames = OrderedDict([#('20171127_Pd_068b', ['20171127_Pd_068_b_02_CA_C01.mpt',
    #                                                # '20171127_Pd_068_b_04_CA_C01.mpt',
    #                                                # '20171127_Pd_068_b_05_CA_C01.mpt'
    #                                                # ]),
    #                          # ('20171203_Pd_069', ['20171203_Pd_069_02_CA_C01.mpt',
    #                          #                      '20171203_Pd_069_04_CA_C01.mpt',
    #                          #                      '20171203_Pd_069_05_CA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171203_Pd_070', ['20171203_Pd_070_02_CA_C01.mpt',
    #                          #                      '20171203_Pd_070_04_CA_C01.mpt',
    #                          #                      '20171203_Pd_070_05_CA_C01.mpt'
    #                          #                      ]),
    #                          ('20171212_Pd_073', ['20171212_AW_Pd_073_02_CA_C01.mpt',
    #                                               '20171212_AW_Pd_073_04_CA_C01.mpt',
    #                                               '20171212_AW_Pd_073_05_CA_C01.mpt',
    #                                               '20171212_AW_Pd_073_SA_eval_04_CVA_C01.mpt'
    #                                               ]),
    #                          ('20171214_Pd_076', ['20171214_AW_Pd_076_SA_eval_04_CVA_C01.mpt',
    #                                               '20171214_AW_Pd_076_02_CA_C01.mpt',
    #                                               '20171214_AW_Pd_076_04_CA_C01.mpt',
    #                                               '20171214_AW_Pd_076_05_CA_C01.mpt'
    #                                               ]),
    #                          ('20171213_Pd_074', ['20171213_AW_Pd_074_05_CA_C01.mpt',
    #                                               '20171213_AW_Pd_074_04_CA_C01.mpt',
    #                                               '20171213_AW_Pd_074_SA_eval_04_CVA_C01.mpt'
    #                                               ]),
    #                          ('20171213_Pd_075', ['20171213_AW_Pd_075_SA_eval_04_CVA_C01.mpt',
    #                                               '20171213_AW_Pd_075_05_CA_C01.mpt',
    #                                               '20171213_AW_Pd_075_04_CA_C01.mpt',
    #                                               '20171213_AW_Pd_075_02_CA_C01.mpt'
    #                                               ]),
    #                          ('20171214_Pd_077', ['20171214_AW_Pd_077_05_CA_C01.mpt',
    #                                               '20171214_AW_Pd_077_OCV_C01.mpt',
    #                                               '20171214_AW_Pd_077_04_CA_C01.mpt',
    #                                               '20171214_AW_Pd_077_SA_eval_05_OCV_C01.mpt',
    #                                               '20171214_AW_Pd_077_SA_eval_04_CVA_C01.mpt',
    #                                               '20171214_AW_Pd_077_02_CA_C01.mpt'
    #                                               ]),
    #                          ('20171214_Pd_078', ['20171214_AW_Pd_078_05_CA_C01.mpt',
    #                                               '20171214_AW_Pd_078_04_CA_C01.mpt',
    #                                               '20171214_AW_Pd_078_02_CA_C01.mpt',
    #                                               '20171214_AW_Pd_078_SA_eval_05_OCV_C01.mpt',
    #                                               '20171214_AW_Pd_078_SA_eval_04_CVA_C01.mpt'
    #                                               ]),
    #                          # ('20171114_Pd_054', ['20171114_Pd_054_06_CA_C01.mpt',
    #                          #                      '20171114_Pd_054_05_CA_C01.mpt',
    #                          #                      '20171114_Pd_054_04_CVA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171115_Pd_056', ['20171115_Pd_056_05_CA_C01.mpt',
    #                          #                      '20171115_Pd_056_06_CA_C01.mpt',
    #                          #                      '20171115_Pd_056_04_CVA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171116_Pd_057', ['20171116_Pd_057_05_CA_C01.mpt',
    #                          #                      '20171116_Pd_057_06_CA_C01.mpt',
    #                          #                      '20171116_Pd_057_04_CVA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171116_Pd_058', ['20171116_Pd_058_05_CA_C01.mpt',
    #                          #                      '20171116_Pd_058_06_CA_C01.mpt',
    #                          #                      '20171116_Pd_058_04_CVA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171116_Pd_059', ['20171116_Pd_059_05_CA_C01.mpt',
    #                          #                      '20171116_Pd_059_06_CA_C01.mpt',
    #                          #                      '20171116_Pd_059_04_CVA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171115_Pd_055', ['20171115_Pd_055_05_CA_C01.mpt',
    #                          #                      '20171115_Pd_055_06_CA_C01.mpt',
    #                          #                      '20171115_Pd_055_04_CVA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171122_Pd_064', ['20171122_Pd_064_05_CA_C01.mpt',
    #                          #                      '20171122_Pd_064_04_CA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171123_Pd_065', ['20171123_Pd_065_04_CA_C01.mpt',
    #                          #                      '20171123_Pd_065_05_CA_C01.mpt'
    #                          #                      ]),
    #                          # ('20171123_Pd_066', ['20171123_Pd_066_04_CA_C01.mpt',
    #                          #                      '20171123_Pd_066_05_CA_C01.mpt'
    #                          #                      ])
    #                          ])




    # custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
    #electrode area (geom and ecsa), ohmic drop to correct for

    filespec_settings = {'20171116_Pd_057_06_CA_C01.mpt': {'label': "1.325 V/RHE then 0.925 V/RHE (057)",
                                                     #'cycles to extract': [2],
                                                     'electrode area geom': 2, 'electrode area ecsa': 0,
                                                      #'individual ohmicdrop': 43.3
                                                    },
                         '20171116_Pd_058_06_CA_C01.mpt': {'label': "0.925 V/RHE (058)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171114_Pd_054_06_CA_C01.mpt': {'label': "1.125 V/RHE (054)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171115_Pd_055_06_CA_C01.mpt': {'label': "1.325V/RHE (055)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171115_Pd_056_06_CA_C01.mpt': {'label': "0.825V/RHE (056)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171116_Pd_059_06_CA_C01.mpt': {'label': "0.575 V/RHE (059)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         # 'AW_Pd_042_02_CVA_C01.mpt':{'label': "Pd_042 50mV/s",
                         #                             'cycles to extract': [2],
                         #                             'electrode area geom': 2, 'electrode area ecsa': 0,
                         #                             'individual ohmicdrop': 44},
                         # 'AW_Pd_045_02_CVA_C01.mpt':{'label': "Pd_045 50mV/s",
                         #                             'cycles to extract': [2],
                         #                             'electrode area geom': 2, 'electrode area ecsa': 0,
                         #                             'individual ohmicdrop': 42},
                         # 'AW_Pd_040_03_CA_C01.mpt':{'label': "Pd_040", 'electrode area geom': 2,
                         #                            'electrode area ecsa':46.49},
                         # 'AW_Pd_042_05_CA_C01.mpt':{'label': "Pd_042", 'electrode area geom': 2,
                         #                            'electrode area ecsa':54.91},
                         # 'AW_Pd_045_05_CA_C01.mpt': {'label': "Pd_045", 'electrode area geom': 2,
                         #                             'electrode area ecsa': 62.99}



                        # '20171005_AW_Pd049_2ndtry_04_CVA_C01.mpt':{'label': "Pd_049 50mV/s",
                        #                              'cycles to extract': [2],
                        #                              'electrode area geom': 2, 'electrode area ecsa': 97.9},
                        #  '20171006_AW_Pd050_onlyAr_04_CVA_C01.mpt': {'label': "Pd_050 50mV/s",
                        #                                              'cycles to extract': [2],
                        #                                              'electrode area geom': 2,
                        #                                              'electrode area ecsa': 55.1},
                        #  '20171010_AW_Pd051_04_CVA_C01.mpt':{'label': "Pd_051 50mV/s",
                        #                                              'cycles to extract': [2],
                        #                                              'electrode area geom': 2,
                        #                                             'electrode area ecsa': 83.5},
                        #  '20171011_AW_Pd_052_2ndgo_04_CVA_C01.mpt':{'label': "Pd_052 50mV/s",
                        #                                              'cycles to extract': [2],
                        #                                              'electrode area geom': 2,
                        #                                             'electrode area ecsa': 78.9
                        #                                             }
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
                     'plotname': "Pd_054-059_CA_raw_zoom",
                     'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                     'grid': True,
                     'second axis':  False,
                     'x_lim': (-10, 3700),
                     'y_lim': (-0.05, 0.2),
                     'y2_lim': (0, 0.025),
                     'top_pad': 0.2,
                     'bottom_pad': 0.1,
                     'l_pad': [],
                     'r_pad': [],
                     'colors': ['g', 'b', 'grey','orange', 'r', '#4a235a', 'r', 'b', 'k', 'c', 'm', '0.50',"#538612", '0.75'],
                     'linestyle': ['-', '-'],
                     'colors2': ['0.25', 'grey', '0.75'],
                     'linestyle2': ['--','--','--'],
                     # color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
                     # color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
                     #options to select which data is plotted
                     'plot type': "ca", #possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
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
            json.dump(plot_load_settings, f)

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
    # esca_data = dpf.calc_esca(datalist[0:4], type='oxide_red')
    # print(esca_data)

    esca_data=[] #uncomment if no calculation of esca to avoid error in EC_plot
    #plot the data from the list of data dictionaries
    # print(datalist)

    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr, esca_data)

    # try:
    # except IndexError:

    print("FINISHED")

if __name__ == "__main__":
    main()



