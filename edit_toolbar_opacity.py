def increase_toolbar_opacity():
    node = nuke.selectedNode()
    if node.Class() == 'RotoPaint':
        old_value =node.knob("toolbar_opacity").value()
        new_value = old_value + 0.1
        clamp_value = max(0.0, min(1.0, new_value))
        node.knob("toolbar_opacity").setValue(clamp_value)

def decrease_toolbar_opacity():
    node = nuke.selectedNode()
    if node.Class() == 'RotoPaint':
        old_value =node.knob("toolbar_opacity").value()
        new_value = old_value - 0.1
        clamp_value = max(0.0, min(1.0, new_value))
        node.knob("toolbar_opacity").setValue(clamp_value)

nuke.menu("Nuke").findItem("Edit").addCommand("decrease_toolbar_opacity", 'decrease_toolbar_opacity()', "alt+,")
nuke.menu("Nuke").findItem("Edit").addCommand("increase_toolbar_opacity", 'increase_toolbar_opacity()', "alt+.")
