import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

url = 'https://www.twse.com.tw/exchangeReport/FMSRFK?&stockNo=6166'

resp = requests.get(url).json()
li = resp['data']
di = {}
for i in li:
    di[i[1]] = i[4]

df = pd.DataFrame.from_dict(di, orient = 'index', columns = ['VWAP'])
ntd = 10000
vwap = df['VWAP'].astype(float)
df['每月購買股數'] = np.floor(ntd / vwap)
df['累積股數'] = df['每月購買股數'].cumsum()
df['累積價值'] = round(df['累積股數'] * vwap, 2)
row = df.shape[0] + 1
df['原始價值'] = np.arange(ntd, ntd*row, ntd)

plt.figure(dpi = 200)
plt.plot(df['累積價值'], 'k-', lw = 1, label = '6166')
plt.plot(df['原始價值'], 'k--',lw = 1, label = 'original')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend(loc = 0) 
plt.grid()
plt.show()
