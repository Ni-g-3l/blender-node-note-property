import bpy

from node_note_property_addon.utils.file_utils import node_name_to_note_text_name

class NODE_OT_add_or_update_note_property(bpy.types.Operator):

    bl_idname = "nodes.add_or_update_note_property"
    bl_label = "Add or update node note property"
    bl_description = "Add or update note to activated node"

    @classmethod
    def poll(cls, context):
        return context.active_node

    def execute(self, context):
        active_node = context.active_node
        note_name = node_name_to_note_text_name(active_node.name)
        if note_name not in bpy.data.texts:
            bpy.data.texts.new(note_name)

        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = 'TEXT_EDITOR'
        
        text_block = bpy.data.texts[note_name]
        area.spaces.active.text = text_block
        return {"FINISHED"}
