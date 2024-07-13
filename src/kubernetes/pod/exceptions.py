# Exceptions for modules executed inside a Kubernetes Pod

import os


class Fatal(RuntimeError):
    """Exception that identifies the root cause of failure for a Kubernetes
    Pod.

    Usage of this class guarantees that not only the exception message goes to
    the Docker container log, but also to the respective termination log,
    making it easier to identify the reason for the Pod failure.
    """

    def __init__(self, message: str, output_file: str ='/dev/termination-log') -> None:
        """Configure a instance of Fatal exception class.

        If ``output_file`` is different from the default, make sure to also
        properly configure the Kubernetes Pod in order to use this
        alternative file path.
        """

        msg = f'A fatal error occurred: {message}'
        super().__init__(msg)
        self.log_file = output_file

        if os.path.isfile(output_file):
            with open(output_file, 'w') as fp:
                fp.write(msg)
