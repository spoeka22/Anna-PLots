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
e_rhe_ref = -0.811  # V -0.811 at pH 3
ph_ref = 3

# electrolyte
info = "0.1 M HClO_{4}"  # to be printed in annotations (not implemented)
ph = 3

# electrode area in cm2
electrode_area_geom = 1  # cm2
electrode_area_ecsa = 1  # cm2

# ohmic drop in Ohm over cell measured with EIS
ohm_drop_corr = False  # to turn on/off ohmic drop correction
ohmicdrop = 50

# insert filename in list if starting time is notzero, AND should be plotted as nonzero (ie NOT BE CHANGED)
no_timezero = {'20180415_Pd_127_RDE_2_03_CA_C01.mpt'}

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
    folder_path = r'C:\Users\annawi\Desktop\Projects\Propene oxidation\Experiments\201902_PdonAu'

    folders = [
        # '20190129',
                # '20190201'
               '20190212'
    ]
    # list of folders from which data is going to be plotted

    filenames = OrderedDict([('20190129', [
                            'AW_PdonAu_003_EC_testing_3_02_CVA_C02.mpt',
                            'AW_PdonAu_005_EC_testing_2_02_CVA_C02.mpt'
    ]),
               ('20190201', [
                   '20190201_AW_Aublank_aquaregia_etched_pH1_Ar_try3_02_CVA_C02.mpt',
                   '20190201_AW_Aublank_aquaregia_etched_pH1_Ar_try4_04_CVA_C02.mpt',
                   '20190201_AW_Aublank_aquaregia_etched_pH3_Ar_05_CVA_C02.mpt',
                   '20190201_AW_Aublank_aquaregia_etched_pH3_Ar_try2_02_CVA_C02.mpt',
                   '20190201_AW_Aublank_flameannealed_pH1_Ar_05_CVA_C02.mpt',
                   '20190201_AW_Aublank_flameannealed_pH1_Ar_try2_02_CVA_C02.mpt',
                   '20190201_AW_Aublank_flameannealed_pH1_Ar_try3_02_CVA_C02.mpt',
                   '20190201_AW_Aublank_flameannealed_pH1_Ar_try4_02_CVA_C02.mpt',
                   '20190201_AW_PdonAu_002_pH3_Ar_01_CA_C02.mpt',
                   '20190201_AW_PdonAu_002_pH3_Ar_02_SPEIS_C02.mpt',
                   '20190201_AW_PdonAu_002_pH3_Ar_03_CA_C02.mpt',
                   '20190201_AW_PdonAu_002_pH3_Ar_05_CVA_C02.mpt',
                   '20190201_AW_PdonAu_004_pH3_Ar_01_CA_C02.mpt',
                   '20190201_AW_PdonAu_004_pH3_Ar_02_SPEIS_C02.mpt',
                   '20190201_AW_PdonAu_004_pH3_Ar_03_CA_C02.mpt',
                   '20190201_AW_PdonAu_004_pH3_Ar_05_CVA_C02.mpt']),
               ('20190212', [
                    '20190212_Pdfoil_HNO3cleaned_pH3_05_CVA_C02.mpt'
                             ]),

        ])




    # custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
    #electrode area (geom and ecsa), ohmic drop to correct for
    # 'ref_data' is list of [Eref, pHref and ph]

    #IMPORTANT: only the SA of propene ox test included in article is correctly DL corrected

    filespec_settings = {'f_CV_Pd_025_Ar_C01_cycle13.mpt': {'label': "Ar cycle 13)",
                                                     # 'cycles to extract': [2],
                                                     'electrode area geom': 1, 'electrode area ecsa': 1,
                                                      #'individual ohmicdrop': 43.3
                                                    },



                         #CVs

                         '20190212_Pdfoil_HNO3cleaned_pH3_05_CVA_C02.mpt': {'label': "Pd foil (HNO3 cleaned)",
                                                     'cycles to extract': [10, 33, 34, 35],
                                                     'electrode area geom': 1, 'electrode area ecsa': 0,
                                                      #'individual ohmicdrop': 43.3
                                                    },


                         '20171212_AW_Pd_073_SA_eval_04_CVA_C01.mpt': {'label': "0.90 V/RHE (073))",
                                                     'cycles to extract': [2],
                                                     'electrode area geom': 2, 'electrode area ecsa': 0,
                                                      #'individual ohmicdrop': 43.3
                                                    },


                         }
    if savesettings:
        data_load_settings = [folder_path, folders, filenames, filespec_settings]

        save_settings_as = input("Save data input settings as ([...]_input.txt): ") + "_input.txt"
        with open('import_settings/'+save_settings_as, 'w') as f:
            json.dump(data_load_settings, f)


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
    plot_settings = {'safeplot': False,
                     'plotname': "20181026_CV_CO_strip_ELPd_c1+2",
                     'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                     'grid': False,
                     'second axis':  False,
                     'x_lim': (-0.1, 1.8),
                     'y_lim': (-4, 12),
                     'y_logscale': False,
                     'y2_lim': (0, 0.025),
                     'top_pad': 0.2,
                     'bottom_pad': 0.1,
                     'l_pad': [],
                     'r_pad': [],
                     # 'colors': ['0.25',[0.03137255, 0.20853518, 0.4497501, 1.],'0.25', 'b', 'grey','k', 'r', '#4a235a', 'c', '#538612', 'c', 'm', '0.50',"#538612", '0.75'],
                     'colors': ['r', 'b', '#bd4de0' ,'orange', 'g', '#d816ff'],
                     # 'colors': ['k','#bd4de0', '#6b12ad', 'g', '#266f0e', 'grey'],
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
                     "tick label size": 14,
                     "plot_average_cond": None,
                     }

    # #settings for the plot - CA settings
    # plot_settings = {'safeplot': False,
    #                  'plotname': "20180918_CAs_article_data_small_095-12VRHE",
    #                  'coplot_evsrhe': False,
    #                  # for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
    #                  'grid': True,
    #                  'second axis': False,
    #                  'x_lim': (-10, 200),
    #                  'y_lim': (-0.1, 0.1),
    #                  'y_logscale': False,
    #                  'y2_lim': (0.0, 2),
    #                  'top_pad': 0.2,
    #                  'bottom_pad': 0.15,
    #                  'l_pad': 0.2,
    #                  'r_pad': [],
    #                  'colors': ['r', 'orange', 'grey', 'orange', 'r', '#4a235a', 'k', 'c', '#538612', 'c', 'm', '0.50',
    #                             "#538612", '0.75'],
    #                  # 'colors': [ '#bd4de0' , 'k', 'orange', 'g', 'b', 'r', '#d816ff', "#ff8a16"],
    #                  # 'colors': ['#bd4de0', '#6b12ad', #purple
    #                  #            'grey', 'k',
    #                  #            'g', '#266f0e'
    #                  #            ],
    #                  # 'colors': ['#bd4de0', 'orange', '#d816ff', "#ff8a16"],
    #                  # 'colors': plt.cm.gist_earth(range(255, 10, 10)),
    #
    #                  # 'colors':  [
    #                  #     # '#08820a', '#098d55','#098d7b','#097d8d',
    #                  #     '#095f8d', '#093b8d', '#15098d', '#120a5a',
    #                  #         # "grey",  # Ar #0.9 Ar 107
    #                  #         "k"
    #                  #     ],
    #                  #
    #
    #
    #                  'linestyle': ['-', '-.', '-', '-', '-', '-', '-', '-', '--', '-'],
    #                  # 'linestyle': ['--', '--', '-', '-', '-', '-', '-', '-'],
    #                  'colors2': ['k', 'grey', '0.75'],
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
    #                  'x_data': "time/min",
    #                  # 'y_data': "<I>/mA",
    #                  'y_data': "i/mAcm^-2_geom",
    #                  'x_data2': "",  # not implemented yet
    #                  "y_data2": "EvsRHE/V",
    #                  # "aspect": 100,
    #                  "axis label size": 14,
    #                  "tick label size": 14,
    #                  "plot_average_cond": None #{"EvsRHE/V":[0.95, 1.0, 1.1, 1.2], "not_average":['20180222_Pd_107_03_CA_C01.mpt']} #, "not_average": ['20180222_Pd_107_03_CA_C01.mpt']} #{"EvsRHE/V":[0.85, 0.9, 0.95]}#{"EvsRHE/V":[0.7, 0.8, 0.85, 0.9 ,0.95, 1.0, 1.1, 1.2]}
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

        #conversion to rhe scale
        try: print(file['settings']['ref_data'])  #'ref_data' is list of [Eref, pHref and ph]
        except KeyError:
            print("KEY ERROR IN RHE CONVERSION")
            file['data'] = file['data'].add(DataFrame([dpf.convert_potential_to_rhe(file['data']['Ewe/V'], e_rhe_ref=e_rhe_ref, ph_ref=ph_ref, ph=ph)],
                                                  index=['EvsRHE/V']).T, fill_value=0)
        else:
            print("NO KEY ERROR IN RHE CONVERSION")
            file['data'] = file['data'].add(DataFrame([dpf.convert_potential_to_rhe(file['data']['Ewe/V'], e_rhe_ref=file['settings']['ref_data'][0],
                                                                                      ph_ref=file['settings']['ref_data'][1], ph=file['settings']['ref_data'][2])],
                                                  index=['EvsRHE/V']).T, fill_value=0)
        if ohm_drop_corr: #only works for standard reference electrode giving at top of settings
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

        #add a column that contains time in min
        time_in_min = file['data']['time/s'].divide(60)
        # print(time_in_min)
        file['data'] = file['data'].add(DataFrame([time_in_min], index=['time/min']).T, fill_value=0)

     #TODO: find set potential in CA and print it/annotate it in plot


    #CALCULATE ESCA: type="CO_strip": difference between the first 2 cycles in list of data, rest of list is ignored.
    #type="oxide_red": finds oxide red charge and calculates ESCA with given charge_p_area for each item in list, also
    #plots the calculated data as bar chart
    #type=oxide_red_tilt: more accurate for tilted CVs
    # esca_data = dpf.calc_esca(datalist[0:17], type='CO_strip', scanrate=2, charge_p_area=0.000481709)
    # print(esca_data)



    #PLOT THE DATA FROM THE LIST OF DATA DICTIONARIES
    esca_data=[] #uncomment if no calculation of esca to avoid error in EC_plot
    # print(datalist)
    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr, esca_data)
    #
    #PLOT THE CURRENT AT A GIVEN TIME AS A FUNCTION OF POTENTIAL
    # dpf.current_at_time_plot(datalist, times=[60, 180, 600, 3300], I_col="i/mAcm^-2_ECSA")
    # dpf.current_at_time_plot(datalist, times=[60, 180, 600, 3300], I_col="q/mCcm^-2_ECSA")


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

    #TEST of grouping datalines
    # selection_conditions = {"EvsRHE/V":[0.85, 0.90, 0.95]}
    # dpf.group_datalines(datalist, selection_conditions)


    print("FINISHED")

if __name__ == "__main__":
    main()



