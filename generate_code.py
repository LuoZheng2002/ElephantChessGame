from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
fixes = [
[r['assign'], [r['reg'], obj(0), []], [obj(12233344444)]], 
[r['return'], [r['count'], [r['reg'], obj(0), []], [r['call'], cid_of['func::compare_concepts'],
[
[r['target']],
[r['concept_instance'], cid_of['4']]
]
]]]
]