from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
increment_f = [
[r['assert'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['natural_number']]
]
]], 
[r['assert'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(1)],
[r['concept_instance'], cid_of['natural_number']]
]
]], 
[r['assign'], [r['reg'], obj(0), []], [r['input'], obj(0)]], 
[r['remove'], [r['input'], obj(0)], [r['concept_instance'], cid_of['True']]], 
[r['assign'], [r['reg'], obj(1), []], [r['call'], cid_of['func::sum'],
[
[r['reg'], obj(0), []],
[r['input'], obj(1)]
]
]], 
[r['for'], obj(0), [r['size'], [r['reg'], obj(1), []]],
[
[r['assign'], [r['at'], [r['input'], obj(0)], [r['iterator'], obj(0)]], [r['at'], [r['reg'], obj(1), []], [r['iterator'], obj(0)]]]
]
]
]