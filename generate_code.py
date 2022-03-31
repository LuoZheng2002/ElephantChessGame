from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException
fixes = [
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['input'], obj(0)],
[r['concept_instance'], cid_of['Fail']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['Fail']]]
],
[],
[]
], 
[r['for'], obj(0), [r['size'], [r['input'], obj(0)]],
[
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['at'], [r['input'], obj(0)], [r['iterator'], obj(0)]],
[r['concept_instance'], cid_of['True']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['True']]]
],
[],
[]
]
]
], 
[r['for'], obj(1), [r['size'], [r['input'], obj(0)]],
[
[r['if'], [r['call'], cid_of['func::compare_concepts'],
[
[r['at'], [r['input'], obj(0)], [r['iterator'], obj(1)]],
[r['concept_instance'], cid_of['Fail']]
]
],
[
[r['return'], [r['concept_instance'], cid_of['Fail']]]
],
[],
[]
]
]
], 
[r['return'], [r['concept_instance'], cid_of['False']]]
]