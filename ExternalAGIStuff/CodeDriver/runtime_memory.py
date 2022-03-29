from exception import AGIException
from copy import deepcopy


class Register:
    def __init__(self, reg_id, scope_info: tuple):
        self.id = reg_id
        self.scope_info = deepcopy(scope_info)  # scope_info: (iter_id1, iter_id2)
        self.value = dict()

    def create_child(self, child_index: tuple):
        if child_index in self.value:
            raise AGIException('Try to create a register child twice.')
        self.value.update({child_index: None})

    def set_value(self, child_index: tuple, value):
        if child_index not in self.value:
            raise AGIException('Register child is not created.')
        self.value[child_index] = value

    '''
    def get_value(self, child_index: None or list) -> AGIObject or int:
        if child_index is None or child_index == []:
            return self.value
        else:
            for child_value in self.value:
                if child_value[0] == child_index:
                    return child_value[1]
            raise AGIException(3)
    '''


class Iterator:
    def __init__(self, iter_id):
        self.id = iter_id
        self.value = 0


class ResourceManager:
    def __init__(self, input_params):
        self.input_params = input_params
        self.registers = []
        self.iterators = []

    def has_reg(self, reg_id, child_index: tuple):
        for register in self.registers:
            if register.id == reg_id \
                    and child_index in register.value:
                return True
        return False

    def create_reg(self, reg_id, scope_info: tuple, child_index: tuple):  # the reg_id should be local id
        for register in self.registers:
            if register.id == reg_id:  # if this is true, means that register has children
                if register.scope_info != scope_info:
                    raise AGIException('Different scope info.')
                if child_index in register.value:
                    raise AGIException('Child register already created.')
                register.create_child(child_index)
                return
        # if none of the registers match in the parent level:
        self.registers.append(Register(reg_id, scope_info))
        for register in self.registers:
            if register.id == reg_id:
                register.create_child(child_index)
                return
        raise AGIException('Can\'t find target register')

    def create_iterator(self, iter_id):
        for iterator in self.iterators:
            if iterator.id == iter_id:
                raise AGIException('Try to create an iterator twice.')
        self.iterators.append(Iterator(iter_id))

    def update_iterator(self, iter_id):
        for iterator in self.iterators:
            if iterator.id == iter_id:
                iterator.value += 1
                return
        raise AGIException('Can\'t find target iterator.')

    def destroy_iterator(self, iter_id):
        for i, iterator in enumerate(self.iterators):
            if iterator.id == iter_id:
                self.iterators.pop(i)
                return
        raise AGIException('Can\'t find target iterator.')

    def get_iterator_value(self, iter_id):
        for iterator in self.iterators:
            if iterator.id == iter_id:
                return iterator.value
        raise AGIException('Can\'t find target iterator.')

    def set_reg_value(self, reg_id, child_index: tuple, value):
        for register in self.registers:
            if register.id == reg_id:
                register.set_value(child_index, value)
                return
        raise AGIException('Can\'t find target register.')

    def get_reg_value(self, reg_id, child_index: tuple):
        for register in self.registers:
            if register.id == reg_id:
                if child_index not in register.value:
                    print(self.registers[0].value)
                    print('child_index: ' + str(child_index))
                    raise AGIException('Register child not found.', special_name='reg3', special_str=str(self.registers[2].value))
                if register.value[child_index] is None:
                    raise AGIException('Register child has value None.')
                return register.value[child_index]
        raise AGIException('Can\'t find target register.')

    def get_reg(self, reg_id) -> Register:
        for register in self.registers:
            if register.id == reg_id:
                return register
        raise AGIException('Can\'t find target register.')
