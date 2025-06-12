import nuke 

def reload_selected():
    nodes = nuke.selectedNode()
    for node in nodes:
        if node.Class() == "Read":
            node.knob("reload").execute()


def reload_all():
    nodes = nuke.allNodes()
    for node in nodes:
        if node.Class() == "Read":
            node.knob("reload").execute()


nuke.menu("Nuke").findItem("Edit").addCommand("reload_all", 'reload_all()', "alt+r")
