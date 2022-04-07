from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
test = [
[r['assign'], [r['reg'], obj(0), []], [obj(523)]], 
[r['assign'], [r['reg'], obj(1), []], [r['find'], [r['reg'], obj(0), []], [r['call'], cid_of['func::compare_concepts'],
[
[r['target']],
[r['concept_instance'], cid_of['5']]
]
]]], 
[r['return'], [r['reg'], obj(1), []]]
]