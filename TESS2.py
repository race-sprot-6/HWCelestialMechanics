import lightkurve as lk
#matplotlib inline
import numpy as np
search_result = lk.search_lightcurve('WASP-126', mission ='TESS', sector=27 )
search_result

lc = search_result[0].download()
plt = lc
#plt.title('Исходная кривая блеска', fontsize=20, fontname='Times New Roman')

plt.plot()