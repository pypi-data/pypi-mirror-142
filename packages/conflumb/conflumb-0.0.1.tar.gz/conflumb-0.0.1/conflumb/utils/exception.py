import json
from inspect import currentframe, getframeinfo


class ExceptionError(Exception):
    def __init__(self, payload=None, message=None):

        # Now for your custom code...
        self.payload = payload if not payload or type(payload) is str else json.dumps(payload)
        self.message = message
        self.ProtoError = True

        # involve stack tracking
        previous_frame = currentframe().f_back
        (filename, line_number, function_name, lines, index) = getframeinfo(previous_frame)
        self.payload = f'{self.payload} \n {filename} - {line_number}'

        # Call the base class constructor with the parameters it needs
        super().__init__(str(self))

    def __str__(self):
        return '\n'.join([self.message, self.payload or ''])


class GErrorConfluenceAPIOffline(ExceptionError):
    pass


class GErrroNotFound(ExceptionError):
    pass


class GErrorFileNotFound(ExceptionError):
    pass
