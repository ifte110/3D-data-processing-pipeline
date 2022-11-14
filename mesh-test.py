from datetime import datetime

start_time = datetime.now()

import pymeshlab as pm

ms = pm.MeshSet()

ms.load_new_mesh('output_sor.ply')

ms.apply_filter('compute_normal_for_point_clouds')

#ms.apply_filter('generate_surface_reconstruction_ball_pivoting')

ms.generate_surface_reconstruction_ball_pivoting(ballradius=pm.Percentage(1), clustering=10)

#ms.apply_filter('meshing_merge_close_vertices')

ms.save_current_mesh('output_mesh.obj')

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))