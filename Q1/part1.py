import sys
import open3d as o3d

if len(sys.argv) <= 2:
    print("Usage: The first argument is the path to the directory which has ply files")
    print("Usage: The second argument is the name of the object")
    exit(-1)

src = sys.argv[1] + "/source.ply"
tgt = sys.argv[1] + "/target.ply"

out_src = "./part1_out/" + sys.argv[2] + "_source.png"
out_tgt = "./part1_out/" + sys.argv[2] + "_target.png"

src_cloud = o3d.io.read_point_cloud(src)
tgt_cloud = o3d.io.read_point_cloud(tgt)

vis = o3d. visualization.Visualizer()
vis.create_window()
vis.add_geometry(src_cloud)
vis.poll_events()
vis.update_renderer()
vis.capture_screen_image(out_src)
vis.remove_geometry(src_cloud)
vis.add_geometry(tgt_cloud)
vis.poll_events()
vis.update_renderer()
vis.capture_screen_image(out_tgt)
vis.destroy_window()
