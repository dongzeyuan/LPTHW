from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())                           # 将文件全部打印出来


def rewind(f):
    f.seek(0)                                 # 将当前位置归到0位置，就是文件第一个字节的位置


def print_a_line(line_count, f):
    print(line_count, f.readline())           # 将行号打印出来，后续打印出对应行号的内容


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)                          # 将当前位置归到0位置，从头开始

print("Let's print three lines:")

current_line = 1                              # 将第一行打印出来，之前加行号
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)      # 行号+1，打印出行号+1 行的内容

current_line += 1
print_a_line(current_line, current_file)

