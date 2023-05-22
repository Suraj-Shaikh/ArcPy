# importning ARCPY and Enviroment
import arcpy
from arcpy import env

# Set workspace 
db = env.workspace = r'F:\Suraj_PC\Other_work\NBSS\NBSS Data\Data\AWC'
# List this Raster data
db = arcpy.ListRasters()
# See Ratser files
print(db)

# Execute the raster to polygon conversion
for AWC in db:
    # Creat Unique Name of output files
    AWC_Layer = AWC.split(".")[0] + "_Polygoan"
    arcpy.RasterToPolygon_conversion(AWC, AWC_Layer,"NO_SIMPLIFY","AWC_class")
    



