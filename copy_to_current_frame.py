def copy_to_current_frame():

    node = nuke.selectedNode()
    if not node.Class() == "CornerPin2D":
        return
        
    node.knob("from1").setValue(node.knob("to1").value())
    node.knob("from2").setValue(node.knob("to2").value())
    node.knob("from3").setValue(node.knob("to3").value())
    node.knob("from4").setValue(node.knob("to4").value())

    node.knob("label").setValue(f"ref frame : {nuke.frame()}")  
    node.knob("label").setValue("ref frame : {}".format(nuke.frame()))  # before nuke13

copy_to_current_frame()



nuke.menu("Nuke").findItem("Edit").addCommand("cornerpin/copy to current frame", 'copy_to_current_frame()')
