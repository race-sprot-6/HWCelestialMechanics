from astroquery.vizier import Vizier
from astropy import units as u
import numpy as np
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

def m2f1(m, z, l):
    return z*10**(-0.4*m)*2.9975E-05/l**2
ra = 167.147458
dec = -58.975037

query_gaia = Vizier.query_region(SkyCoord(ra=ra, dec=dec, unit = (u.deg,u.deg), frame = 'icrs'), radius = 2*u.arcsec, catalog = 'I/345/gaia2')
query_wise = Vizier.query_region(SkyCoord(ra=ra, dec=dec, unit = (u.deg,u.deg), frame = 'icrs'), radius = 20*u.arcsec, catalog = 'II/311/wise')

#query = Vizier(columns=['*','+_r']).query_region(SkyCoord(ra=ra, dec=dec, unit = (u.deg,u.deg), frame = 'icrs'), radius = 200*u.arcsec, catalog = 'I/345/gaia2')

#print(query_gaia[0])
#print(query_gaia[0].columns)
print(query_gaia[0]['e_Gmag', 'e_BPmag', 'e_RPmag'][0])
phot_gaia = np.array(list(query_gaia[0]['Gmag', 'BPmag', 'RPmag'][0]))
e_gaia = np.array(list(query_gaia[0]['e_Gmag', 'e_BPmag', 'e_RPmag'][0]))
ZeroP_gaia = np.array([3599.12, 3256.01, 2530.35])
EffW_gaia = np.array([5041.61, 5850.88, 7690.74])
Flux_gaia = m2f1(phot_gaia, ZeroP_gaia, EffW_gaia)
Flux_gaiaP = m2f1(phot_gaia-e_gaia, ZeroP_gaia, EffW_gaia)
#Flux_gaiaM = m2f1(phot_gaia-e_gaia, ZeroP_gaia, EffW_gaia)
e_flux_gaia = Flux_gaiaP - Flux_gaia

#print(query_wise[0])
#print(query_wise[0].columns)
#print(query_wise[0]['W1mag', 'W2mag', 'W3mag', 'W4mag'][0]) #там ещё есть фильтры. ?
phot_wise = np.array(list(query_wise[0]['W1mag', 'W2mag', 'W3mag', 'W4mag'][0]))
e_wise = np.array(list(query_wise[0]['e_W1mag', 'e_W2mag', 'e_W3mag', 'e_W4mag'][0]))
ZeroP_wise = np.array([309.54, 171.79, 31.67, 8.36])
EffW_wise = np.array([33526.00, 46028.00, 115608.00, 220883.00])
Flux_wise = m2f1(phot_wise, ZeroP_wise, EffW_wise)
Flux_wiseP = m2f1(phot_wise-e_wise, ZeroP_wise, EffW_wise)
e_flux_wise = Flux_wiseP - Flux_wise

plt.plot(EffW_gaia, Flux_gaia, 'r.')
plt.errorbar(EffW_gaia, Flux_gaia, yerr=e_flux_gaia, errorevery = 1, markeredgewidth = 20, linestyle = "")
plt.plot(EffW_wise, Flux_wise, 'b.')
plt.errorbar(EffW_wise, Flux_wise, yyerr=e_flux_wise, errorevery = 1, markeredgewidth = 20, linestyle = "")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$\lambda,\AA$')
plt.ylabel('$flux,erg/cm^2/s/A$')
plt.show()


