import arcpy 

from arcpy.sa import *
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListLayers(mxd)

# Loop through each layer and add the field    
for rs in df:
    #print(raster)
    arcpy.AddField_management(rs,"AWC_clas","TEXT")
    


