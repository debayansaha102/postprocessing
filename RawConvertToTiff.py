# This script allows importing an image sequence of raw files 
# from a folder. The user just needs to know/enter image width,
# height and depth.
#
# Author: Robert Haase, http://github.com/haesleinhuepf
# October 2017
#


from ij import IJ;
from ij import ImageJ;
from ij import ImagePlus;
from ij.plugin import RGBStackMerge;

from java.io import File;
from java.util import ArrayList;

import os




folder = '/Volumes/myers_scope_cache/Deb/2018-05-09-18-27-19-69-Titanic_MirrorModes_Beads_Deb/stacks/C0L0';

imageWidth=256;
imageHeight=256;
imageDepth=62;
pixelWidth=0.26;
pixelHeight=0.26;
pixelDepth=1.0;

outfolder = '/Volumes/myers_scope_cache/Deb/2018-05-09-18-27-19-69-Titanic_MirrorModes_Beads_Deb/stacks/C0L0/TiffFiles';


print(folder)

images = [];

# load all images, collect them in a list
for root, directories, filenames in os.walk(folder):
    filenames.sort();
    for filename in filenames:
	    print(filename)
	    if (filename.endswith(".raw")):
		    if (not File(os.path.join(folder, filename + ".tif")).exists()):
			    IJ.run("Raw...", "open=[" + os.path.join(folder, filename) + "] image=[16-bit Signed] width=" + str(imageWidth) + " height=" + str(imageHeight) + " number=" + str(imageDepth) + " little-endian");
			    imp = IJ.getImage();
			    imp.getCalibration().pixelWidth = pixelWidth
			    imp.getCalibration().pixelHeight = pixelHeight
			    imp.getCalibration().pixelDepth = pixelDepth
			    IJ.saveAsTiff(imp, os.path.join(outfolder, filename + ".tif") )
			    imp.close()