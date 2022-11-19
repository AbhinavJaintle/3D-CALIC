# 3-D Context Based Adaptive Lossless Image Codec
### Implementation of [Band reordering heuristics for lossless satellite image compression with 3D-CALIC and CCSDS](https://www.sciencedirect.com/science/article/pii/S1047320319300501) Research Paper
[![Generic badge](https://img.shields.io/badge/Research-Implementation-<COLOR>.svg)](https://shields.io/)

An end-to-end implementation of a research paper which proposes a novel algorithm for sattelite image processing. 

## Methodology in Research:
### *Abstract*
> Remote sensing satellite images are used widely in space imaging applications as they collect significant
information of ground objects through capturing the ground surface in immense wavelength bands. The
size of these images is typically enormous in quantity due to the bulky number of capturing wavelengths.
The images need to transmit to the ground from the sensors for a specific application. Thus, the efficient
compression techniques are required to fit the available bandwidth for reducing the transmission time.
The data in the images are usually redundant spatially, spectrally and temporally which give an ample
opportunity to compress the images in various domains. Most importantly, the data features have a
strong correlation in the separate spectral area. As a result, the similarity-based band reordering strategy
is used to increase the compression performance in comparison to the image having natural band order.
However, finding the optimal band reordering is still a computationally challenging problem. In this
paper, three different methods namely Band Reordering based on Consecutive Continuity Breakdown
Heuristics (BRCCBH), Band Reordering based on Weighted-Correlation Heuristic (BRWCH) and
Segmented BRCCBH have been proposed for the compression of multispectral, hyperspectral and hyper-
spectral sounder data. The presented methods are different on the number and type of heuristics used for
obtaining the optimal band reordering. The performances of the proposed band reordering methods are
tested using CCSDS 123 lossless predictor and lossless 3D-CALIC. The experimental results show the sig-
nificant improvement on compression performance by using the proposed band ordering techniques for
different types of real multispectral data (3–5% using CCSDS and 2–3% using 3D-CALIC), hyperspectral
data (0.2–0.7% using CCSDS and 0.8–1% using 3D-CALIC) and hyperspectral sounder data (5.5–7% usin
### *Proposed Algorithm*
- **Band Ordering:**
-- Band reordering based on consecutive continuity breakdown heuristics (BRCCBH)
-- Band reordering based on weighted-correlation heuristics (BRWCH)
--  Band reordering based on the segmentation of bands (BRSB)

- **3D-CALIC**


## File Directory

```
3D-CALIC
│   README.md
│
└───Band Reordering
|   │
│   └───Input
│       │   image1.tiff
│       │   image2.tiff
|       │
│   └───Output
│       │   image1ReorderedWithOpenCV.jpg
│       │   image2ReorderedWithOpenCV.jpg
│       │   
│   │   raster_band_reordering.ipynb
│   │   raster_band_reordering.py
|   |   dependencies.md
│   │
└───CALIC
|   │
│   └───Input
│       │   image1.tiff
│       │   image2.tiff
|       │
│   └───Output
│       │   image1.calic
│       │   image1.craw
│       │   image1.raw
│       │   image1.tiff
│       │   image2.calic
│       │   image2.craw
│       │   image2.raw
│       │   image2.tiff
│       │   
│   │   CALIC.ipynb
│   │   calic.py
│   │   adaptivearithmeticcompress.py
|   |   dependencies.md

```

Note: Any changes in the file structure must reflect in the respective code to run it error-free.

## Code

The following two files are the main executable scripts. To run either one of them, we suggest you first see the dependencies associated with them in their markdown files in their respective folders or better, execute in Google Colab (although the files must be uploaded in the same structure either in a S3 container or every time you reconnect the kernel).

- __Band Reordering__
  ___Input:___
      - A regular .tiff image could do but if you want to see the band reording done in an efficient way, you must read [this](https://mikitabelikau.wordpress.com/2017/07/05/getting-sentinel-images-and-browsing-it/)  on how to convert jp2 to GeoTIFF for making a corpus for better results.
  ___Output:___
      - Output is a GTiff file.
      
- __CALIC__
  ___Input:___
      - Any skimage file or a regular image would suffice.
  ___Output:___
      - For a single image, four files will be created: ```img.calic```, ```img.craw```, ```img.raw```, and ```img.tiff```.
     
For more detailed description of the codes see their respective files in this repository.

## Installation

Clone this repository in your system through GitHub Desktop or run the following command:

```
git clone https://github.com/AbhinavJaintle/3D-CALIC.git
```

## Authorization


|  **Project owner** |
| -------------------- |
| Name: ABHINAV JAIN  |
| Date: 2022-11-19     |

* * *

## References

Contributions from the following resources were taken for the project.

1.  https://sss348.wordpress.com/
2.  https://www.nayuki.io/page/reference-arithmetic-coding
3.  https://www.sciencedirect.com/science/article/pii/B0122266803003094
4.  https://mikitabelikau.wordpress.com/2017/08/22/correct-way-of-programmatic-raster-bands-reordering-while-satellite-images-processing/
5.  https://trac.osgeo.org/osgeo4w/wiki
6.  https://gisrsstudy.com/gis-tutorial/erdas-imagine/
7.  https://www.amazon.com/Learning-Geospatial-Analysis-Python-Lawhead/dp/1783281138
8.  https://visibleearth.nasa.gov/




