"""
Tree build
"""
import re


class LevelError(Exception):
    def __init__(self):
        print('level has some problem')


class Tree:
    def __init__(self, code):
        super(Tree, self).__init__()
        self.Tree = None
        self.Dict = {}
        self.state = None
        self.Leval = 0
        self.Describe = []
        doing = []
        final = []
        describe_line = code.split('\n')
        self.Data = code
        for i in describe_line:
            if i == '':
                continue
            level = re.search('[^ ]', i).span()[0] // 4
            if re.findall('~(.+?)~', i):
                continue
            elif level > self.Leval:
                pre = doing[-1][0:2]
                doing[-1] = pre + [True]
                doing.append([i.replace('\n', '').replace(' ', ''), level, False])
                self.Leval = level
            elif level < self.Leval or describe_line.index(i) == len(describe_line) - 1:  #
                doing.append([i.replace('\n', '').replace(' ', ''), level, False])
                final += doing
                doing = []
                self.Leval = 0
            elif level == self.Leval:
                doing.append([i.replace('\n', '').replace(' ', ''), level, False])
            else:
                raise LevelError
        self.Describe = final

    def dict(self):
        for i in self.Describe:
            split = i[0].split(':')
            self.Dict[split[0]] = i[1:3]

    def tree(self, leveled=0, father='~', data=None):
        doing = {}
        final = {}
        if data is None:
            data = self.Dict
        for k, v in data.items():
            if leveled == v[0]:
                if v[1]:
                    final[k] = None
                    doing = {}
                    father = k
                else:
                    final[k] = re.findall('[ ]*' + k + ':(.+?)', self.Data)[0]
            elif leveled > v[0]:
                doing[k] = v
            else:
                doing[k] = v
                final[father] = self.tree(leveled + 1, father, doing)
        return final


class Form:
    def __init__(self, code):
        code = code.split('\n')
        self.level = []
        for i in code:
            self.level.append(i.count(' ') // 4)
        self.code = [i.replace(' ', '') for i in code]

    def make(self, base, code=None, level=None):
        if (code and level) is None:
            code = self.code
            level = self.level
        wait = False  # wait or not
        pre_c = []  # making code
        pre_l = []  # making level
        out = {}  # final
        last = ''  # the key before
        for code_, level_ in zip(code, level):  # iter code, level
            if level_ == base:  # a small tree
                if wait:
                    out[last] = self.make(base + 1, pre_c, pre_l)
                if code_[-1] == ':':  # tree block
                    last = code_.split(':')[0]
                    wait = True
                elif code_[-1] != ':':
                    split = code_.split(':')
                    out[split[0]] = split[1]
            elif level_ > base:  # son level
                pre_c.append(code_)
                pre_l.append(level_)
        return out
