# -*- coding: utf-8 -*-
"""
Created on Tue Oct  18 19:25:46 2016

@author: Anna

Plotting of CV and CA data recorded with EC-lab and safed as .mpt file

Settings for the data to plot are inserted here. The data plotting is done using functions stored in anna_data_plot_functions.
"""

from pandas import DataFrame

import anna_data_plot_functions as dpf

# general information  if applicable, otherwise comment
# temperature
temperature = 25  # C

# reference electrode
e_rhe_ref = -0.720  # V
ph_ref = 1

# electrolyte
info = "0.1 M HClO_{4}"  # to be printed in annotations
ph = 0.96

# electrode area in cm2
electrode_area_geom = 20  # cm2
electrode_area_ecsa = 500  # cm2 NOT IMPLEMENTED YET

#ohmic drop in Ohm over cell measured with EIS
ohm_drop_corr = True #to turn on/off ohmic drop correction
ohmicdrop = 50
ohmicdrop_filename = {}
             
#insert filename in list if starting time is notzero, AND should be plotted as nonzero (ie NOT BE CHANGED)
no_timezero = {'i_CA_Pd_025_Ar_propenepurge_02_CA_C01.mpt'}             

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

# custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
#electrode area (geom and ecsa), ohmic drop to correct for

filespec_settings = {'AW_Pd_046_02_CVA_C01.mpt':{'label': "",
                                                 'cycles to extract': [1,2,5,9],
                                                 'electrode area geom': 1, 'electrode area ecsa': 10,
                                                 'individual ohmicdrop':40}}
                                            

#TODO: automatically detect which is the CO strip and the reference cycle based on the potential holde period in the cycle??


# settings for the plot
plot_settings = {'safeplot': False,
                 'plotname': 'CV_Pd_038_Propene_development_scanrate_UPL_1.4Vrhe',
                 'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                 'grid': True,
                 'second axis':  False,
                 'x_lim': (0.3, 1.6),
                 'y_lim': (-6.0, 6),
                 'y2_lim': (-3, 3),
                 'top_pad': 0.2,
                 'bottom_pad': 0.1,
                 'l_pad': [],
                 'r_pad': [],
                 'colors': ['g', 'orange'],#, 'r', 'b', 'k', 'g', 'orange', 'r', 'b', 'k', 'c', 'm', '0.50',"#538612", '0.75'],
                 'linestyle': ['-', ':'],
                 # color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
                 # color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
                 #options to select which data is plotted
                 'plot type': "cv", #possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
                 #custom column selection, will overrule plottype, if given. Possibilities are all data column names,
                 #most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
                 # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
                 'x_data':"",
                 'y_data':"i/mAcm^-2_geom",
                 'x_data2':"", #not implemented yet
                 "y_data2":"i/mAcm^-2_ECSA"
                 }

# legend:
legend_settings = {'position1': (0, 1.15),
                   'position2': (0, -0.15), #position of the legend for the second y axis
                   'number_of_cols': 2,
                   'fontsize': 8
                   }

# annotations: dictionary of annotation plus relevant properties in list form CURRENTLY NOT USED!?!?
annotation_settings = {'annotation 1': ["scanrate"],
                       #E-range for finding the delta i in the capacitance region for estimation of surface area
                       'e_range': [0.99, 1.01] #works only if scan starts at lowest potential
                       }


# todo: subplot possibility


def main():
    #create list of data dictionaries for plotting
        #loop through datafiles
        #import data
    # list of dictionaries for each file/loop that was chosen to be plotted, each containing filename(+cycle), DataFrame of all extracted data (all data columns), and file specific settings (unaltered) as given in input as "settings".
    #actual data in form of DataFrame for further treatment with the functions from data plot. if sync metadata is to be implemented the conversion has to be moved to later stage
    datalist = dpf.extract_data(folder_path, filenames, folders, filespec_settings)
    # print(datalist)

    # #treat data (now functions from data plot, future sync metadate from EC_MS package?, also depending of data-type)
    for file in datalist:
        #ohmic drop correction
        if 'ohm_drop_corr':
            print("Carrying out ohmic drop correction")
            file['data'] = file['data'].add(dpf.ohmicdrop_correct_e(file, ohmicdrop), fill_value=0)
            # print(file['data'])

        #conversion to rhe scale TODO: make it possible to choose pH and reference individually!
        file['data'] = file['data'].add(DataFrame([file['data']['Ewe/V'].apply(dpf.convert_potential_to_rhe)],
                                                  index=['EvsRHE/V']).T, fill_value=0)
        if 'ohm_drop_corr':
            file['data'] = file['data'].add(DataFrame([file['data']['E_corr/V'].apply(dpf.convert_potential_to_rhe)],
                                                      index=['E_corr_vsRHE/V']).T, fill_value=0)
        # print(file['data'])
        print(file['filename'])

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


    #plot the data from the list of data dictionaries
    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr)

    # try:
    # except IndexError:


if __name__ == "__main__":
    main()



