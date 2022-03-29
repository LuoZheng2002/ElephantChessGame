from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.IDs.to_object import obj

digit_to_natural_number_code = [
    [r['assign'], [r['reg'], obj(0), []], [r['concept_instance'], cid_of['natural_number']]],
    [r['assign'], [r['at'], [r['reg'], obj(0), []], [obj(0)]], [r['input'], obj(0)]],
    [r['return'], [r['reg'], obj(0), []]]
]

# 参数：两个自然数
# 伪代码：
# if input0.size == 1 and input1.size == 1:
#     return 'compare_single_digit_natural_numbers'(input0, input1)
# reg0 = input0.size
# reg1 = input1.size
# reg2 = 'compare_natural_numbers'(reg0, reg1)
# if reg2 == 'greater_than':
#     return 'greater_than'
# elif reg2 == 'less_than':
#     return 'less_than'
# for i in range(reg0):
#     reg3<i> = 'compare_single_digit_natural_number'('digit_to_number'(input0[i]), 'digit_to_number'(input1[i]))
#     if reg3<i> == 'greater_than':
#         return 'greater_than'
#     elif reg3<i> == 'less_than':
#         return 'less_than'
# return 'math_equal'
compare_natural_numbers_code = [
    [r['if'],
     [r['call'], cid_of['func::logic_and'],
      [
          [r['call'], cid_of['func::is_natural_number_single_digit'], [[r['input'], obj(0)]]],
          [r['call'], cid_of['func::is_natural_number_single_digit'], [[r['input'], obj(1)]]],
      ]],
     [
         [r['return'], [r['call'], cid_of['func::compare_single_digit_natural_numbers'],
                        [
                            [r['input'], obj(0)],
                            [r['input'], obj(1)]
                        ]]]
     ],
     # elif
     [],
     # else
     []
     ],
    [r['assign'], [r['reg'], obj(0), []], [r['size'], [r['input'], obj(0)]]],
    [r['assign'], [r['reg'], obj(1), []], [r['size'], [r['input'], obj(1)]]],
    [r['assign'], [r['reg'], obj(2), []], [r['call'], cid_of['func::compare_natural_numbers'],
                                           [
                                               [r['reg'], obj(0), []],
                                               [r['reg'], obj(1), []]
                                           ]]],
    [r['if'], [r['call'], cid_of['func::compare_concepts'],
               [
                   [r['reg'], obj(2), []],
                   [r['concept_instance'], cid_of['greater_than']]
               ]],
     [
         [r['return'], [r['concept_instance'], cid_of['greater_than']]]
     ],
     # elif block
     [[
         [r['call'], cid_of['func::compare_concepts'],
          [
              [r['reg'], obj(2), []],
              [r['concept_instance'], cid_of['less_than']]
          ]],
         [
             [r['return'], [r['concept_instance'], cid_of['less_than']]]
         ]
     ]],
     # else block
     []
     ],
    [r['for'], obj(0), [r['reg'], obj(0), []],
     [
         [r['assign'], [r['reg'], obj(3), [[r['iterator'], obj(0)]]],
          [r['call'], cid_of['func::compare_single_digit_natural_numbers'],
           [
               [r['call'], cid_of['func::digit_to_natural_number'],
                [[r['at'], [r['input'], obj(0)], [r['iterator'], obj(0)]]]],
               [r['call'], cid_of['func::digit_to_natural_number'],
                [[r['at'], [r['input'], obj(1)], [r['iterator'], obj(0)]]]],
           ]]],
         [r['if'], [r['call'], cid_of['func::compare_concepts'],
                    [
                        [r['reg'], obj(3), [[r['iterator'], obj(0)]]],
                        [r['concept_instance'], cid_of['greater_than']]
                    ]],
          [
              [r['return'], [r['concept_instance'], cid_of['greater_than']]]
          ],
          [[
              [r['call'], cid_of['func::compare_concepts'],
               [
                   [r['reg'], obj(3), [[r['iterator'], obj(0)]]],
                   [r['concept_instance'], cid_of['less_than']]
               ]],
              [
                  [r['return'], [r['concept_instance'], cid_of['less_than']]]
              ]
          ]],
          []
          ]
     ]
     ],
    [r['return'], [r['concept_instance'], cid_of['math_equal']]]
]


greater_code = [

]