def set_project_settings_from_read():
    node = nuke.selectedNode()
    first = node.knob("first").getValue()
    last = node.knob("last").getValue()
    format = node.knob("format").value()
    
    nuke.root().knob("first_frame").setValue(first)
    nuke.root().knob("last_frame").setValue(last)
    nuke.root().knob("format").setValue(format)
    nuke.root().knob("lock_range").setValue(True)

nuke.menu("Nuke").findItem("Edit").addCommand("set_project_settings_from_read", 'set_project_settings_from_read()')
