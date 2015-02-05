'''
Testing kivy_examples Sphinx Extension
======================================

'''
import unittest
from doc.sources.sphinxext.kivy_examples import *

class ExamplesTestCase(UnitTest):
    monkey = d = """'''
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
    def test_grab_docstring(self):
        self.assertIsNone(grab_docstring(''))
        self.assertIsNone(grab_docstring('Foobar'))
        s = ('"\nSingle Quotes\n'
             'A docstring without triple quotes is not a docstring."\n')
        self.assertIsNone(grab_docstring(s))

    def test_grab_docstring_monkey(self):
        d = grab_docstring(self.monkey)
        assertIsNotNone(d)

