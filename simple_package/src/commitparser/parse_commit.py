"""
A function that reads a commit message, and returns info about the message
measage: "submit ~My assignment name~ file1.py file2.py ..."
"""


def parse_commit(commit):
    if not commit.startswith('submit '):
        return False
    assignment = commit[commit.find('~'):commit.rfind('~')]
    file = [file for file in commit[commit.rfind('~'):].split(' ') if file][0]
    return assignment, file
