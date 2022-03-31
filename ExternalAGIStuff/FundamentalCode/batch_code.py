from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException

batch_logic_and_visual = '''
if input0 == 'Fail':
    return 'Fail'
for i in range(input0.size):
    if input0[i] == False:
        return False
for j in range(input0.size):
    if input0[j] == Fail:
        return Fail
return True
'''
batch_logic_and = [
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
         [r['if'], [r['call'], cid_of['func::logic_or'],
                    [
                        [r['call'], cid_of['func::compare_concepts'],
                         [
                             [r['at'], [r['input'], obj(0)], [r['iterator'], obj(0)]],
                             [r['concept_instance'], cid_of['False']]
                         ]
                         ],
                        [r['call'], cid_of['func::compare_concepts'],
                         [
                             [r['at'], [r['input'], obj(0)], [r['iterator'], obj(0)]],
                             [r['concept_instance'], cid_of['Fail']]
                         ]
                         ]
                    ]
                    ],
          [
              [r['return'], [r['concept_instance'], cid_of['False']]]
          ],
          [],
          []
          ]
     ]
     ],
    [r['return'], [r['concept_instance'], cid_of['True']]]
]

batch_logic_or = [
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
    [r['return'], [r['concept_instance'], cid_of['False']]]
]
