import bpy

from node_note_property_addon.utils.file_utils import node_name_to_note_text_name

class NODE_OT_remove_note_property(bpy.types.Operator):

    bl_idname = "nodes.remove_note_property"
    bl_label = "Remove node note property"
    bl_description = "Remove note to activated node"

    @classmethod
    def poll(cls, context):
        return context.active_node

    def execute(self, context):
        active_node = context.active_node
        note_name = node_name_to_note_text_name(active_node.name)
        note = bpy.data.texts[note_name]
        bpy.data.texts.remove(note)
        return {"FINISHED"}
