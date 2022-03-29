from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import obj
from ExternalAGIStuff.IDs.concept_ids import cid_of
test_code1 = [
    [r['assert'], [obj(True)]],
    [r['return'], [obj(0)]]
]

test_code2 = [
    [r['assign'], [r['reg'], obj(0), []], [r['input'], obj(0)]],
    [r['assign_as_reference'], [r['reg'], obj(1), []], [r['reg'], obj(0), []]],
    [r['assign'], [r['at'], [r['reg'], obj(1), []], [obj(1)]], [r['concept_instance'], cid_of['2']]],
    [r['return'], [r['reg'], obj(0), []]]
]
