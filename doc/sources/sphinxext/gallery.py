import os
import re
from os.path import join as slash  # just like that name better


base_dir = '/Users/charlesmerriam/p/kivy'
examples_dir = slash(base_dir, 'examples')
screenshots_dir = slash(base_dir, 'doc/sources/images/examples')
source_dir = slash(base_dir, '')
def iter_files(dir):
    pattern = re.compile('^([^_]+)__(.+)__(.+)__([^-]+)(-[^_]*)?\.png')
    for t in os.walk(dir):
        for filename in t[2]:
            if filename.endswith('.png'):
                m = pattern.match(filename)
                if m is None:
                    yield {'error': 'png filename does not match screenshot '
                           'pattern: {}'.format(filename) }
                else:
                    yield { 'image' : slash(t[0], filename),  # full path?
                            'order': m.group(1),
                            'dir' : m.group(2).replace('__', os.path.sep),
                            'file' : m.group(3),
                            'ext' : m.group(4),
                            'index' : m.group(5)  # may be None
                    }



def grab_docstring(text):
    """ return text of the docstring else None """
    q = '\"\"\"|\'\'\''
    p = r'({}).*?(\1)'.format(q)
    m = re.search(p, text, re.S)
    if m:
        return m.group(0)
    else:
        return None


print grab_docstring(''' NO ''')
d = """'''
3D Rendering Monkey Head
========================

This example demonstrates using OpenGL to display rotating monkey head. This
includes loading a Blender OBJ file, shaders written in OpenGL's Shading
Language (GLSL), and using scheduled callbacks.

The file monkey.obj is a OBJ file output form the Blender free 3D creation
software. The file is text, listing vertices and faces. It is loaded
into a scene using objloader.py's ObjFile class. The file simple.glsl is
a simple vertex and fragment shader written in GLSL.
'''
blah blah
blah blah
"""
print grab_docstring(d)



def expand_file_dict(fd):
    filename = slash(examples_dir, fd['dir'], fd['file'] + '.' + fd['ext'])
    if not os.path.exists(filename):
        fd.clear()
        fd['error'] = 'Referenced file does not exist {}'.format(filename)
        return fd
    with open(filename) as f:
        text = f.read()
        docstring = grab_docstring(text)
        p = "'''\n([^\n]+)\n=+\n+(.*)'''"
        pass

for fi in iter_files(screenshots_dir):
    print expand_file_dict(fi)

