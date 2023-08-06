"""
description: this module provides the function for teststeps, including the decorator and timeout function.
"""
import enum
import functools
import inspect
import itertools
import threading
from typing import Union, List, Tuple, Sequence

from _pistar.utilities.constants import TESTCASE_EXECUTION_STATUS
from _pistar.utilities.exceptions import UsageError
from _pistar.utilities.exceptions import DuplicatedTestStepNameException
from _pistar.utilities.exceptions import UnsupportedStartTypeException
from .thread_status import Status


def has_teststep(cls):
    """
    description: this function is used to
                 check whether a testcase has teststep.
    arguments:
        Class:
            type: type
    return:
        type: bool
    """

    for member in cls.__dict__.values():
        if hasattr(member, "start") and hasattr(member, "end"):
            return True
    return False


def is_teststep(function):
    """
    description: this function is used to check whether a function is teststep.
    arguments:
        function:
            type: any
            assertion: callable
    return:
        type: bool
        description: if the function is a teststep, return True,
                     else return False.
    """
    return (
        hasattr(function, "start") and hasattr(function, "end") and callable(function)
    )


def teststep(test_function=None, *, start=None, skip=None, mark=None, timeout=None):
    """
    description: decorate of teststep, parse actual teststep arguments
                 and run the step
    arguments:
        start:
            description: indicate teststep when to run
            type: str
            default: None
        skip:
            description: set the teststep not to run
            type: bool
        mark:
            description: set mark to teststep, specific mark step
    return:
        type: TestStep
        description: actual step function results
    """
    teststep_obj = TestStep(start=start, skip=skip, mark=mark, timeout=timeout)
    if test_function:
        return teststep_obj(test_function)

    return teststep_obj


class TestStep:
    """
    description: teststep decorate class, generate schedule strategy based on
                 testcase class
    attribute:
        start:
            description: indicate teststep when to run
            type: str
            default: None
        skip:
            description: set the teststep not to run
            type: bool
        mark:
            description: set mark to teststep,  specific mark step
    """

    start = None
    skip = None
    mark = None

    __status_dictionary = {
        key: value
        for key, value in TESTCASE_EXECUTION_STATUS.__dict__.items()
        if not key.startswith("__")
    }
    __teststep_list = None

    def __get_previous_teststep(self):
        caller_frame = inspect.currentframe()
        while True:
            if not caller_frame.f_code.co_filename == __file__:
                break
            caller_frame = caller_frame.f_back

        member_name_list = list(caller_frame.f_locals.keys())
        for member_name in member_name_list[::-1]:
            last_member = caller_frame.f_locals[member_name]

            if is_teststep(last_member):
                self.__teststep_list.append(last_member)

        if self.__teststep_list:
            return self.__teststep_list[0]
        return None

    def __init__(self, start=None, skip=None, mark=None, timeout=None):
        self.skip = skip
        self.mark = mark
        self.timeout = timeout
        self.__teststep_list = list()

        previous_teststep = self.__get_previous_teststep()
        if start is None:
            if previous_teststep:
                self.start = previous_teststep.end
            else:
                self.start = Status(True)
        elif not isinstance(start, Status):
            raise UnsupportedStartTypeException(start)
        else:
            self.start = start

    def __execute(self, function, testcase, **kwargs):
        function(testcase, **kwargs)

    def __call__(self, function, **kwargs):
        if function.__name__ in [item.__name__ for item in self.__teststep_list]:
            raise DuplicatedTestStepNameException(function.__name__)
        function = Timeout(self.timeout)(function)

        @functools.wraps(function, **kwargs)
        def wrapper(*args, **kwargs):
            testcase = args[0]
            function.__globals__.update(**self.__status_dictionary)
            if self.skip:
                pass
            elif not self.mark:
                self.__execute(function, testcase, **kwargs)
            elif not wrapper.marks:
                self.__execute(function, testcase, **kwargs)
            elif self.mark not in wrapper.marks:
                pass
            else:
                self.__execute(function, testcase, **kwargs)
            wrapper.end.value = True

        wrapper.start = self.start
        wrapper.end = Status(False)
        wrapper.marks = list()
        return wrapper


class Algorithm(enum.Enum):
    NONE = -1
    Full_Combination = 1

    @classmethod
    def __missing__(cls, key) -> "Algorithm":
        return Algorithm.NONE


def parameters(arg_names: Union[str, Sequence[str]],
               arg_values: Union[List, Tuple],
               *,
               indirect=False, 
               algorithm=Algorithm.NONE):
    """
    description: decorate of parameters, parse actual teststep arguments
                 and run the step
    arguments:
        arg_names:
            description: teststep parameter names
            type: str, list, tuple
        arg_values:
            description: teststep parameter values
            type: list, tuple
        indirect:
            description: whether to use condition, true if so
            type: bool
            default: false
        algorithm:
            description: built-in algorithm, users can expand more parameters
            type: Algorithm
            default: none
    return:
        type: Parameters
    """
    parameters_obj = Parameters(
        arg_names=arg_names,
        arg_values=arg_values,
        indirect=indirect,
        algorithm=algorithm,
    )
    return parameters_obj


class Parameters:
    """
    description: parameters decorate class, generate schedule strategy based on
                 testcase class
    attribute:
        arg_names:
            description: teststep parameter names
            type: str, list, tuple
        arg_values:
            description: teststep parameter values
            type: list, tuple
        indirect:
            description: whether to use condition, true if so
            type: bool
            default: false
        algorithm:
            description: built-in algorithm, users can expand more parameters
            type: Algorithm
            default: none
    """

    arg_names = None
    arg_values = None
    indirect = False
    algorithm = Algorithm.NONE
    parameters = list()

    def __init__(
        self, arg_names, arg_values, *, indirect=False, algorithm=Algorithm.NONE
    ):
        self.arg_names = arg_names
        self.arg_values = arg_values
        self.indirect = indirect
        self.algorithm = algorithm

        if not isinstance(self.arg_names, (str, list, tuple)):
            msg = (
                f"the type of parameter arg_names '{self.arg_names}' is '{self.arg_names.__class__.__name__}', "
                f"but the 'str', 'list' or 'tuple' is expected"
            )
            raise UsageError(msg)
        if not isinstance(self.arg_values, (list, tuple)):
            msg = (
                f"the type of parameter arg_values '{self.arg_values}' is '{self.arg_values.__class__.__name__}', "
                f"but the 'list' or 'tuple' is expected"
            )
            raise UsageError(msg)

        if self.indirect:
            self.parameters = [{}]
        else:
            self.arg_values = self.__transform_values()
            if isinstance(self.arg_names, str):
                self.parameters = [{self.arg_names: value} for value in self.arg_values]
            else:
                self.parameters = [
                    dict(zip(self.arg_names, value)) for value in self.arg_values
                ]

    def __transform_values(self):
        if self.algorithm == Algorithm.Full_Combination:
            return itertools.product(*self.arg_values)
        elif self.algorithm == Algorithm.NONE:
            return self.arg_values
        else:
            return self.arg_values

    def __execute(self, function, testcase, **kwargs):
        for parameter in self.parameters:
            # For report printing specific parameters
            function.cur_param = [
                k + "=" + str(parameter.get(k, "")) for k in parameter
            ]

            function(testcase, **parameter, **kwargs)

    def __call__(self, function, **kwargs):
        @functools.wraps(function, **kwargs)
        def wrapper(*args, **kwargs):
            testcase = args[0]
            self.__execute(function, testcase, **kwargs)

        wrapper.parameters = self.parameters
        wrapper.indirect = self.indirect
        return wrapper


class TimeoutException(Exception):
    """
    description: if a function is timeout, raise this exception.
    """

    def __init__(self, function_name, timeout):
        super().__init__(
            f"teststep '{function_name}' is terminated due to timeout {timeout} seconds"
        )


class Timeout:
    """
    description: this class is used to wrap a function with timeout limit.
    """

    timeout = None

    def __init__(self, timeout=None):
        self.timeout = timeout

    def __call__(self, function):
        if self.timeout is None:
            return function

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            results = [
                TimeoutException(function_name=function.__name__, timeout=self.timeout)
            ]

            def thread_function():
                try:
                    results[0] = function(*args, **kwargs)
                except BaseException as exception:
                    results[0] = exception

            thread = threading.Thread(target=thread_function)
            thread.daemon = True

            thread.start()
            thread.join(self.timeout)

            if isinstance(results[0], Exception):
                raise results[0]

            return results[0]

        return wrapper
