

import numpy as np
import matplotlib.pyplot as plt
import os
figdir = os.path.join(os.environ["PYPROBML"], "figures")
def save_fig(fname): plt.savefig(os.path.join(figdir, fname))

from scipy.spatial import KDTree, Voronoi, voronoi_plot_2d

np.random.seed(42)
data = np.random.rand(25, 2)
tree = KDTree(data)
vor = Voronoi(data)
x = np.linspace(0, 1, 200)
y = np.linspace(0, 1, 200)
xx, yy = np.meshgrid(x, y)
xy = np.c_[xx.ravel(), yy.ravel()]

print('Using scipy.spatial.voronoi_plot_2d, wait...')
voronoi_plot_2d(vor)
save_fig('knnVoronoiMesh.pdf')
plt.show()

print('Using scipy.spatial.KDTree, wait a few seconds...')
plt.figure()
plt.plot(data[:, 0], data[:, 1], 'ko')
plt.pcolormesh(x, y, tree.query(xy)[1].reshape(200, 200), cmap='jet')
save_fig('knnVoronoiColor.pdf')
plt.show()
