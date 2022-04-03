from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
fixes = [
[r['assign_as_reference'], [r['reg'], obj(0), []], [r['input'], obj(0)]], 
[r['append'], [r['reg'], obj(0), []], [r['concept_instance'], cid_of['1']]], 
[r['return'], [r['reg'], obj(0), []]]
]