import bpy
import textwrap

from node_note_property_addon.utils.file_utils import node_name_to_note_text_name

from node_note_property_addon.blender.operator import (
    NODE_OT_add_or_update_note_property, NODE_OT_remove_note_property
)


class NODE_PT_NotePanel(bpy.types.Panel):

    CHAR_PIXEL_SIZE = 7

    bl_label = "Note"
    bl_idname = "NODE_PT_NotePanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = "NODE_PT_active_node_generic" # This makes the panel foldable under the Node Properties panel
    bl_options = {'DEFAULT_CLOSED'} # This makes the panel foldable

    def draw(self, context):
        layout = self.layout
        active_node = context.active_node
        note_name = node_name_to_note_text_name(active_node.name)
        if note_name in bpy.data.texts:
            self.multiline_label(
                context=context,
                lines=bpy.data.texts[note_name].lines,
                parent=layout
            )
        create_or_update_text, create_or_update_icon = "Add Note", "ADD"
        if note_name in bpy.data.texts:
            create_or_update_text, create_or_update_icon = "Edit note", "GREASEPENCIL"

        row = layout.row()
        row.operator(NODE_OT_add_or_update_note_property.bl_idname, text=create_or_update_text, icon=create_or_update_icon) # description="Edit note of activated node"
        
        if note_name in bpy.data.texts:
            row.operator(NODE_OT_remove_note_property.bl_idname, text="Remove note", icon="REMOVE") # description="Remove note of activated node", 

    def multiline_label(self, context, lines, parent):
        chars = int(context.region.width / self.CHAR_PIXEL_SIZE)   # 7 pix on 1 character
        wrapper = textwrap.TextWrapper(width=chars)
        for line in lines:
            text_lines = wrapper.wrap(text=line.body)
            for text_line in text_lines:
                parent.label(text=text_line)