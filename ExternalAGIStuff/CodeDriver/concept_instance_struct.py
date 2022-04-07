from copy import deepcopy
from exception import AGIException
from ExternalAGIStuff.CodeDriver.process_stack import process_stack
from ExternalAGIStuff.IDs.concept_ids import cid_reverse
class AGIObject:
    def __init__(self, concept_id: int, attributes=None):
        self.concept_id = concept_id
        if attributes is not None:
            self.attributes = attributes
        else:
            self.attributes = dict()


class AGIList:
    def __init__(self, value: list = None):
        if value is None:
            self.forward = []
            self.reverse = []
            self.value = []
        else:
            self.forward = value
            self.reverse = []
            self.value = self.forward

    def update(self):
        reverse = deepcopy(self.reverse)
        reverse.reverse()
        self.value = self.forward + reverse

    def set_forward(self, index, value):
        if len(self.forward) == index:
            self.forward.append(value)
        elif len(self.forward) < index:
            self.forward += [[None] * (index - len(self.forward))]
            self.forward.append(value)
        else:
            self.forward[index] = value
        self.update()

    def set_reverse(self, index, value):
        if len(self.reverse) == index:
            self.reverse.append(value)
        elif len(self.reverse) < index:
            self.reverse += [None for i in range(index - len(self.reverse))]
            self.reverse.append(value)
        else:
            if self.reverse[index] is not None:
                raise AGIException('Reverse index in AGIList is already occupied.')
            self.reverse[index] = value
        self.update()

    def get_element(self, index) -> any:
        try:
            return self.value[index]
        except IndexError:
            print('index: ' + str(index))
            print('value: ' + str(self.value))
            print('forward: ' + str(self.forward))
            print('reverse: ' + str(self.reverse))
            raise AGIException('index error!', special_name='code_id', special_str=cid_reverse[process_stack[-1].code_id])

    def get_element_reverse(self, index) -> any:
        if len(self.value) - index - 1 < 0:
            print(self.forward)
            print(self.reverse)
            print(self.value)
            raise AGIException('index < 0')
        return self.value[len(self.value) - index - 1]

    def size(self) -> int:
        return len(self.value)

    def get_list(self) -> list:
        return self.value

    def append(self, element):
        self.forward.append(element)
        self.update()

    def remove(self, index):
        try:
            self.forward.pop(index)
        except IndexError:
            print('forward: ' + str(self.forward))
            print('reverse: ' + str(self.reverse))
            print('value: ' + str(self.value))
            raise AGIException('Index Error!')
        self.update()


def get_agi_list(agi_object: AGIObject) -> AGIList:
    if len(agi_object.attributes) != 1:
        attributes = []
        for i in agi_object.attributes.keys():
            attributes.append(cid_reverse[i])
        print(attributes)
        raise AGIException('Trying to get list from AGIObject but AGIObject has more than one attribute',
                           special_name='Concept id', special_str=cid_reverse[agi_object.concept_id])
    for i in agi_object.attributes.keys():
        if agi_object.attributes[i] is None:
            agi_object.attributes[i] = AGIList()
        elif type(agi_object.attributes[i]) != AGIList:
            raise AGIException('Target type is not AGIList', special_name='type', special_str=str(type(i)))
        return agi_object.attributes[i]