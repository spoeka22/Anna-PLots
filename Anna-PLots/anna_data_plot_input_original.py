# -*- coding: utf-8 -*-
"""
Created on Tue Oct  18 19:25:46 2016

@author: Anna

Settings for the data to plot are inserted here. The data plotting is done using functions stored in anna_data_plot_functions.
"""

from pandas import DataFrame

import anna_data_plot_functions

# general information  if applicable, otherwise comment
# temperature
temperature = 25  # C

# reference electrode
e_rhe_ref = -0.720  # V
ph_ref = 1

# electrolyte
info = "0.1 M HClO4"  # to be printed in annotations
ph = 0.96

# electrode area in cm2
electrode_area_geom = 2  # cm2
electrode_area_real = False  # cm2 NOT IMPLEMENTED YET
electrode_area_geom_special = {#'f_CA_Au_001_POR_C01.mpt': 1, 
#              'Au_002_POR_06_CA_C01.mpt': 1,
#              'i_CA_Pd_025_Ar_propenepurge_02_CA_C01.mpt': 1,
#              'k_CA_Pd_025_Propene_C01.mpt': 1
              }

#ohmic drop in Ohm over cell measured with EIS
ohm_drop_corr = True #to turn on/off ohmic drop correction
ohmicdrop = 39
ohmicdrop_filename = {'b_CA_Pd_020_HClO4_propene_C01.txt': 34.5,
              'c_CA_Pd_021_HClO4_propene_C01.txt': 23.5,
              'b_CA_POR_Pd_022_C01.txt': 44
              }
             
#insert filename in list if starting time is notzero, AND should be plotted as nonzero (ie NOT BE CHANGED)
no_timezero = {'i_CA_Pd_025_Ar_propenepurge_02_CA_C01.mpt'}             

general_info = DataFrame(data=[temperature, e_rhe_ref, ph_ref, info, ph, electrode_area_geom, electrode_area_real, electrode_area_geom_special, ohm_drop_corr, ohmicdrop,
                               ohmicdrop_filename, no_timezero],
                         index=["temperature", "e_rhe_ref", "ph_ref", "info", "ph", "electrode_area_geom",
                                "electode_area_real", "electrode_area_geom_special", "ohm_drop_corr",  "ohmicdrop", 'ohmicdrop_filename', 'no_timezero'], columns=["value"])

print(general_info)


# dictionary containing local folder names and names of the files containing relevant data
# TO BE IMPLEMENTED: automatic searching for appropriate filenames in a given folder and importing selected files


#folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Au electrodes'

folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Pd electrodes\initial POR tests Pd\AW_Pd_038'

folders = [
#           'CV_tests_Ar',
           'CV_test_propene',
#           'CO stripping'
           ]  # list of folders from which data is going to be plotted

filenames = {'CV_tests_Ar': [# 'AW_Pd_038_CVtests_Ar_02_CVA_C01_cycle1.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_02_CVA_C01_cycle2.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_02_CVA_C01_cycle11.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_03_CVA_C01_cycle4.mpt',
                                                       'AW_Pd_038_CVtests_Ar_04_CVA_C01_cycle4.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_05_CVA_C01_cycle4.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_06_CVA_C01_cycle4.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_07_CVA_C01_cycle4.mpt',
#                                           'AW_Pd_038_CVtests_Ar_08_CVA_C01_cycle4.mpt',
#                                           'AW_Pd_038_CVtests_Ar_09_CVA_C01_cycle5.mpt',
#                                           'AW_Pd_038_CVtests_Ar_10_CVA_C01_cycle5.mpt',
#                                           'AW_Pd_038_CVtests_Ar_11_CVA_C01_cycle5.mpt',
#                                           'AW_Pd_038_CVtests_Ar_12_CVA_C01_cycle5.mpt',
                                                       'AW_Pd_038_CVtests_Ar_13_CVA_C01_cycle5.mpt',
                                                       'AW_Pd_038_CVtests_Ar_14_CVA_C01_cycle5.mpt',
                                                       'AW_Pd_038_CVtests_Ar_15_CVA_C01_cycle5.mpt',
                                                       'AW_Pd_038_CVtests_Ar_16_CVA_C01_cycle5.mpt',
#                                                       'AW_Pd_038_CVtests_Ar_17_CVA_C01_cycle5.mpt'
                                           ],
             'CV_test_propene': [#'AW_Pd_038_CVtests_Propene_17_CVA_02_CVA_C01_cycle1.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_02_CVA_C01_cycle2.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_02_CVA_C01_cycle11.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_03_CVA_C01_cycle4.mpt',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_04_CVA_C01_cycle4.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_05_CVA_C01_cycle4.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_06_CVA_C01_cycle4.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_07_CVA_C01_cycle4.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_08_CVA_C01_cycle4.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_09_CVA_C01_cycle5.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_10_CVA_C01_cycle5.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_11_CVA_C01_cycle5.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_12_CVA_C01_cycle5.mpt',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_13_CVA_C01_cycle5.mpt',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_14_CVA_C01_cycle5.mpt',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_15_CVA_C01_cycle5.mpt',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_16_CVA_C01_cycle5.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_17_CVA_C01_cycle5.mpt',
#                                  'AW_Pd_038_CVtests_Propene_17_CVA_17_CVA_C01_cycle11.mpt'
                                  ],

                'CO stripping': ['AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle18.mpt',
                                 'AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle19.mpt',
                                 'AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle21.mpt',
                                 'AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle13.mpt',
                                 'AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle14.mpt',
                                 'AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle15.mpt',
                                 'AW_Pd_038_CO_stripping_test_02_CVA_C01_cycle16.mpt'
                                 ]
             
             }



# custom labels for data: dictionary correlating filename with label to be assigned:

data_label = {                 
                                       'AW_Pd_038_CVtests_Ar_08_CVA_C01_cycle4.mpt': 'Ar, 08 cycle4, 50 mV/s',
                                                       'AW_Pd_038_CVtests_Ar_09_CVA_C01_cycle5.mpt': 'Ar, 09 cycle5, 20 mV/s',
                                                       'AW_Pd_038_CVtests_Ar_10_CVA_C01_cycle5.mpt': 'Ar, 10 cycle5, 100 mV/s',
                                                       'AW_Pd_038_CVtests_Ar_11_CVA_C01_cycle5.mpt': 'Ar, 11 cycle5, 200 mV/s',
                                                       'AW_Pd_038_CVtests_Ar_12_CVA_C01_cycle5.mpt': 'Ar, 12 cycle5, 500 mV/s',
                                                           'AW_Pd_038_CVtests_Propene_17_CVA_08_CVA_C01_cycle4.mpt': 'propene, 08 cycle4, 50 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_09_CVA_C01_cycle5.mpt': 'propene, 09 cycle5, 20 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_10_CVA_C01_cycle5.mpt': 'propene, 10 cycle5, 100 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_11_CVA_C01_cycle5.mpt': 'propene, 11 cycle5, 200 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_12_CVA_C01_cycle5.mpt': 'propene, 12 cycle5, 500 mV/s',
                                  'AW_Pd_038_CVtests_Ar_04_CVA_C01_cycle4.mpt': 'Ar, 04 cycle4, 50 mV/s',
                                  'AW_Pd_038_CVtests_Ar_13_CVA_C01_cycle5.mpt': 'Ar, 13 cycle5, 20 mV/s',
                                  'AW_Pd_038_CVtests_Ar_14_CVA_C01_cycle5.mpt': 'Ar, 14 cycle5, 100 mV/s',
                                  'AW_Pd_038_CVtests_Ar_15_CVA_C01_cycle5.mpt': 'Ar, 15 cycle5, 200 mV/s',
                                  'AW_Pd_038_CVtests_Ar_16_CVA_C01_cycle5.mpt': 'Ar, 16 cycle5, 500 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_04_CVA_C01_cycle4.mpt': 'propene, 04 cycle4, 50 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_13_CVA_C01_cycle5.mpt': 'propene, 13 cycle5, 20 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_14_CVA_C01_cycle5.mpt': 'propene, 14 cycle5, 100 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_15_CVA_C01_cycle5.mpt': 'propene, 15 cycle5, 200 mV/s',
                                  'AW_Pd_038_CVtests_Propene_17_CVA_16_CVA_C01_cycle5.mpt': 'propene, 16 cycle5, 500 mV/s'}
                                            

# plottype defines axis labels and settings. can be either ca or cv. to be evaluated whether useful or not
plottype = "cv"


# settings for the plot
plot_settings = {'safeplot': True,
                 'plotname': 'CV_Pd_038_Propene_development_scanrate_UPL_1.4Vrhe',
                 'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                 'grid': True,
                 'second axis':  True,
                 'x_lim': (0.25, 1.6),
                 'y_lim': (-6.0, 6),
                 'y2_lim': (0.25, 1.5),
                 'top_pad': 0.2,
                 'bottom_pad': 0.1,
                 'l_pad': [],
                 'r_pad': [],
                 }

# legend:
legend_settings = {'position': (0, 1.15),
                   'number_of_cols': 2,
                   'fontsize': 10
                   }

# annotations: dictionary of annotation plus relevant properties in list form
annotation_settings = {'annotation 1': ["scanrate"],
                       #E-range for finding the delta i in the capacitance region for estimation of surface area
                       'e_range': [0.99, 1.01] #works only if scan starts at lowest potential
                       }


# todo: subplot possibility


def main():
    # import file (can be commented if doplot is active)
    # anna_data_plot.import_data(plottype, filenames, general_info)


    # make the plot (includes importing the file)
    anna_data_plot_functions.doplot(plottype=plottype, folder_path=folder_path, filenames=filenames, folders=folders,
                                    data_label=data_label, plot_settings=plot_settings, legend_settings=legend_settings,
                                    annotation_settings=annotation_settings, general_info=general_info)


if __name__ == "__main__":
    main()



