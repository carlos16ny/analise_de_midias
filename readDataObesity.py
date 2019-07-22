from getCurrentPoulation import Locations
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='carloshnpa', api_key='iVI5uPMVtoQakYLxGaPy')

global_path = os.getcwd()

diabetesDir = '/diabetes/prevalence/'
obesityDir   = '/obesity/'

labels = ["Total", "Low", "Up", "AVG"]

for location in Locations:

    read = pd.read_excel(global_path + obesityDir + location + '.xlsx', usecols=[74,75,76,77,78,79], nrows=11)
    anos = []
    pessoas = []
    low = []
    up = []
    obesos = []
    frame = pd.DataFrame(read)
    
    for i in range (1,11):
        anos.append(frame.iloc[i,0])
        pessoas.append(float(frame.iloc[i,5]) / 1000000)
        low.append(int(frame.iloc[i,3]) / 100 * pessoas[i-1]  )
        up.append(int(frame.iloc[i,4]) / 100 * pessoas[i-1] )
        obesos.append(int(frame.iloc[i,1]))
        
    total = go.Scatter(
        x = anos,
        y = pessoas,
        fill='tozeroy'
    )
    
    l = go.Scatter(
        x = anos,
        y = low,
        fill='tozeroy'
    )
    
    u = go.Scatter(
        x = anos,
        y = up,
        fill='tozeroy'
    )
    
    o = go.Scatter(
        x = anos,
        y = low,
        fill='tozeroy'
    )
    
    data = [total, l, u , o]
    py.iplot(data, filename='obesidade-{}'.format(location))

    anos.clear()
    pessoas.clear()
    low.clear()
    obesos.clear()
    up.clear()

