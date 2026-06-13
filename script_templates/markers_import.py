import bpy

markerfile = '/tmp/markertransfer.txt'

with open(markerfile, 'r') as mf:
    for l in mf:
        f,n = l.split(',')
        bpy.context.scene.timeline_markers.new(n.strip(), frame=int(f))
