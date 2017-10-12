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

folder_path = r'\\dtu-storage\annawi\Desktop\Propene oxidation\Experiments\Pd electrodes\EC and product analysis'

folders = [#'20171005_Pd_049',
           # '20170901_Pd_040',
           # '20170831_Pd_039',
           '20170916_Pd_046',
           # '20171003_Pd_047',
           # '20171003_Pd_048',
           # '20171006_Pd_050',
           # '20171010_Pd_051'
            ]  # list of folders from which data is going to be plotted

filenames = {'20171005_Pd_049': ['20171005_AW_Pd049_2ndtry_04_CVA_C01.mpt',
                                 '20171005_AW_Pd049_3rd_onlyAr_04_CVA_C01.mpt',
                                 '20171005_AW_Pd049_2ndtry_05_CVA_C01.mpt',
                                 '20171005_AW_Pd049_2ndtry_07_CA_C01.mpt',
                                 '20171005_AW_Pd049_3rd_onlyAr_01_CA_C01.mpt',
                                 '20171005_AW_Pd049_3rd_onlyAr_06_CA_C01.mpt',
                                 '20171005_AW_Pd049_02_CA_C01.mpt',
                                 '20171005_AW_Pd049_2ndtry_06_CA_C01.mpt'
                                 ],
             '20170916_Pd_046': [#'AW_Pd_046_05_CA_C01.mpt',
                                 'AW_Pd_046_02_CVA_C01.mpt'
                                 ],
             '20171006_Pd_050': ['20171006_AW_Pd050_onlyAr_restart_02_CA_C01.mpt',
                                 '20171006_AW_Pd050_onlyAr_restart_03_CA_C01.mpt',
                                 '20171006_AW_Pd050_onlyAr_02_CA_C01.mpt',
                                 '20171006_AW_Pd050_onlyAr_04_CVA_C01.mpt',
                                 '20171006_AW_Pd050_onlyAr_05_CVA_C01.mpt'
                                 ],
             '20170901_Pd_040': ['AW_Pd_040_03_CA_C01.mpt',
                                 'AW_Pd_040_02_CVA_C01.mpt',
                                 'AW_Pd_040_01_CA_C01.mpt',
                                 'AW_Pd_042_05_CA_C01.mpt',
                                 'AW_Pd_042_03_CA_C01.mpt',
                                 'AW_Pd_042_02_CVA_C01.mpt',
                                 'AW_Pd_041_05_CA_C01.mpt',
                                 'AW_Pd_041_03_CA_C01.mpt',
                                 'AW_Pd_041_02_CVA_C01.mpt',
                                 'AW_Pd_045_05_CA_C01.mpt',
                                 'AW_Pd_045_03_CA_C01.mpt',
                                 'AW_Pd_045_02_CVA_C01.mpt',
                                 'AW_Pd_044_05_CA_C01.mpt',
                                 'AW_Pd_044_03_CA_C01.mpt',
                                 'AW_Pd_044_02_CVA_C01.mpt',
                                 'AW_Pd_043_05_CA_C01.mpt',
                                 'AW_Pd_043_03_CA_C01.mpt',
                                 'AW_Pd_043_02_CVA_C01.mpt'
                                 ],
             '20170831_Pd_039': ['AW_Pd_039_05_CA_C01.mpt',
                                 'AW_Pd_039_02_CVA_C01.mpt',
                                 'AW_Pd_039_03_CA_C01.mpt'
                                 ],
             '20171003_Pd_047': ['20171003_AW_Pd047_COstripping_test_04_CVA_C01.mpt',
                                 '20171003_AW_Pd047_COstripping_test_02_CVA_C01.mpt',
                                 '20171003_AW_Pd047_COstripping_test_03_CVA_C01.mpt'
                                 ],
             '20171010_Pd_051': ['20171010_AW_Pd051_06_CA_C01.mpt',
                                 '20171010_AW_Pd051_08_CVA_C01.mpt',
                                 '20171010_AW_Pd051_02_CA_C01.mpt',
                                 '20171010_AW_Pd051_04_CVA_C01.mpt',
                                 '20171010_AW_Pd051_05_CVA_C01.mpt'
                                 ],
             '20171003_Pd_048': ['20171003_AW_Pd048_COstripping_test_04_CVA_C01.mpt',
                                 '20171003_AW_Pd048_COstripping_test_02_CVA_C01.mpt',
                                 '20171003_AW_Pd048_COstripping_test_05_CVA_C01.mpt'
                                 ]

             
             }



# custom labels for data: dictionary correlating filename with label to be assigned:

data_label = {}
                                            

# plottype defines axis labels and settings. can be either ca or cv. to be evaluated whether useful or not
plottype = "cv"


# settings for the plot
plot_settings = {'safeplot': False,
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



