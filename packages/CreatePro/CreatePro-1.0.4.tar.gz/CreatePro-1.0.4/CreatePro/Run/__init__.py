"""
Run CreatePro
"""
import os
import sys

from ..ScriptEngine.Compiler import Tree


class Execute:
    def __init__(self):
        self.build = ''

    @staticmethod
    def main():
        if 'CreateInfo' in os.listdir(os.path.split(sys.argv[0])[0]):
            with open('CreateInfo') as info:
                build = Tree(info.read())
                build.dict()
                return build.tree()
        else:
            print('CreateInfo is missing, stop')
            print(__file__)


if __name__ == '__main__':
    raise ImportError("'Can't run")
else:
    print(Execute.main())
