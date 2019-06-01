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
e_rhe_ref = 0 # V #new:-0.724, pH=1.2
ph_ref = 0

# electrolyte
info = "1 M HClO_{4}"  # to be printed in annotations (not implemented)
ph = 0

# electrode area in cm2
electrode_area_geom = 6.25# cm2
electrode_area_ecsa = 1 # cm2
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
    # folder_path = r'\\dtu-storage\annawi\Desktop\Projects\Methane oxidation\FC teststation experiments Stanford\commercial cell Pt-Pt'
    folder_path = r'\\dtu-storage\annawi\Desktop\Projects\Methane oxidation\FC teststation experiments Stanford\commercial MEA PtRu-Pt'
    OrderedDict([ ])

    folders = [
               # '20180920',
               # '20180922',
               # '20180924',
               # '20181101',
               #  '20181105',
               #  '20181106',
               #  '20181123', # THIS FOLDER REQUIRES FOLDERPATH TO PtRu FOLDER!!
                '20181126', # THIS FOLDER REQUIRES FOLDERPATH TO PtRu FOLDER!!
               ]
      # list of folders from which data is going to be plotted

    filenames = OrderedDict([('20180920', [
                                           # '20180920_CAs_H2air_02_CA_C05.mpt',
                                           # '20180920_CAs_H2air_2_02_CA_C05.mpt',
                                           '20180920_CAs_polcurve_H2air_02_CA_C05.mpt',
                                           # '20180920_CVs_WE@cathode_startup_1_02_CV_C05.mpt',
                                           # '20180920_PEIS_after_polcurve_C05.mpt',
                                           # '20180920_PEIS_startup_5_C05.mpt',
                                           # '20180920_PEIS_startup_6_afterCVs_C05.mpt'
                                           ]),
                             ('20180922', [
                                            '20180922_CAs_polcurve_restart_H2air_run_02_CA_C05.mpt',
                                            # '20180922_CAs_Refcath_N2Ch4_02_CA_C05.mpt',
                                            # '20180922_CVs_Refcath_N2Ch4_02_CV_C05.mpt',
                                            # '20180922_OCV_gas_change_C05.mpt',
                                            # '20180922_PEIS_after_restart_3_C05.mpt',
                                            # '20180922_PEIS_Refcath_N2Ch4_afterCAs_C05.mpt',
                                            # '20180922_PEIS_Refcath_N2Ch4_C05.mpt'
                                           ]),
                             ('20180924', [
                                            # '20180924_CAs_Refcath_airCh4_02_CA_C05.mpt',
                                           '20180924_CVs_Refanode_Ch4air_02_CV_C05.mpt',
                                           # '20180924_CVs_Refanode_Ch4air_2_02_CV_C05.mpt',
                                           # '20180924_CVs_Refcath_airCh4_02_CV_C05.mpt',
                                           # '20180924_PEIS_Refanode_Ch4air_C05.mpt',
                                           # '20180924_PEIS_Refcath_airCh4_afterstartup_C05.mpt'
                                           ]),
                             ('20181101',[
                                          # '20181101_CA_EFatCATH_test_02_CA_C05.mpt',
                                          # '20181101_CVs_N2N2_refatcathode_02_CV_C05.mpt',
                                          # '20181101_CVs_startup_3_02_CV_C05.mpt',
                                          # '20181101_CVs_startup_afterCAinH2_02_CV_C05.mpt',
                                          # '20181101_polarisation_N2N2_refatcathode_03_CA_C05.mpt',
                                          # '20181101_polarisation_N2N2_refatcathode_06_CA_C05.mpt',
                                          # '20181101_polcurve_startup_REFatCATH_try2_02_CA_C05.mpt',
                                          # '20181102_CVs_CH4anN2cath_refatcath_02_CV_C05.mpt',
                                          # '20181102_CVs_N2N2_refatcathode_afterCAs_02_CV_C05.mpt',
                                          # '20181102_CVs_N2N2_refatcathode_afterCAs_purge_higherflow_02_CV_C05.mpt',
                                          # '20181102_Polcurve_CH4anN2cath_refatcath__02_CA_C05.mpt'
                              ]),
                             ('20181105', [
                                           # '20181105_CA_polcurve_CH4strip450mV_CH4cathH2an_refatAnode_02_CA_C05.mpt',
                                           # '20181105_CVs_CH4cathH2an_refatAnode_02_CV_C05.mpt',
                                           '20181105_CVs_CH4strip250mV_CH4cathH2an_refatAnode_02_CA_C05.mpt',
                                           # '20181105_CVs_CH4strip250mV_CH4cathH2an_refatAnode_03_CV_C05.mpt',
                                           '20181105_CVs_CH4strip350mV_CH4cathH2an_refatAnode_02_CA_C05.mpt',
                                           # '20181105_CVs_CH4strip350mV_CH4cathH2an_refatAnode_03_CV_C05.mpt',
                                           '20181105_CVs_CH4strip450mV_CH4cathH2an_refatAnode_02_CA_C05.mpt',
                                           # '20181105_CVs_CH4strip450mV_CH4cathH2an_refatAnode_03_CV_C05.mpt'
                             ]),
                            ('20181106', [
                                         # '20181106_CA_polcurve_N2cathH2an_refatAnode_10mAcurrentrange_02_CA_C05.mpt',
                                         # '20181106_CA_polcurve_N2cathH2an_refatAnode_1mAcurrentrange_02_CA_C05.mpt',
                                         # '20181106_CA_polcurve_N2cathH2an_refatAnode_1mAcurrentrange_try2_02_CA_C05.mpt',
                                         # '20181106_CVs__N2cathH2an_refatAnode_02_CV_C05.mpt',
                                         #   '20181106_CA_polcurve_N2cathH2an_refatAnode_02_CA_C05.mpt'
                                         '20181106_CVs__stripping_250+450mV_N2cathH2an_refatAnode_02_CA_C05.mpt',
                                         # '20181106_CVs__stripping_250+450mV_N2cathH2an_refatAnode_03_CV_C05.mpt',
                                         '20181106_CVs__stripping_250+450mV_N2cathH2an_refatAnode_04_CA_C05.mpt',
                                         # '20181106_CVs__stripping_250+450mV_N2cathH2an_refatAnode_05_CV_C05.mpt',
                                         '20181106_CVs__stripping_350mV_N2cathH2an_refatAnode_02_CA_C05.mpt',
                                         # '20181106_CVs__stripping_350mV_N2cathH2an_refatAnode_03_CV_C05.mpt'
                            ]),
                            ('20181123', [
                                        # '20181122_CAs_CH4atPtRu_h2atPt_polcurve_02_CA.mpt',
                                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_02_CV.mpt', #start
                                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_03_CA.mpt', #350 mV
                                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_04_CV.mpt', #350 mV
                                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_05_CA.mpt', #250 mV
                                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_06_CV.mpt', #250 mV
                                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_07_CA.mpt', #450 mV
                                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_08_CV.mpt'  #450 mV
                            ]),
                             ('20181126', [
                                         # '20181126_CAs_N2atPtRu_h2atPt_polcurve_02_CA.mpt',
                                         # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_02_CV.mpt', #start
                                         # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_03_CA.mpt', #350 mV
                                         '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_04_CV.mpt', #350 mV
                                         # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_05_CA.mpt', #250 mV
                                         '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_06_CV.mpt', #250 mV
                                         # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_07_CA.mpt', #450 mV
                                         '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_08_CV.mpt'  #450 mV
                             ])


    ])




    # custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
    #electrode area (geom and ecsa), ohmic drop to correct for
    #'ref_data' is list of [Eref, pHref and ph] for co-plotting data recorded at different pH/with different ref

    filespec_settings = {
                        '02_cycles_02_CVA.mpt': {'label': "CO strip pc Pd",
                                                               'cycles to extract': [24,25],
                                                               'electrode area geom': 0.196349541,
                                                               'electrode area ecsa': 0.196349541,
                                                               # 'individual ohmicdrop': 43.3
                                                           },
                        '20180920_CAs_polcurve_H2air_02_CA_C05.mpt': {'label': "H2_air, ref@anode day1"},
                        '20180922_CAs_polcurve_restart_H2air_run_02_CA_C05.mpt': {'label': "H2_air, ref@anode, day 2"},
                        '20180922_CAs_Refcath_N2Ch4_02_CA_C05.mpt': {'label': "CH4_N2, ref@cath"},
                        '20180924_CAs_Refcath_airCh4_02_CA_C05.mpt': {'label': "CH4_air, ref@cath"},
                        '20180920_CVs_WE@cathode_startup_1_02_CV_C05.mpt': {'label': "H2_air, ref@anode",
                                                                            'cycles to extract': [5] },
                        '20180922_CVs_Refcath_N2Ch4_02_CV_C05.mpt': {'label': "CH4_N2, ref@cath",
                                                                            'cycles to extract': [5]},
                        '20180924_CVs_Refcath_airCh4_02_CV_C05.mpt': {'label': "CH4_air, ref@anode",
                                                                            'cycles to extract': [8]},
                        '20180924_CVs_Refanode_Ch4air_02_CV_C05.mpt': {'label': "air_CH4, ref@cath",
                                                                      'cycles to extract': [2]},

                        '20181101_CVs_startup_afterCAinH2_02_CV_C05.mpt': {'label': "air_H2, ref@cath",
                                                                      'cycles to extract': [1,5,8]},

                        '20181105_CVs_CH4cathH2an_refatAnode_02_CV_C05.mpt': {'label': "CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,5,8]},

                        '20181105_CVs_CH4strip250mV_CH4cathH2an_refatAnode_03_CV_C05.mpt': {'label': "250 mV 30 min CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1]},

                        '20181105_CVs_CH4strip350mV_CH4cathH2an_refatAnode_03_CV_C05.mpt': {'label': "350 mV 30 min CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1]},

                        '20181105_CVs_CH4strip450mV_CH4cathH2an_refatAnode_03_CV_C05.mpt': {'label': "450 mV 30 min CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1]},

                        '20181106_CVs__stripping_250+450mV_N2cathH2an_refatAnode_03_CV_C05.mpt': {'label': "250 mV 30 min N2(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1]},

                        '20181106_CVs__stripping_250+450mV_N2cathH2an_refatAnode_05_CV_C05.mpt': {'label': "450 mV 30 min N2(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1]},

                        '20181106_CVs__stripping_350mV_N2cathH2an_refatAnode_03_CV_C05.mpt': {'label': "350 mV 30 min N2(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1]},
                         '20181106_CA_polcurve_N2cathH2an_refatAnode_02_CA_C05.mpt': {'label': "N2(anode)_H2, ref@cath"},
                        '20181105_CA_polcurve_CH4strip450mV_CH4cathH2an_refatAnode_02_CA_C05.mpt': {'label': "CH4(anode)_H2, ref@cath"},

                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_02_CV.mpt': {'label': "initial CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]},
                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_03_CA.mpt', #350 mV
                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_04_CV.mpt': {'label': "350 mV 30 min CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]}, #350 mV
                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_05_CA.mpt', #250 mV
                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_06_CV.mpt': {'label': "250 mV 30 min CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]}, #250 mV
                        # '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_07_CA.mpt', #450 mV
                        '20181122_CVsCAs_CH4atPtRu_h2atPt_start+350+250+450mV_stripping_08_CV.mpt': {'label': "450 mV 30 min CH4(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]},  #450 mV,
                        # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_02_CV.mpt', #start
                        # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_03_CA.mpt', #350 mV
                        '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_04_CV.mpt': {'label': "350 mV 30 min N2(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]}, #350 mV
                        # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_05_CA.mpt', #250 mV
                        '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_06_CV.mpt': {'label': "250 mV 30 min N2(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]}, #250 mV
                        # '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_07_CA.mpt', #450 mV
                        '20181126_CVsCAs_N2atPtRu_h2atPt_start+350+250+450mV_stripping_08_CV.mpt': {'label': "450 mV 30 min N2(anode)_H2, ref@cath",
                                                                      'cycles to extract': [1,2]},   #450 mV



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
                     'plotname': "20181123_CVs_N2_H2_strip_250350450mV_30min",
                     'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                     'grid': False,
                     'second axis':  False,
                     'x_lim': (-0.09, 0.99),
                     'y_lim': (-110, 60),
                     'y_logscale': False,
                     'y2_lim': (0, 0.025),
                     'top_pad': 0.2,
                     'bottom_pad': 0.1,
                     'l_pad': [],
                     'r_pad': [],
                     'colors': ['orange', '0.75', 'r', 'k', '#bd4de0', 'grey','g', 'r', '#4a235a', 'c', '#538612', 'c', 'm', '0.50',"#538612", '0.75'],
                     # 'colors': [ '#bd4de0' , 'k', 'orange', 'g', 'b', 'r', '#d816ff', "#ff8a16"],
                     # 'colors': ['#bd4de0', 'k', '#6b12ad', 'g', '#266f0e', 'grey'],
                     # 'colors': ['#bd4de0', 'orange', '#d816ff', "#ff8a16"],
                     'linestyle': ['-', ':','-', '--','-', '--'],
                     'colors2': ['0.25', 'grey', '0.75'],
                     'linestyle2': ['--','--','--'],
                     #options to select which data is plotted
                     'plot type': "cv", #possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
                     #custom column selection, will overrule plottype, if given. Possibilities are all data column names,
                     #most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
                     # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
                     'x_data':"Ewe/V",
                     'x_data_label': "Cell voltage / V",
                     'y_data':"i/mAcm^-2_geom",
                     'x_data2':"", #not implemented yet
                     "y_data2":"",
                     "aspect": 0.95,
                     "axis label size": 16,
                     "tick label size": 14,
                     'plot_average_cond': False
                     }

    # settings for the plot - polarisation curve settings
    # plot_settings = {'safeplot': True,
    #                  'plotname': "2018112326_PtRu_polcurves_CH4+N2_H2_vs1",
    #                  'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
    #                  'grid': False,
    #                  'second axis':  False,
    #                  'x_lim': (-0.4, 1.00), #current
    #                  'y_lim': (0.0, 1.0), #voltage
    #                  'y_logscale': False,
    #                  'y2_lim': (0, 0.025),
    #                  'top_pad': 0.2,
    #                  'bottom_pad': 0.1,
    #                  'l_pad': [],
    #                  'r_pad': [],
    #                  'colors': [ 'k', 'orange','#266f0e', 'k', 'r', '0.25',[0.03137255, 0.20853518, 0.4497501, 1.], 'b', 'grey','k', 'r', '#4a235a', 'c', '#538612', 'c', 'm', '0.50',"#538612", '0.75'],
    #                  # 'colors': [ '#bd4de0' , 'k', 'orange', 'g', 'b', 'r', '#d816ff', "#ff8a16"],
    #                  # 'colors': ['#bd4de0', 'k', '#6b12ad', 'g', '#266f0e', 'grey'],
    #                  # 'colors': ['#bd4de0', 'orange', '#d816ff', "#ff8a16"],
    #                  'linestyle': ['-', '--'],
    #                  'colors2': ['0.25', 'grey', '0.75'],
    #                  'linestyle2': ['--','--','--'],
    #                  #options to select which data is plotted
    #                  'plot type': "cv", #possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
    #                  #custom column selection, will overrule plottype, if given. Possibilities are all data column names,
    #                  #most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
    #                  # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
    #                  'y_data':"Ewe/V",
    #                  'y_data_label': "Cell voltage / V",
    #                  'x_data':"i/mAcm^-2_geom",
    #                  'x_data2':"", #not implemented yet
    #                  "y_data2":"",
    #                  "aspect": 0.95,
    #                  "axis label size": 16,
    #                  "tick label size": 14,
    #                  'plot_average_cond': False
    #                  }

    # settings for the plot - CA settings
    # plot_settings = {'safeplot': False,
    #                  'plotname': "20181106_CA_polarisation_N2_H2",
    #                  'coplot_evsrhe': False,
    #                  # for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
    #                  'grid': False,
    #                  'second axis': True,
    #                  'x_lim': (-10, 240),
    #                  'y_lim': (-0.5, 1.25),
    #                  'y_logscale': False,
    #                  'y2_lim': (0, 1.25),
    #                  'top_pad': 0.2,
    #                  'bottom_pad': 0.15,
    #                  'l_pad': 0.2,
    #                  'r_pad': [],
    #                  'colors': [ 'r', '#4a235a', 'k', 'c', '#538612', 'm', '0.50',
    #                             "#538612", '0.75'], #'g', 'b', 'grey','orange',
    #
    #                  # 'linestyle': ['-', '-','-', '-','-', '-','-', '-'],
    #                  'linestyle': ['-', '-', '-', '--', '--', '--', '-', '-'],
    #                  'colors2': ['k'],
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
    #                  # 'y_data_label': "TEST",
    #                  'x_data2': "",  # not implemented yet
    #                  "y_data2": "Ewe/V", #"Ewe/V",
    #                  'y_data2_label': "Cell voltage / V",
    #                  # "aspect": 100,
    #                  "axis label size": 14,
    #                  "tick label size": 12,
    #                  "plot_average_cond": False
    #                  }


    # legend:
    legend_settings = {'position1': (0, 1.05),
                       'position2': (0, -0.3), #position of the legend for the second y axis
                       'number_of_cols': 1,
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
        try: file['settings']['ref_data'] #'ref_data' is list of [Eref, pHref and ph]
        except KeyError:
            file['data'] = file['data'].add(DataFrame([dpf.convert_potential_to_rhe(file['data']['Ewe/V'], e_rhe_ref=e_rhe_ref, ph_ref=ph_ref, ph=ph)],
                                                  index=['EvsRHE/V']).T, fill_value=0)
        else: file['data'] = file['data'].add(DataFrame([dpf.convert_potential_to_rhe(file['data']['Ewe/V'], e_rhe_ref=file['settings']['ref_data'][0],
                                                                                      ph_ref=file['settings']['ref_data'][1], ph=file['settings']['ref_data'][2])],
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

        # add a column that contains time in min
        time_in_min = file['data']['time/s'].divide(60)
        # print(time_in_min)
        file['data'] = file['data'].add(DataFrame([time_in_min], index=['time/min']).T, fill_value=0)




    #CALCULATE ESCA: type="CO_strip": difference between the first 2 cycles in list of data, rest of list is ignored.
    #type="oxide_red": finds oxide red charge and calculates ESCA with given charge_p_area for each item in list, also
    #plots the calculated data as bar chart
    # esca_data = dpf.calc_esca(datalist[0:17], type='CO_strip', scanrate=50, charge_p_area=1)
    # print(esca_data)



    #PLOT THE DATA FROM THE LIST OF DATA DICTIONARIES

    # print(datalist)
    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr)
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

    #EVALUATE POLARISATION CURVE
    # polarisationdata = dpf.get_pol_curve_data(datalist, save=False)
    # print(polarisationdata)
    # dpf.EC_plot(polarisationdata, plot_settings, legend_settings, annotation_settings, ohm_drop_corr)

    print("FINISHED")

if __name__ == "__main__":
    main()



