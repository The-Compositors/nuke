def camera_shake_to_transform():
    #global frame
    first_frame = nuke.root().knob('first_frame').value()
    last_frame = nuke.root().knob('last_frame').value()

    #select camera shake node
    nodes = nuke.selectedNodes()
    if len(nodes) > 1 or len(nodes) == 0:
        nuke.message("Select One CameraShake node")
        return
    node = nodes[0]
    if not node.Class() == "CameraShake3":
        nuke.message("Select One CameraShake node")
        return

    #make group
    group_node = node.makeGroup()

    #into the group and find src transform 
    group_node.begin()
    src_transform_node = nuke.toNode('Transform1')
    group_node.end()

    #make new transform
    new_transform_node = nuke.nodes.Transform()
    new_transform_node.knob('translate').setAnimated()
    new_transform_node.knob('rotate').setAnimated()
    new_transform_node.knob('scale').setAnimated()

    #copy values
    for frame in range(int(first_frame), int(last_frame) + 1):
        # copy transform value
        src_translate = src_transform_node.knob('translate').valueAt(frame)
        src_translate_x = src_translate[0]
        src_translate_y = src_translate[1]
        new_transform_node.knob('translate').setValue(src_translate_x, 0, frame)
        new_transform_node.knob('translate').setValue(src_translate_y, 1, frame)

        # copy rotate value
        src_rotate = src_transform_node.knob('rotate').valueAt(frame)
        new_transform_node.knob('rotate').setValueAt(src_rotate, frame)

        # copy scale value
        src_scale = src_transform_node.knob('scale').valueAt(frame)
        new_transform_node['scale'].setValueAt(src_scale, frame)

    #center_expression
    center_expression = node.knob("cs_center").toScript()
    new_transform_node.knob("center").fromScript(center_expression)

    #place new transfrom node below camera shake
    new_transform_node.setXYpos(node.xpos(), node.ypos()+100)

    #remove group 
    nuke.delete(group_node)
