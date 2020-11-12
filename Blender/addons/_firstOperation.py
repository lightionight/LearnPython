import bpy

scene = bpy.context.scene;
for obj in scene.object:
    obj.location.x += 1.0;