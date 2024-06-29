import os


class Fatal(RuntimeError):
    def __init__(self, message, output_file='/dev/termination-log'):
        msg = f'A fatal error occurred: {message}'
        super().__init__(msg)
        self.log_file = output_file

        if os.path.isfile(output_file):
            with open(output_file, 'w') as fp:
                fp.write(msg)
