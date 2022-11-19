import cv2
from osgeo import gdal

destinationFile = 'reorderdWithOpenCV.jpg'
inpuDataset = gdal.Open('T18TWL_20170423T155131_TCI..gtiff')
format = 'JPEG'

driver = gdal.GetDriverByName(format)

outputDataset = driver.CreateCopy(destinationFile, inpuDataset, 0)

inpuDataset = None
outputDataset = None

image = cv2.imread(destinationFile, cv2.IMREAD_LOAD_GDAL)
print(image.shape)
reordered = image[..., [1, 0, 2]]

cv2.imwrite(destinationFile, reordered)