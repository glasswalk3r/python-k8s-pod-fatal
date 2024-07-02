# Exceptions for modules executed inside a Kubernetes Pod

import os


class Fatal(RuntimeError):
    """Configures a instance of Fatal exception class.

    :param message: The exception message
    :type message: str
    :param output_file: The full path to the file that will be used to write
                        the message to. It defaults to /dev/termination-log.
    :type output_file: str

    Fatal inherits from RuntimeError.
    """
    def __init__(self, message, output_file='/dev/termination-log'):
        msg = f'A fatal error occurred: {message}'
        super().__init__(msg)
        self.log_file = output_file

        if os.path.isfile(output_file):
            with open(output_file, 'w') as fp:
                fp.write(msg)
