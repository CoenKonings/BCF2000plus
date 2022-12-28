from __future__ import absolute_import, print_function, unicode_literals
from .BCF2000plus import BCF2000plus
import Live 

def create_instance(c_instance):
    u' Creates and returns the BCR2000plus script '
    return BCF2000plus(c_instance)

