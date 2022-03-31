from ExternalAGIStuff.CodeVisualization.code_editor import find_middle
from ExternalAGIStuff.CodeVisualization.StructureVisualization.translate_AGIObject import translate_AGIList
from ExternalAGIStuff.IDs.reserved_keywords import rr
a = [2, ['fuck'], 3]
b = a[1]
a.pop(0)
print(b)
