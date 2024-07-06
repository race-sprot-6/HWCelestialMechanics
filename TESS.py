import lightkurve as lk
#matplotlib inline
import numpy as np
search_result = lk.search_lightcurve('WASP-126', mission ='TESS', sector=27 )
search_result

lc = search_result[0].download()
plt = lc
#plt.title('Исходная кривая блеска', fontsize=20, fontname='Times New Roman')

plt.plot()

lcnew = lc.remove_outliers(sigma_upper = 3)

plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
lcnew.plot()

ls = lcnew.to_periodogram(method = 'ls', minimum_period = 2, maximum_period = 10, )

ls.plot()

ls.period_at_max_power

P = lcnew.fold(period=1.6487962, epoch_time=2041.2)
P.plot()

lc120 = search_result[1].download()
lc120.plot()

lcnew120 = lc120.remove_outliers(sigma_upper = 3)
lcnew120.plot()

ls120 = lcnew120.to_periodogram(method = 'ls', minimum_period = 2, maximum_period = 10 )
ls120.plot()

Per = ls120.period_at_max_power
print(Per)
lcnew120 = lc120.remove_outliers(sigma_upper = 3)
lcnew120.plot()

P120 = lcnew120.fold(period=Per, epoch_time=2041.1)
P120.plot()

result = lk.search_targetpixelfile('WASP-126', mission ='TESS', sector=27, exptime = 120)
result

tpf = result[0].download()

tpf.plot()

#кривая блеска пайплайн
lcpipe = tpf.to_lightcurve(aperture_mask="pipeline")
lcpipe.plot()

#кривая блеска зресхолд
lcth = tpf.to_lightcurve(aperture_mask='threshold')
lcth.plot()

cut_mask = np.zeros(tpf[0].shape[1:], dtype='bool')
cut_mask[3:6,4:7] = True
cut_mask[6,5:7] = True
#cut_mask[3:6,8] = True
#cut_mask[1,4:7] = True
#cut_mask[7,4:7] = True
tpf.plot(aperture_mask =cut_mask)

#кривая блеска кастом
lcc = tpf.to_lightcurve(aperture_mask=cut_mask)
lcc.plot()

background_mask = ~tpf.create_threshold_mask(threshold=1)
tpf.plot(aperture_mask=background_mask, mask_color='w')

#вычитаем фон для тресхолд
#custom_pipeline = tpf.pipeline_mask
background_mask = ~tpf.create_threshold_mask(threshold=0.01)
#tpf.plot(aperture_mask=background_mask, mask_color='w')
custom_threshold = tpf.create_threshold_mask(threshold=10)

n_th_pixels = custom_threshold.sum() # количество пикселей в выбранной апертуре
n_background_pixels = background_mask.sum() # количество пикселей в маске фона
background_lc_per_pixel = tpf.to_lightcurve(aperture_mask=background_mask)  # кривая блеска фона в расчёте на 1 пиксель
background_lc = background_lc_per_pixel * n_th_pixels # фон, который необходимо вычесть из кривой блеска объекта
cor_lcth = lcth - background_lc.flux # кривая блеска объекта после учета фона
cor_lcth.plot()
print(n_th_pixels, n_background_pixels)

lcthnew = cor_lcth.remove_outliers(sigma_upper = 3)
lcthnew.plot()

lsthnew = lcthnew.to_periodogram(method = 'ls', minimum_period = 2, maximum_period = 6 )
lsthnew.plot()

Per = lsthnew.period_at_max_power
print(Per)

P120 = lcthnew.fold(period=Per, epoch_time=2054.5)
P120.plot()

