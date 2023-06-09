import arcpy

from arcpy import env

from arcpy.sa import *

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListLayers(mxd)

# add field and set type
for rs in df:
    arcpy.AddField_management(rs,"SD_Class","TEXT")

# Calculate Field        
for rs in df:
    arcpy.management.CalculateField(rs, "SD_Class", "!Class!", "PYTHON")
    
# Raster to Polygaon conversion 
for SD in df:
    SD_Layers = SD.split(".")[0] + "_" + "poly"
    arcpy.RasterToPolygon_conversion(SD, SD_Layers,"NO_SIMPLIFY","Texture")
    

