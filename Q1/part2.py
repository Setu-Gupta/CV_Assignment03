import sys
import numpy as np
import open3d as o3d

if len(sys.argv) <= 2:
    print("Usage: The first argument is the path to the directory which has ply files")
    print("Usage: The second argument is the name of the object")
    exit(-1)

src = sys.argv[1] + "/source.ply"
tgt = sys.argv[1] + "/target.ply"
transform = sys.argv[1] + "/T_gt.txt"

out_tgt = "./part2_out/" + sys.argv[2] + "_target.png"

# Create the point clouds
src_cloud = o3d.io.read_point_cloud(src)
tgt_cloud = o3d.geometry.PointCloud()

# Convert to numpy array in homogeneous coordinates
points = np.asarray(src_cloud.points)
num_points = points.shape[0]
zeros = np.ones((num_points, 1), dtype=points.dtype)
homo_points = np.append(points, zeros, axis=1)

# Read the transformation matrix
mat = []
with open(transform, 'r') as mat_file:
    for line in mat_file.readlines():
        row = [float(r) for r in line.strip().split()]
        mat.append(row)
T = np.array(mat)

# Compute the transformed points
transformed = []
for p in homo_points:
    tmp = T.dot(p)
    w = tmp[-1]
    transformed_p = [i/w for i in tmp[:-1]]
    transformed.append(transformed_p)
tgt_points = np.array(transformed)

# Populate the target point cloud
tgt_cloud.points = o3d.utility.Vector3dVector(tgt_points)
 
# Save the target
vis = o3d. visualization.Visualizer()
vis.create_window()
vis.add_geometry(tgt_cloud)
vis.poll_events()
vis.update_renderer()
vis.capture_screen_image(out_tgt)
vis.destroy_window()
