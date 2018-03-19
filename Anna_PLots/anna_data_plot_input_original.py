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

load_new_data = False #False if saved set of data files should be used.
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

    folder_path = r'\\dtu-storage\annawi\Desktop\Projects\Propene oxidation\Experiments\Pd-electrodes\Systematic Study NovDec2017'

    folders = [
                # '20171122_Pd_064',
                # '20171122_GC_005',
                # '20171123_Pd_065',
                # '20171123_Pd_066',
                #'20171127_Pd_068b',
                # '20171203_Pd_069',
                # '20171203_Pd_070',
                # '20171212_Pd_073',
                # '20171213_Pd_074',
                # '20171213_Pd_075',
                # '20171214_Pd_076',
                # '20171214_Pd_077',
                # '20171214_Pd_078',
                # '20171219_Pd_079',
                # '20171219_Pd_080',
                # '20180103_Pd_081',
                # '20180103_Pd_082',
                # '20180104_Pd_084',
                # '20180104_Pd_085',
                # '20180110_Pd_089',
                # '20180109_Pd_086',
                # '20180111_Pd_090',
                # '20180109_Pd_087',
                # '20180111_Pd_091'
                '20180124_Pd_092',
                '20180124_Pd_093',
                # '20180130_Pd_094',
                # '20180130_Pd_095',
                # '20180130_Pd_096',
                # '20180131_Pd_097',
                # '20180131_Pd_098',
                # '20180201_Pd_099',
                # '20180201_Pd_100',
                # '20180208_Pd_101',
                # '20180209_Pd_102',
                # '20180216_Pd_103',
                # '20180220_Pd_104',
                # '20180220_Pd_105',
                # '20180222_Pd_106',
                # '20180222_Pd_107',
                # '20180222_Pd_108',
                # '20180223_Pd_109',
                # '20180226_Pd_110',
                # '20180226_Pd_112',
                # '20180226_Pd_113',
                # '20180227_Pd_114',
                # '20180227_Pd_115',
    ]  # list of folders from which data is going to be plotted

    filenames = OrderedDict([

                            ('20171122_Pd_064', ['20171122_Pd_064_05_CA_C01.mpt',
                                                 # '20171122_Pd_064_04_CA_C01.mpt'
                                                 ]),
                            ('20171123_Pd_065', [#'20171123_Pd_065_04_CA_C01.mpt',
                                                 '20171123_Pd_065_05_CA_C01.mpt'
                                                 ]),
                            ('20171123_Pd_066', [#'20171123_Pd_066_04_CA_C01.mpt',
                                                 '20171123_Pd_066_05_CA_C01.mpt'
                                                 ]),
                             #('20171127_Pd_068b', ['20171127_Pd_068_b_02_CA_C01.mpt',
                                                   # '20171127_Pd_068_b_04_CA_C01.mpt',
                                                   # '20171127_Pd_068_b_05_CA_C01.mpt'
                                                   # ]),
                             ('20171203_Pd_069', [#'20171203_Pd_069_02_CA_C01.mpt',
                                                  # '20171203_Pd_069_04_CA_C01.mpt',
                                                  '20171203_Pd_069_05_CA_C01.mpt'
                                                  ]),
                             ('20171203_Pd_070', [#'20171203_Pd_070_02_CA_C01.mpt',
                                                  # '20171203_Pd_070_04_CA_C01.mpt',
                                                  '20171203_Pd_070_05_CA_C01.mpt'
                                                  ]),
                             ('20171212_Pd_073', [#'20171212_AW_Pd_073_02_CA_C01.mpt',
                                                  #'20171212_AW_Pd_073_04_CA_C01.mpt',
                                                  '20171212_AW_Pd_073_05_CA_C01.mpt',
                                                  # '20171212_AW_Pd_073_SA_eval_04_CVA_C01.mpt'
                                                  ]),
                             ('20171213_Pd_074', ['20171213_AW_Pd_074_05_CA_C01.mpt',
                                                   #'20171213_AW_Pd_074_04_CA_C01.mpt',
                                                   #'20171213_AW_Pd_074_SA_eval_04_CVA_C01.mpt'
                                                 ]),
                             # ('20171213_Pd_075', ['20171213_AW_Pd_075_SA_eval_04_CVA_C01.mpt',
                             #                        # '20171213_AW_Pd_075_05_CA_C01.mpt',
                             #                        # '20171213_AW_Pd_075_04_CA_C01.mpt',
                             #                        # '20171213_AW_Pd_075_02_CA_C01.mpt'
                             #                        ]),
                             ('20171214_Pd_076', [#'20171214_AW_Pd_076_SA_eval_04_CVA_C01.mpt',
                                                  # '20171214_AW_Pd_076_02_CA_C01.mpt',
                                                  #'20171214_AW_Pd_076_04_CA_C01.mpt',
                                                  '20171214_AW_Pd_076_05_CA_C01.mpt'
                                                  ]),

                             ('20171214_Pd_077', ['20171214_AW_Pd_077_05_CA_C01.mpt',
                                                  # '20171214_AW_Pd_077_OCV_C01.mpt',
                                                  # '20171214_AW_Pd_077_04_CA_C01.mpt',
                                                  # '20171214_AW_Pd_077_SA_eval_05_OCV_C01.mpt',
                                                  # '20171214_AW_Pd_077_SA_eval_04_CVA_C01.mpt',
                                                  # '20171214_AW_Pd_077_02_CA_C01.mpt'
                                                  ]),
                             ('20171214_Pd_078', ['20171214_AW_Pd_078_05_CA_C01.mpt',
                                                  # '20171214_AW_Pd_078_04_CA_C01.mpt',
                                                  # '20171214_AW_Pd_078_02_CA_C01.mpt',
                                                  # '20171214_AW_Pd_078_SA_eval_05_OCV_C01.mpt',
                                                  # '20171214_AW_Pd_078_SA_eval_04_CVA_C01.mpt'
                                                  ]),
                             ('20171219_Pd_079', [#'20171219_AW_Pd_079_CA_eval_04_CVA_C01.mpt',
                                                  '20171219_AW_Pd_079_05_CA_C01.mpt',
                                                  # '20171219_AW_Pd_079_02_CA_C01.mpt',
                                                  # '20171219_AW_Pd_079_04_CA_C01.mpt',
                                                  # '20171219_AW_Pd_079_CA_eval_05_OCV_C01.mpt'
                                                  ]),
                             ('20171219_Pd_080',
                                                ['20171219_AW_Pd_080_05_CA_C01.mpt',
                                                 # '20171219_AW_Pd_080_02_CA_C01.mpt',
                                                 # '20171219_AW_Pd_080_04_CA_C01.mpt',
                                                 # '20171219_AW_Pd_080_SAeval_05_OCV_C01.mpt',
                                                 # '20171219_AW_Pd_080_SAeval_04_CVA_C01.mpt'
                                                 ]),
                             ('20180103_Pd_081', [#'20180103_POR_Pd_081_02_CA_C01.mpt',
                                                  '20180103_POR_Pd_081_03_CA_C01.mpt',
                                                  # '20180103_POR_Pd_081_SAeval_04_CVA_C01.mpt',
                                                  # '20180103_POR_Pd_081_SAeval_05_OCV_C01.mpt'
                                                  ]),
                             # ('20180103_Pd_082', [#'20180103_POR_Pd_082_02_CA_C01.mpt',
                             #                      # '20180103_POR_Pd_082_03_CA_C01.mpt',
                             #                      '20180103_POR_Pd_082_SAeval_04_CVA_C01.mpt',
                             #                      # '20180103_POR_Pd_082_SAeval_05_OCV_C01.mpt'
                             #                      ]),
                             ('20180104_Pd_084', [#'20180104_POR_Pd_084_02_CA_C01.mpt',
                                                  '20180104_POR_Pd_084_03_CA_C01.mpt',
                                                  # '20180104_POR_Pd_084_SAeval_04_CVA_C01.mpt',
                                                  # '20180104_POR_Pd_084_SAeval_05_OCV_C01.mpt'
                                                  ]),
                             ('20180104_Pd_085',  [#'20180104_POR_Pd_085_02_CA_C01.mpt',
                                                   '20180104_POR_Pd_085_03_CA_C01.mpt',
                                                   # '20180104_POR_Pd_085_SAeval_04_CVA_C01.mpt',
                                                   # '20180104_POR_Pd_085_SAeval_05_OCV_C01.mpt'
                                                   ]),
                             # ('20180109_Pd_086', ['20180109_POR_Pd_086_100muMPdCl2_03_CA_C01.mpt',
                             #                     '20180109_POR_Pd_086_100muMPdCl2_02_CA_C01.mpt',
                             #                     '20180109_POR_Pd_086_SAeval_05_OCV_C01.mpt',
                             #                     '20180109_POR_Pd_086_SAeval_04_CVA_C01.mpt'
                             #                     ]),
                             # ('20180109_Pd_087', ['20180109_POR_Pd_087b_SAeval_04_CVA_C01.mpt',
                             #                         '20180109_POR_Pd_087b_SAeval_05_OCV_C01.mpt',
                             #                         '20180109_POR_Pd_087b_100muMPdCl2_02_CA_C01.mpt',
                             #                         '20180109_POR_Pd_087b_100muMPdCl2_03_CA_C01.mpt'
                             #                         ]),
                             # ('20180110_Pd_089',   ['20180110_Pd_089_SA_eval_acid_04_CVA_C01.mpt',
                             #                        '20180110_Pd_089_SA_eval_acid_05_OCV_C01.mpt',
                             #                        '20180110_Pd_089_PO4_04_CA_C01.mpt',
                             #                        '20180110_Pd_089_PO4_05_CA_C01.mpt'
                             #                        ]),
                             #
                             # ('20180111_Pd_090',   ['20180111_Pd_090_SAeval_acid_04_CVA_C01.mpt',
                             #                        '20180111_Pd_090_SAeval_acid_05_OCV_C01.mpt',
                             #                        '20180111_Pd_090_PO4_04_CA_C01.mpt',
                             #                        '20180111_Pd_090_PO4_05_CA_C01.mpt'
                             #                        ]),
                             #
                             # ('20180111_Pd_091',    ['20180111_Pd_091_PO4_05_CA_C01.mpt',
                             #                         '20180111_Pd_091_SAeval_acid_04_CVA_C01.mpt',
                             #                         '20180111_Pd_091_SAeval_acid_05_OCV_C01.mpt',
                             #                         '20180111_Pd_091_PO4_04_CA_C01.mpt'
                             #                         ])

                               ('20180124_Pd_092',  ['20180124_Pd_092_04_CVA_C01.mpt',
                                                     # '20180124_Pd_092_02_CA_C01.mpt',
                                                     # '20180124_Pd_092_05_CA_C01.mpt'
                                                     ]),

                               ('20180124_Pd_093', [#'20180124_Pd_093_02_CA_C01.mpt',
                                                     # '20180124_Pd_093_06_CA_C01.mpt',
                                                     '20180124_Pd_093_04_CVA_C01.mpt',
                                                     # '20180124_Pd_093_05_CA_C01.mpt'
                                                     ]),
                            #    ('20180130_Pd_094', ['20180130_Pd_094_SAeval_05_OCV_C01.mpt',
                            #                         '20180130_Pd_094_SAeval_04_CVA_C01.mpt',
                            #                         '20180130_Pd_094_25mM_allyl_alcohol_03_CA_C01.mpt',
                            #                         '20180130_Pd_094_25mM_allyl_alcohol_02_CA_C01.mpt'
                            #                         ]),
                            #    ('20180130_Pd_095', ['20180130_Pd_095_02_CA_C01.mpt',
                            #                         '20180130_Pd_095_SA_eval_05_OCV_C01.mpt',
                            #                         '20180130_Pd_095_SA_eval_04_CVA_C01.mpt',
                            #                         '20180130_Pd_095_03_CA_C01.mpt'
                            #                         ]),
                            #    ('20180130_Pd_096', ['20180130_Pd_096_SAeval_04_CVA_C01.mpt',
                            #                         '20180130_Pd_096_02_CA_C01.mpt',
                            #                         '20180130_Pd_096_SAeval_05_OCV_C01.mpt'
                            #                         ]),
                            #    ('20180131_Pd_097', ['20180131_Pd_097_02_CA_C01.mpt',
                            #                         '20180131_Pd_097_SAeval_04_CVA_C01.mpt',
                            #                         '20180131_Pd_097_SAeval_05_OCV_C01.mpt'
                            #                         ]),
                            #
                            #     ('20180131_Pd_098', ['20180131_Pd_098_02_CA_C01.mpt',
                            #                          '20180131_Pd_098_03_CA_C01.mpt',
                            #                   '20180131_Pd_098_SAeval_04_CVA_C01.mpt',
                            #                   '20180131_Pd_098_SAeval_05_OCV_C01.mpt'
                            #                          ]),
                            #    ('20180201_Pd_099', ['20180201_Pd_099_02_CA_C01.mpt',
                            #                         '20180201_Pd_099_SAeval_04_CVA_C01.mpt',
                            #                         '20180201_Pd_099_SAeval_05_OCV_C01.mpt'
                            #                         ]),
                            #   ('20180201_Pd_100', [#'20180201_Pd_100_02_CA_C01.mpt',
                            #                        '20180201_Pd_100_saeval_04_CVA_C01.mpt',
                            #                        # '20180201_Pd_100_saeval_05_OCV_C01.mpt'
                            #                        ]),
                            # ('20180208_Pd_101', [#'20180208_Pd_101_03_CA_C01.mpt',
                            #                      # '20180208_Pd_101_02_CA_C01.mpt',
                            #                      # '20180208_Pd_101_SAeval_05_OCV_C01.mpt',
                            #                      '20180208_Pd_101_SAeval_04_CVA_C01.mpt'
                            #                     ]),
                            #  ('20180209_Pd_102', [#'20180209_Pd_102_02_CA_C01.mpt',
                            #                       '20180209_Pd_102_03_CA_C01.mpt',
                            #                       # '20180209_Pd_102_saeval_04_CVA_C01.mpt',
                            #                       # '20180209_Pd_102_saeval_05_OCV_C01.mpt'
                            #                     ]),
                            #   ('20180216_Pd_103', ['20180216_Pd_103_03_CA_C01.mpt',
                            #                        # '20180216_Pd_103_02_CA_C01.mpt',
                            #                        # '20180216_Pd_103_SAeval_05_OCV_C01.mpt',
                            #                        # '20180216_Pd_103_SAeval_04_CVA_C01.mpt'
                            #                        ]),
                            # ('20180220_Pd_104', [#'20180220_Pd_104_05_CA_C01.mpt',
                            #                      '20180220_Pd_104_SAeval_04_CVA_C01.mpt',
                            #                      # '20180220_Pd_104_SAeval_05_OCV_C01.mpt',
                            #                      # '20180220_Pd_104_01_SPEIS_C01.mpt',
                            #                      # '20180220_Pd_104_02_CA_C01.mpt',
                            #                      # '20180220_Pd_104_04_CA_C01.mpt'
                            #                      ]),
                            # ('20180220_Pd_105', [#'20180220_Pd_105_02_CA_C01.mpt',
                            #                      # '20180220_Pd_105_04_CA_C01.mpt',
                            #                      # '20180220_Pd_105_05_CA_C01.mpt',
                            #                      '20180220_Pd_105_SAeval_04_CVA_C01.mpt',
                            #                      # '20180220_Pd_105_SAeval_05_OCV_C01.mpt',
                            #                      # '20180220_Pd_105_01_SPEIS_C01.mpt'
                            #                      ]),
                            # ('20180222_Pd_106', [#'20180222_Pd_106_SAeval_04_CVA_C01.mpt',
                            #                        # '20180222_Pd_106_SAeval_05_OCV_C01.mpt',
                            #                        # '20180222_Pd_106_02_CA_C01.mpt',
                            #                         '20180222_Pd_106_03_CA_C01.mpt'
                            #                      ]),
                            ('20180222_Pd_107', [#'20180222_Pd_107_03_CA_C01.mpt',
                                                 '20180222_Pd_107_SAeval_04_CVA_C01.mpt',
                                                 # '20180222_Pd_107_SAeval_05_OCV_C01.mpt',
                                                 # '20180222_Pd_107_02_CA_C01.mpt'
                                                 ]),
                            # ('20180222_Pd_108', [#'20180222_Pd_108_03_CA_C01.mpt',
                            #                       '20180222_Pd_108_SAeval_04_CVA_C01.mpt',
                            #                       # '20180222_Pd_108_SAeval_05_OCV_C01.mpt',
                            #                       # '20180222_Pd_108_02_CA_C01.mpt'
                            #                      ]),
                            # ('20180223_Pd_109',[#'20180223_Pd_109_03_CA_C01.mpt',
                            #                     # '20180223_Pd_109_02_CA_C01.mpt',
                            #                     # '20180223_Pd_109_SAeval_05_OCV_C01.mpt',
                            #                     '20180223_Pd_109_SAeval_04_CVA_C01.mpt'
                            #                     ]),
                            # ('20180226_Pd_110', [#'20180224_Pd_110_SAeval_05_OCV_C01.mpt',
                            #                      '20180224_Pd_110_SAeval_04_CVA_C01.mpt',
                            #                      # '20180224_Pd_110_03_CA_C01.mpt',
                            #                      # '20180224_Pd_110_02_CA_C01.mpt'
                            #                      ]),
                            ('20180226_Pd_112', [#'20180226_POR_Pd_112_SAeval_04_CVA_C01.mpt',
                                                 # '20180226_POR_Pd_112_SAeval_05_OCV_C01.mpt',
                                                 # '20180226_POR_Pd_112_02_CA_C01.mpt',
                                                 '20180226_POR_Pd_112_03_CA_C01.mpt'
                                                 ]),
                            ('20180226_Pd_113', ['20180226_POR_Pd_113_03_CA_C01.mpt',
                                                 # '20180226_POR_Pd_113_SAeval_04_CVA_C01.mpt',
                                                 # '20180226_POR_Pd_113_SAeval_05_OCV_C01.mpt',
                                                 # '20180226_POR_Pd_113_02_CA_C01.mpt'
                                                 ]),
                            ('20180227_Pd_114', ['20180227_POR_Pd_114_03_CA_C01.mpt',
                                                 #'20180227_POR_Pd_114_SAeval_04_CVA_C01.mpt',
                                                 # '20180227_POR_Pd_114_SAeval_05_OCV_C01.mpt',
                                                 # '20180227_POR_Pd_114_02_CA_C01.mpt'
                                                 ]),
                            ('20180227_Pd_115', ['20180227_POR_Pd_115_03_CA_C01.mpt',
                                                 # '20180227_POR_Pd_115_SAeval_04_CVA_C01.mpt',
                                                 # '20180227_POR_Pd_115_SAeval_05_OCV_C01.mpt',
                                                 # '20180227_POR_Pd_115_02_CA_C01.mpt'
                                                 ]),
    ])




    # custom settings for data files: dictionary correlating filename with custom label, cycles to extract from CV file,
    #electrode area (geom and ecsa), ohmic drop to correct for

    filespec_settings = {'20171122_Pd_064_05_CA_C01.mpt': {'label': "1.10 V/RHE (064))",
                                                     # 'cycles to extract': [2],
                                                     'electrode area geom': 2, 'electrode area ecsa': 64.75,
                                                      #'individual ohmicdrop': 43.3
                                                    },
                        '20171123_Pd_065_05_CA_C01.mpt': {'label': "0.70 V/RHE (065))",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2, 'electrode area ecsa': 64.75,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                        '20171123_Pd_066_05_CA_C01.mpt': {'label': "1.20 V/RHE (066))",
                                                                # 'cycles to extract': [2],
                                                                'electrode area geom': 2, 'electrode area ecsa': 64.75,
                                                                # 'individual ohmicdrop': 43.3
                                                                },
                        '20171203_Pd_069_05_CA_C01.mpt': {'label': "0.85 V/RHE (069))",
                                                                 # 'cycles to extract': [2],
                                                                 'electrode area geom': 2, 'electrode area ecsa': 64.75,
                                                                 # 'individual ohmicdrop': 43.3
                                                                 },
                        '20171203_Pd_070_05_CA_C01.mpt': {'label': "1.00 V/RHE (070))",
                                                                  # 'cycles to extract': [2],
                                                                  'electrode area geom': 2,
                                                                  'electrode area ecsa': 64.75,
                                                                  # 'individual ohmicdrop': 43.3
                                                                  },
                        '20171212_AW_Pd_073_05_CA_C01.mpt': {'label': "0.90 V/RHE (073))",
                                                     # 'cycles to extract': [2],
                                                     'electrode area geom': 2, 'electrode area ecsa': 87.88,
                                                      #'individual ohmicdrop': 43.3
                                                    },
                         '20171213_AW_Pd_074_05_CA_C01.mpt': {'label': "0.70 V/RHE (074)",
                                                            # 'cycles to extract': [3],
                                                           'electrode area geom': 2, 'electrode area ecsa': 51.04,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171213_AW_Pd_075_05_CA_C01.mpt': {'label': "0.95 V/RHE (075)",
                                                           # 'cycles to extract': [3],
                                                           'electrode area geom': 2, 'electrode area ecsa': 19.57,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171214_AW_Pd_076_05_CA_C01.mpt': {'label': "0.80 V/RHE (076)",
                                                            # 'cycles to extract': [3],
                                                           'electrode area geom': 2, 'electrode area ecsa': 91.26,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171214_AW_Pd_077_05_CA_C01.mpt': {'label': "0.85 V/RHE (077)",
                                                           # 'cycles to extract': [3],
                                                           'electrode area geom': 2, 'electrode area ecsa': 48.92,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171214_AW_Pd_078_05_CA_C01.mpt': {'label': "1.00 V/RHE (078)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 79.34,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171219_AW_Pd_079_05_CA_C01.mpt': {'label': "0.90 V/RHE (079)",
                                                                       # 'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 79.87,
                                                                       # 'individual ohmicdrop': 43.3
                                                                       },
                         '20171219_AW_Pd_080_05_CA_C01.mpt': {'label': "0.95 V/RHE (080)",
                                                                       # 'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 72.76,
                                                                       # 'individual ohmicdrop': 43.3
                                                                      },
                         '20180103_POR_Pd_081_03_CA_C01.mpt': {'label': "0.95 V/RHE (081)",
                                                              # 'cycles to extract': [2],
                                                              'electrode area geom': 2,
                                                              'electrode area ecsa': 69.55,
                                                              # 'individual ohmicdrop': 43.3
                                                              },
                         '20180104_POR_Pd_084_03_CA_C01.mpt': {'label': "0.80 V/RHE (084)",
                                                              # 'cycles to extract': [2],
                                                              'electrode area geom': 2,
                                                              'electrode area ecsa': 77.792,
                                                              # 'individual ohmicdrop': 43.3
                                                              },
                         '20180104_POR_Pd_085_03_CA_C01.mpt': {'label': "0.85 V/RHE (085)",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2,
                                                               'electrode area ecsa': 79.69,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                         '20180208_Pd_101_03_CA_C01.mpt': {'label': "0.8 V/RHE (101)",
                                                              # 'cycles to extract': [2],
                                                              'electrode area geom': 2,
                                                              'electrode area ecsa': 66.17,
                                                              # 'individual ohmicdrop': 43.3
                                                              },
                         '20180209_Pd_102_03_CA_C01.mpt': {'label': "0.79 V/RHE (102)",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2,
                                                               'electrode area ecsa': 49.81,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                         '20180216_Pd_103_03_CA_C01.mpt': {'label': "0.89 V/RHE (103)",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2,
                                                               'electrode area ecsa': 57.64,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                         '20180222_Pd_106_03_CA_C01.mpt': {'label': "0.89 V/RHE (106)",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2,
                                                               'electrode area ecsa': 58.88,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                         '20180222_Pd_107_03_CA_C01.mpt': {'label': "0.90 V/RHE, Ar (107)",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2,
                                                               'electrode area ecsa': 75.78,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                         '20180222_Pd_108_03_CA_C01.mpt': {'label': "0.90 V/RHE (108)",
                                                               # 'cycles to extract': [2],
                                                               'electrode area geom': 2,
                                                               'electrode area ecsa': 53.72,
                                                               # 'individual ohmicdrop': 43.3
                                                               },
                         '20180226_POR_Pd_112_03_CA_C01.mpt': {'label': "0.70 V/RHE (112)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2,
                                                           'electrode area ecsa': 78.27,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20180226_POR_Pd_113_03_CA_C01.mpt': {'label': "0.80 V/RHE (113)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2,
                                                           'electrode area ecsa': 46.78,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20180227_POR_Pd_114_03_CA_C01.mpt': {'label': "0.90 V/RHE (114)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2,
                                                           'electrode area ecsa': 74.18,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20180227_POR_Pd_115_03_CA_C01.mpt': {'label': "0.95 V/RHE (115)",
                                                           # 'cycles to extract': [2],
                                                           'electrode area geom': 2,
                                                           'electrode area ecsa': 32.38,
                                                           # 'individual ohmicdrop': 43.3
                                                           },

                         '20171212_AW_Pd_073_SA_eval_04_CVA_C01.mpt': {'label': "0.90 V/RHE (073))",
                                                     'cycles to extract': [2],
                                                     'electrode area geom': 2, 'electrode area ecsa': 0,
                                                      #'individual ohmicdrop': 43.3
                                                    },
                         '20171213_AW_Pd_074_SA_eval_04_CVA_C01.mpt': {'label': "0.70 V/RHE (074)",
                                                            'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171213_AW_Pd_075_SA_eval_04_CVA_C01.mpt': {'label': "0.95 V/RHE (075)",
                                                           'cycles to extract': [3],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171214_AW_Pd_076_SA_eval_04_CVA_C01.mpt': {'label': "0.80 V/RHE (076)",
                                                            'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171214_AW_Pd_077_SA_eval_04_CVA_C01.mpt': {'label': "0.85 V/RHE (077)",
                                                           'cycles to extract': [3],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171214_AW_Pd_078_SA_eval_04_CVA_C01.mpt': {'label': "1.00 V/RHE (078)",
                                                           'cycles to extract': [2],
                                                           'electrode area geom': 2, 'electrode area ecsa': 0,
                                                           # 'individual ohmicdrop': 43.3
                                                           },
                         '20171219_AW_Pd_079_CA_eval_04_CVA_C01.mpt': {'label': "0.90 V/RHE (079)",
                                                                       'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                       },
                         '20171219_AW_Pd_080_SAeval_04_CVA_C01.mpt': {'label': "0.95 V/RHE (080)",
                                                                       'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                      },
                         '20180103_POR_Pd_081_SAeval_04_CVA_C01.mpt': {'label': "0.95 V/RHE (081)",
                                                                       'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                      },
                         '20180103_POR_Pd_082_SAeval_04_CVA_C01.mpt': {'label': "0.95 V/RHE EDTA (082)",
                                                                       'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                       },
                         '20180104_POR_Pd_084_SAeval_04_CVA_C01.mpt': {'label': "0.80 V/RHE (084)",
                                                                       'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                      },
                         '20180104_POR_Pd_085_SAeval_04_CVA_C01.mpt': {'label': "0.85 V/RHE (085)",
                                                                       'cycles to extract': [2],
                                                                       'electrode area geom': 2,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                      },
                         '20180124_Pd_092_04_CVA_C01.mpt': {'label': "Pd foil (092, cycle 20)",
                                                                       'cycles to extract': [20],
                                                                       'electrode area geom': 1,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                       },
                         '20180124_Pd_093_04_CVA_C01.mpt': {'label': "Pd foil (093, cycle 10)",
                                                                       'cycles to extract': [10],
                                                                       'electrode area geom': 1,
                                                                       'electrode area ecsa': 0,
                                                                       # 'individual ohmicdrop': 43.3
                                                                       },
                         '20180201_Pd_100_saeval_04_CVA_C01.mpt': {'label': "Pd (100, cycle 3)",
                                                                   'cycles to extract': [3],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 0,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180208_Pd_101_SAeval_04_CVA_C01.mpt': {'label': "Pd (101, cycle 3)",
                                                            'cycles to extract': [3],
                                                            'electrode area geom': 2,
                                                            'electrode area ecsa': 0,
                                                            # 'individual ohmicdrop': 43.3
                                                            },
                         '20180209_Pd_102_saeval_04_CVA_C01.mpt': {'label': "Pd (102, cycle 4)",
                                                            'cycles to extract': [4],
                                                            'electrode area geom': 2,
                                                            'electrode area ecsa': 0,
                                                            # 'individual ohmicdrop': 43.3
                                                            },
                         '20180216_Pd_103_SAeval_04_CVA_C01.mpt': {'label': "Pd (103, cycle 3)",
                                                            'cycles to extract': [3],
                                                            'electrode area geom': 2,
                                                            'electrode area ecsa': 0,
                                                            # 'individual ohmicdrop': 43.3
                                                            },
                         '20180220_Pd_104_SAeval_04_CVA_C01.mpt': {'label': "Pd (104, cycle 3)",
                                                            'cycles to extract': [3],
                                                            'electrode area geom': 2,
                                                            'electrode area ecsa': 0,
                                                            # 'individual ohmicdrop': 43.3
                                                            },
                         '20180220_Pd_105_SAeval_04_CVA_C01.mpt': {'label': "Pd (105, cycle 3)",
                                                            'cycles to extract': [3],
                                                            'electrode area geom': 2,
                                                            'electrode area ecsa': 0,
                                                            # 'individual ohmicdrop': 43.3
                                                            },
                         '20180222_Pd_106_SAeval_04_CVA_C01.mpt': {'label': "Pd (106, cycle 8)",
                                                            'cycles to extract': [8],
                                                            'electrode area geom': 2,
                                                            'electrode area ecsa': 0,
                                                            # 'individual ohmicdrop': 43.3
                                                            },
                         '20180222_Pd_107_SAeval_04_CVA_C01.mpt': {'label': "Pd (107, cycle 10)",
                                                                   'cycles to extract': [10],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 75.78,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180222_Pd_108_SAeval_04_CVA_C01.mpt': {'label': "Pd (108, cycle 3)",
                                                                   'cycles to extract': [1],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 75.78,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180223_Pd_109_SAeval_04_CVA_C01.mpt': {'label': "Pd (109, cycle 3)",
                                                                   'cycles to extract': [3],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 0,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180224_Pd_110_SAeval_04_CVA_C01.mpt': {'label': "Pd (110, cycle 3)",
                                                                   'cycles to extract': [3],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 0,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180226_POR_Pd_112_SAeval_04_CVA_C01.mpt': {'label': "Pd (112, cycle 4)",
                                                                   'cycles to extract': [4],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 0,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180226_POR_Pd_113_SAeval_04_CVA_C01.mpt': {'label': "Pd (113, cycle 5)",
                                                                    'cycles to extract': [5],
                                                                    'electrode area geom': 2,
                                                                     'electrode area ecsa': 0,
                                                                     # 'individual ohmicdrop': 43.3
                                                                         },
                         '20180227_POR_Pd_114_SAeval_04_CVA_C01.mpt': {'label': "Pd (114, cycle 3)",
                                                                   'cycles to extract': [3],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 0,
                                                                   # 'individual ohmicdrop': 43.3
                                                                   },
                         '20180227_POR_Pd_115_SAeval_04_CVA_C01.mpt': {'label': "Pd (115, cycle 3)",
                                                                   'cycles to extract': [3],
                                                                   'electrode area geom': 2,
                                                                   'electrode area ecsa': 0,
                                                                   # 'individual ohmicdrop': 43.3
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
    # settings for the plot - CV settings
    plot_settings = {'safeplot': False,
                     'plotname': "20180319_CV_049-052_50mVps_cycles",
                     'coplot_evsrhe': False, #for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
                     'grid': True,
                     'second axis':  False,
                     'x_lim': (0.2, 1.6),
                     'y_lim': (-15, 10),
                     'y2_lim': (0, 0.025),
                     'top_pad': 0.2,
                     'bottom_pad': 0.1,
                     'l_pad': [],
                     'r_pad': [],
                     'colors': ['k','g', 'b', 'grey','orange', 'r', '#4a235a', 'k', 'c', '#538612', 'c', 'm', '0.50',"#538612", '0.75'],
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
                     "y_data2":""
                     }
    #settings for the plot - CA settings
    # plot_settings = {'safeplot': True,
    #                  'plotname': "20180307_CAs_for_PORonPd_article",
    #                  'coplot_evsrhe': False,
    #                  # for plottype ca: selection whether ohmic drop corrected EvsRHE is co-plotted
    #                  'grid': False,
    #                  'second axis': False,
    #                  'x_lim': (-100, 3700),
    #                  'y_lim': (-0.1, 10),
    #                  'y2_lim': (0, 0.025),
    #                  'top_pad': 0.2,
    #                  'bottom_pad': 0.1,
    #                  'l_pad': [],
    #                  'r_pad': [],
    #                  # 'colors': ['g', 'b', 'grey', 'orange', 'r', '#4a235a', 'k', 'c', '#538612', 'c', 'm', '0.50',
    #                  #            "#538612", '0.75'],
    #                  # 'colors': [ '#bd4de0' , 'k', 'orange', 'g', 'b', 'r', '#d816ff', "#ff8a16"],
    #                  # 'colors': ['#bd4de0', '#6b12ad', #purple
    #                  #            'grey', 'k',
    #                  #            'g', '#266f0e'
    #                  #            ],
    #                  # 'colors': ['#bd4de0', 'orange', '#d816ff', "#ff8a16"],
    #                  # 'colors': plt.cm.gist_earth(range(255, 10, 10)),
    #                  'colors': #plt.cm.Blues([50,100,150,200,250,255]),
    #                          [[0.10249904, 0.40868897, 0.68289121, 1.], #4
    #                           [0.59215688, 0.77708575, 0.87643215, 1.],  # 2
    #                           [0.03137255, 0.1882353, 0.41960785, 1.], #6
    #                           [0.03137255, 0.20853518, 0.4497501, 1.], #5
    #
    #                           [0.30611305, 0.60484431, 0.79492504, 1.], #3
    #                           [0,0,0,1.], #black
    #                           [0.81707037, 0.88589005, 0.95078816, 1.]], #1
    #
    #
    #                  'linestyle': ['-', '-'],
    #                  'colors2': ['0.25', 'grey', '0.75'],
    #                  'linestyle2': ['--', '--', '--'],
    #                  # color_list = plt.cm.YlGnBu(np.linspace(0, 1, 14))
    #                  # color_list = plt.cm.gist_earth(np.linspace(0, 1, 14))
    #
    #                  # options to select which data is plotted
    #                  'plot type': "cv",
    #                  # possibilies: ca or cv, for standard selection of columns: EvsRHE (E_corr vsRHE), i_geom and time/s
    #                  # custom column selection, will overrule plottype, if given. Possibilities are all data column names,
    #                  # most likely useful: "Ewe/V", "EvsRHE/V", "E_corr/V", "E_corr_vsRHE/V", "<I>/mA", "i/mAcm^-2_geom",
    #                  # "i/mAcm^-2_ECSA", "time/s", "(Q-Qo)/C"
    #                  'x_data': "time/s",
    #                  'y_data': "i/mAcm^-2_ECSA",
    #                  'x_data2': "",  # not implemented yet
    #                  "y_data2": ""
    #                  }

    # schwarz
    # 0.7
    # grün
    # 0.8
    # blau
    # 0.85
    # lila
    # 0.9
    # orange
    # 0.95
    # rot
    # 1.0



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


    #Calculate ESCA from a list of 2 data dictionaries (all further items in the list will be disregarded).
    esca_data = dpf.calc_esca(datalist[0:9], type='oxide_red', scanrate=50)
    print(esca_data)

    # esca_data=[] #uncomment if no calculation of esca to avoid error in EC_plot
    #plot the data from the list of data dictionaries
    # print(datalist)

    dpf.EC_plot(datalist, plot_settings, legend_settings, annotation_settings, ohm_drop_corr, esca_data)

    # dpf.current_at_time_plot(datalist, times=[60, 600, 3300], I_col="i/mAcm^-2_ECSA")


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



