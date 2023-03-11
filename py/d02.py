"""

    Lecture:

        run python file from pycharm
        str()
        doc strings
        comments
        import
        pep8

    Project 1.1
        Continue exploration on hello_world()
        1. add user name
        2. replace user name with friendly name
        3. say good morning and good night appropriately

    homework:
        1. expand on hello_world()
        2. make a PR

"""

import getpass

def hello_world():
    '''
    Prints variations on 'hello world' depending on conditions.
    :return: None
    '''
    use_getpass = True

    if use_getpass:
        user = getpass.getuser()
        print('hello {0}'.format(user))
    else:
        print('hello_world')


hello_world()
