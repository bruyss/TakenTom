# -*- coding: utf-8 -*-
"""
Script to plot the simulated heads of a modflow 6 model (steady state)

Things to be adjusted by yourself:
    directory_S
    direcory_O
    model
    csv
    
    condition
    error
"""

import matplotlib.pyplot as plt
import flopy
import math
import pandas as pd
import numpy as np
import os

plt.rcParams['figure.dpi'] = 300

# path to the directory where your results are
directory_S = './'

# path to the directory where the observed heads are
directory_O = './'

# name of your model
model = 'Model_2024_ss_pump'
model = 'Taak'

# name of observed heads file (the one from Ufora)
csv = 'steady_state_calibration_RAW'

# open the simulation results
sim_out = flopy.utils.observationfile.Mf6Obs(os.path.join(directory_S, '{}.ob_gw_out_head.csv'.format(model)), isBinary=False)

# customize dataframe
sim_df = sim_out.get_dataframe().transpose()
sim_df.columns = ['natural', 'pumping']
sim_df = sim_df.iloc[1:]

index_labels = ["P1", "Pz10", "Pz11", "Pz12", "Pz2", "Pz3", "Pz4", "Pz5", "Pz6", "Pz7", "Pz8", "Pz9"] #CHANGE THIS SO IT MATCHES THE ORDER OF YOUR SIMULATED FILE
index_labels = ["P1", "Pz2", "Pz3", "Pz4", "Pz5", "Pz6", "Pz7", "Pz8", "Pz9", "Pz10", "Pz11", "Pz12"] #CHANGE THIS SO IT MATCHES THE ORDER OF YOUR SIMULATED FILE
sim_df.index=index_labels

#open the file with the observed heads
obs_df = pd.read_csv(os.path.join(directory_O, '{}.csv'.format(csv)),delimiter=';')
obs_df = obs_df.set_index('Unnamed: 0')

#calculate residual between simulated and observed heads
sim_df['natural_R'] = sim_df['natural'] - obs_df['natural']
sim_df['pumping_R'] = sim_df['pumping'] - obs_df['pumping']
#%%
#Create a basic scatter plot with Matplotlib comparing the observed and the simulated heads
#An identity line was created based on the minumum and maximum observed value
#Points markers are colored by the residual and a residual colorbar is added to the figure

#choose what you want to plot: pumping/natural condition
condition = 'pumping'
# which kind of error do you want to show in the plot: NRMSE/SSE (Root Mean Square Error or Sum of Squared Errors)
error = 'SSE'

# from here on you do not have to change anything anymore (but ofcourse you are always free to customize your plots further ;))

if error == 'NMRSE':
    MSE = np.square(sim_df['{}_R'.format(condition)]).mean()
    NMRSE = math.sqrt(MSE)
    error_value=NMRSE
elif error == 'SSE':
    error_value = np.sum(sim_df['{}_R'.format(condition)]**2)

obs_df = obs_df.loc[sim_df.index]
fig = plt.figure(figsize=(10,8))
x = np.linspace(sim_df['{}'.format(condition)].min()-0.5, sim_df['{}'.format(condition)].max()+0.5, 100)
plt.plot(x, x, linestyle='dashed')
plt.scatter(obs_df['{}'.format(condition)],sim_df['{}'.format(condition)], marker='o', c = sim_df['{}_R'.format(condition)])

cbar = plt.colorbar()
cbar.set_label('Residual (m)', fontsize=14)

plt.grid()
plt.xlabel('Observed Head (m)', fontsize=14)
plt.ylabel('Simulated Head (m)', fontsize=14)
plt.title('calibration {} conditions: {}={}'.format(condition, error, round(error_value,4)), fontsize=20)
fig.tight_layout()

plt.show()

#%%

