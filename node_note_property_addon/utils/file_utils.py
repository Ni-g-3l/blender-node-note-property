def node_name_to_note_text_name(node_name):
    cleaned_name = node_name.replace(" ", "_")
    cleaned_name = cleaned_name.replace(".", "_")
    return f"{cleaned_name}_note"