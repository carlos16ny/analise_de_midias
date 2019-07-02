from getCurrentPoulation import Locations
import os
import pandas as pd

global_path = os.getcwd()

diabetesDir1 = '/diabetes/incidence/'
diabetesDir2 = '/diabetes/prevalence/'
obesityDir   = '/obesity/'

fileO = pd.read_excel(global_path + obesityDir + list(Locations.keys())[0] + '.xlsx')
print(pd.DataFrame(fileO.values))

