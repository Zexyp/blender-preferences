import bpy

markerfile = '/tmp/markertransfer.txt'

with open(markerfile, 'w') as mf:
    for m in bpy.context.scene.timeline_markers:
        mf.write('{},{}\n'.format(m.frame, m.name))
