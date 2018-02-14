'''
generate graph based on x and y automatically

'''


import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib as mpl


path = "/Users/xu/DLearning/skydisc_intern/pomp"

# save the csv file name to a list called filenames
filenames = []
for file in os.listdir(path):
    if file.endswith(".CSV"):
        filenames.append(file)
        print(file)

# for every file, read is as csv to pandas, and plot the graph to specific folder
for file in filenames:
    # use beautifile color style
    mpl.style.use('seaborn-darkgrid')

    # because the header have some probelem with encoding due to hanzi, so I don't use header and delete it
    df = pd.read_csv(os.path.join(path, file), encoding ='latin1', header= None, skiprows=1)
    file_path = os.path.join(path,"graph", file)
    base_name = os.path.basename(file_path)
    file_name = os.path.splitext(base_name)[0]

    plt.title(file_name)
    plt.ylabel('CHI(V)')
    plt.xlim(0.0, 1.6)# set axis limits
    plt.xlabel('time(seconds)')

    plt.plot(df[0], df[1])
    plt.savefig(os.path.splitext(file_path)[0]+'.png')
    print('save png to: '+ os.path.splitext(file_path)[0]+'.png')
    # plt.clf() is important. Because matplotlib will remember the style you used previous time
    # so if don't clear it, the color of granph will change every time.
    plt.clf()
