# Python for Tech Artists 101
This repo will have Python examples and helpful stuff for class.

Also this is how you hand in your homework. 
You make a PR and we review it together in class.

Please make sure to make a folder with your name and last name all lower case, like this: "alexis_meade"

# Useful git commands:
git clone https://github.com/isoparms/pyta_pulse_2023_summer
git -C "D:\pulse_college\pyta_pulse_2023_summer" pull

# Week by Week Breakdown:
## Week 1:

    Intro:
        Teacher and students

    Lecture:

        scrpipted language vs compiled language?
        python 3
        why python?
        Standalone Vs Maya/Substance/Houdini
        git and github

    Project 1.1
        Set up Python Dev Environment

        1. Install Python 3
            https://www.python.org/downloads/
            run python, play around.

        2. Make a github account
            https://docs.github.com/en/get-started/quickstart/set-up-git
            Make accounts
            Join https://github.com/isoparms/pyta_pulse_2023_summer

        3. Install Pycharm Community
            https://www.jetbrains.com/pycharm/download/#section=windows
            Connect to git hub
            Make a project
            clone pyta_pulse_2023_summer
            make your first PR

    Project 1.2:
        hello_world()

    Homework:
        1. Expand on hello_world() and make a PR
        2. Ask a question in the QA section

## Week 2:

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


## Week 3:

    Lecture:
        list()
        bool()
        import
        for
        if

    Project 1:
        list_files(extension='.txt')
        - list()
        - bool()
        - import and use os.path and os.file
        - for:
        - if:

        1. make a fucntion that lists all the files in a folder
        2. only files of a given extension
        3. only files of a given list of extensions
        (stretch)
        4. recursively search files
            - os.walk
            - break
            - continue

    Homework:
        1. finish project
        2. make a PR

## Week 4:

    Lecture:
        libraries
        import shared.python.x
        build up libraries
        readabiliy vs efficiency vs optimization

    Project 1:
        Shared library 101
        Add list_files() to library
        shared.python.utils
            new fn are_items_in_list()
            new fn empty_list()
            new fn remove_duplicates()
        shared.python.file
            add list_files()
            new fn name()

    Homework:
        1. add new functions to your library
            examples:
                get extension,
                get path,
                does the file exist?
                is it a file or a path?
                copy
                move
                rename

        2. make a PR

## Week 5:

    Lecture:
        Maya.
        Install Maya.
        maya.cmds and maya.mel
        Maya commands:
            https://help.autodesk.com/view/MAYAUL/2022/ENU/
            right click menu in script editor

    Project 1:
        Get python running on Maya
        Environment Variables
        userSetup.py
        Maya.env
        C:\Users\<user-name>\OneDrive\Documents\maya\2023

    Project 2:
        shared.maya.core.attribute
        shared.maya.core.node

    Homework:
        1. play in Maya with your library

## Week 6:

    Lecture:
        context & decorators

    Project 1:
        with selection_restored():

    Project 2:
        @selection_restored_decorator

    Project 3:
        Start file batcher.

    Homework:
        Final project: file batcher

## Week 7-8:

    Lecture:
        File batcher lecture
        dict()
        json, yml & serialisation of data.
        underscores in names (json, or json)

    Project 1:
        Read / Write json data to files.

    Project 2 / Homework:
        File batcher.