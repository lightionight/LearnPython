bl_info = {
    "name" : "Cursor Array",
    "blender" : (2, 90, 1),
    "category": "object",
}

import bpy

class ObjectCursorArray(bpy.types.Operator):
    ''' object cursor Array'''
    bl_idname = "object.cursor_array";
    bl_label = "Cursor Array";
    bl_options = {"REGISTER", "UNDO"};

    def execute(self, context):
        scene = context.scene;
        cursor = scene.cursor.location;
        obj = context.active_object;

        copy_number = 10;
        
        for i in range(copy_number):
            obj_new = obj.copy();
            scene.collection.objects.link(obj_new);
            factor = i / copy_number;
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor));
        
        return {"FISISHED"};
def register():
    bpy.utils.register_class(ObjectCursorArray);
def unregister():
    bpy.utils.unregister_class(ObjectCursorArray);
    
if__name__ == "__main__":
    register();