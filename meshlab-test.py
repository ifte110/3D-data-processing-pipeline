import pymeshlab as pm

ms = pm.MeshSet()

ms.load_new_mesh('output_sor.ply')

ms.apply_filter('compute_normal_for_point_clouds')

ms.apply_filter('generate_surface_reconstruction_ball_pivoting')

ms.save_current_mesh('output_mesh.obj')