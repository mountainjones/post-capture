from osgeo import gdal
gdal.AllRegister()
rast_src = gdal.Open('filename.tif', 1 )
gt = rast_src.GetGeoTransform()
gtl = list(gt)
gtl[0] -= 200	#EAST
gtl[3] -= 100	#NORTH
rast_src.SetGeoTransform(tuple(gtl))
rast_src = None