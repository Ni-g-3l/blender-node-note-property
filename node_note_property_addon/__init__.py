bl_info = {
    "name": "blender-node-note-addon",
    "author": "Ni-g-3l",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "Node",
    "description": "Add note property on Blender Node",
    "warning": "",
    "doc_url": "",
    "category": "Node",
}

import bpy

def register():
    from node_note_property_addon.blender.panel import NODE_PT_NotePanel
    bpy.utils.register_class(NODE_PT_NotePanel)

    from node_note_property_addon.blender.operator import (
        NODE_OT_add_or_update_note_property, NODE_OT_remove_note_property
    )

    bpy.utils.register_class(NODE_OT_add_or_update_note_property)
    bpy.utils.register_class(NODE_OT_remove_note_property)

def unregister():
    from node_note_property_addon.blender.panel import NODE_PT_NotePanel
    bpy.utils.unregister_class(NODE_PT_NotePanel)
    
    from node_note_property_addon.blender.operator import (
        NODE_OT_add_or_update_note_property, NODE_OT_remove_note_property
    )

    bpy.utils.unregister_class(NODE_OT_add_or_update_note_property)
    bpy.utils.unregister_class(NODE_OT_remove_note_property)
