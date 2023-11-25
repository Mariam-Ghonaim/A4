from astropy.table import Table
import os
filename='Gaia_bLT10_pGT5.fits'
if not os.path.isfile(filename):
gaia_data=Table.read('File-Path'+filename)
gaia_data.write(filename)
else:
gaia_data=Table.read(filename)