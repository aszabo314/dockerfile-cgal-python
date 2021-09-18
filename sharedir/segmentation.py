from __future__ import print_function
import sys
sys.path.insert(1, '/root/cgal-swig-bindings/build/build-python')
import datetime
import time

from CGAL.CGAL_Kernel import Point_3
from CGAL.CGAL_Kernel import Vector_3
from CGAL.CGAL_Point_set_3 import Point_set_3
from CGAL.CGAL_Shape_detection import *

import os
filename = "Jb_small.pts"

datadir = "/things"
datafile = datadir+'/'+filename

# https://github.com/CGAL/cgal-swig-bindings/blob/ba57f96a1d06e669ed866919be90ef180830370f/SWIG_CGAL/Shape_detection/impl.h

bt = datetime.datetime.now()
points = Point_set_3(datafile)
print(points.size(), "points read")
plane_map = points.add_int_map("plane_index")
et = datetime.datetime.now()
print(et-bt, "import time")

bt = datetime.datetime.now()
print("region growing")
nb_planes = region_growing(points, plane_map, min_points=2000, epsilon=0.15, cluster_epsilon=1.0, normal_treshold=0.0, k=0)
print(nb_planes, "planes detected")
et = datetime.datetime.now()
print(et-bt, "region growing time")

# print("ransac")
# bt = datetime.datetime.now()
# planes = efficient_RANSAC(points, plane_map,
#                           min_points=1000,
#                           epsilon=0.15,
#                           cluster_epsilon=0.5,
#                           normal_threshold=0.0,
#                           planes=True, cylinders=False,
#                           spheres=False, cones=False, tori=False)
# print(len(planes), "ransac planes")
# et = datetime.datetime.now()
# print(et-bt, "ransac time")

print("write out file..")
offf = open('/things/out-'+str(int(time.time()))+'.pts', 'a')
for idx in points.indices():
    p = points.point(idx)
    si = plane_map.get(idx)
    _ = offf.write(""+str(p.x())+" "+str(p.y())+" "+str(p.z())+" "+str(si)+" "+str(idx)+"\r\n")
offf.close()
print("done")