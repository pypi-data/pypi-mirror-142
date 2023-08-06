import traceback
import logging
import os
from threading import Thread


def print(value=None):
    name = 'qts'
    trace = f'''
Traceback (most recent call last):
  File "{name}", line {hs}, in <module>
System Error: print is not defind
    '''
    printf(f'\033[31m\n{trace}\033[0m')


def printf(value):
    os.sys.stdout.write(value+"\n")


class Path:
    def __init__(self, path):
        self.path = path
        self.name = path

    def python2qts(self):
        with open(self.path)as f:
            data = f.read()
        name = self.name
        for y in range(len(data)):
            if data[y:y+1] == "#":
                data = data[0:y]+"//"+data[y+1:]
            if data[y:y+5] == "print" and data[y+5:y+6] != "f":
                data = data[0:y]+"printf"+data[y+5:]
            if data[y:y+3] == "def":
                data = data[0:y]+"func"+data[y+3:]
        return data

    def analysis(self):
        global hs
        hs = 1
        name = self.name
        with open(self.path)as f:
            data = f.read()
        try:
            for y in range(len(data)):
                if data[y:y+4] == "func":
                    data = data[0:y]+"def"+data[y+4:]
                if data[y:y+5] == "const":
                    data = data[0:y]+data[y+5:]
                if data[y:y+3] == "var":
                    data = data[0:y]+data[y+3:]
                if data[y:y+2] == "//":
                    data = data[0:y]+"#"+data[y+2:]
                    s = 1
                if data[y:y+7] == '!include':
                    data = data[0:y]+"import"+data[y+8:]
                if data[y:y+1] == "#" and s != 1:
                    trace = f'''
    Traceback (most recent call last):
    File "{name}", line {hs}, in <module> 
    Error: # is not defind
                    '''
                    printf(f'\033[31m\n{trace}\033[0m')
                if data[y:y+1] == "#" and s != 1:
                    trace = f'''
    Traceback (most recent call last):
    File "{name}", line {hs}, in <module> 
    Error: # is not defind
                    '''
                    printf(f'\033[31m\n{trace}\033[0m')
                if data[y:y+1] == "\n":
                    hs += 1
                s = 0

            exec(data)
        except Exception:
            trace = traceback.format_exc()
            for x in range(len(trace)):
                if trace[x:x+8] == "<string>":
                    trace = trace[0:x] + name + trace[x+8:]
                if trace[x] == '^':
                    trace = trace[:x+1]
                    break
            printf(f'\033[31m\n{trace}\nError\033[0m')


hs = 0


def main():
    try:
        while True:
            cmd = input("请输入命令:(analysis,python2qts)")
            if cmd == "analysis":
                name = input("请输入qts文件名（带路径）")
                with open(name)as f:
                    r = f.read()

                analysis(r)
            elif cmd == "python2qts":
                name = input("请输入py文件名（带路径）")
                with open(name)as f:
                    r = f.read()

                f = python2qts(r)
                name = input("请输入保存文件名")
                if os.path.exists(name):
                    c = input("文件已存在，请问是否继续")
                    if c == '是':
                        pass
                    else:
                        continue
                with open(name, "w")as fl:
                    fl.write(f)
                print("保存成功")
            else:
                raise SystemError("\033[31mcommand not found\033[0m")
    except KeyboardInterrupt:
        printf('\n')
        inp = input('是否退出')
        if inp == '是':
            quit()


if __name__ == '__main__':
    main()
