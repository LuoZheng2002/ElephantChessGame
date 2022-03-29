import traceback


class AGIException(BaseException):
    def __init__(self, error_name,
                 current_process=None,  # proc_id
                 current_method=None,
                 current_expression=None,  # expression head, params
                 raw_expression=None,
                 current_line=None,
                 special_name=None,
                 special_str=None):
        self.error_name = error_name
        self.current_process = current_process
        self.current_method = current_method
        self.current_expression = current_expression
        self.raw_expression = raw_expression
        self.current_line = current_line
        self.special_name = special_name
        self.special_str = special_str

    def show(self):
        print('\n################################')
        print('AGI Exception Triggered!')
        print('[Description]: ' + self.error_name)
        if self.current_process is not None:
            print('[Process]:     ' + str(self.current_process))
        if self.current_process is not None:
            print('[Method]:      ' + str(self.current_method))
        if self.current_line is not None:
            print('[Current Line]:  ' + str(self.current_line))
        if self.current_expression is not None:
            print('[Expression]:  ' + str(self.current_expression))
        if self.raw_expression is not None:
            print('[Raw Expr]:    ' + str(self.raw_expression))
        if self.special_name is not None:
            print('[' + self.special_name + ']: ' + self.special_str)
        print('################################\n')
        traceback.print_exc()
