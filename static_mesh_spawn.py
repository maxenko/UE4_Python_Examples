import unreal 
from unreal import EditorLevelLibrary as lib

meshPath = "StaticMesh'/Game/Megascans_4K/3D_Asset/24_Rock_Sandstone_rjApI/Aset_rock_sandstone_M_rjApI_LOD0.Aset_rock_sandstone_M_rjApI_LOD0'"

exists = unreal.EditorAssetLibrary.does_asset_exist(meshPath)

if exists:

    #load once
    asset = unreal.EditorAssetLibrary.load_asset(meshPath)
    offset_m = 75
    grid_size_x = 10
    grid_size_y = 10

    for x in range(grid_size_x):
        for y in range(grid_size_y):

            label = "%s_%i_%i" % ("rock", x, y)

            mesh = lib.spawn_actor_from_class(unreal.StaticMeshActor.static_class(), unreal.Vector((x*offset_m)-(grid_size_x*offset_m)/2, (y*offset_m)-(grid_size_y*offset_m)/2, 18.0), unreal.Rotator(0.0, 0.0, 0.0))
            mesh.set_actor_label(label)

            mesh.static_mesh_component.set_static_mesh(asset)

            unreal.log(mesh.get_actor_label())
