from __future__ import with_statement
import os
import numpy as np
from lsst.sims.catUtils.utils import ObservationMetaDataGenerator
from lsst.sims.catUtils.exampleCatalogDefinitions import PhoSimCatalogPoint
from lsst.sims.catUtils.baseCatalogModels import StarObj

if __name__ == "__main__":

    opsimdb = os.path.join('/Users', 'danielsf', 'physics')
    opsimdb = os.path.join(opsimdb, 'lsst_150412', 'Development')
    opsimdb = os.path.join(opsimdb, 'garage', 'OpSimData')
    opsimdb = os.path.join(opsimdb, 'enigma_1189_sqlite.db')


    generator = ObservationMetaDataGenerator(database = opsimdb, driver='sqlite')

    obs_metadata_list = generator.getObservationMetaData(fieldRA=(np.degrees(6.08), np.degrees(6.11)),
                                                         fieldDec=(np.degrees(-1.11), np.degrees(-1.09)),
                                                         telescopeFilter = 'r',
                                                         expMJD = (49553.0, 49653.0))

    print len(obs_metadata_list)

    db = StarObj()
    with open('amazeball_bands.txt', 'w') as timeseries:
        for ix, obs in enumerate(obs_metadata_list):
            fileName = 'amazeball_frame_%d.txt' % ix
            cat = PhoSimCatalogPoint(db, obs_metadata=obs)
            with open(fileName, 'w') as output:
                cat.write_header(output)
                output.write("object 0 %.4f %.4f 20 ../sky/sed_flat.txt 0 0 0 0 0 0 output_double.fits 0.2 0.0 none\n" 
                             % (obs.unrefractedRA, obs.unrefractedDec))
            timeseries.write('%.4f %s\n' % (obs.mjd, obs.bandpass[0]))


