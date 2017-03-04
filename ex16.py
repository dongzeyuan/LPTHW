from sys import argv

script, filename = argv                                  # 参数传递文件名

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input ("?")                                              # 这个地方按回车继续下一步，其实怎么都会下一步

print ("Opening the file...")
target = open(filename, 'w')                             # 用写模式打开文件，注意python3里 w是小写

print ("Truncating the file. Goodbye!")
target.truncate()                                        # 清空文件内容

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")                                 # 提示输入三行新内容

print ("I'm going to write these to the file.")

target.write (line1)
target.write ("\n")
target.write (line2)
target.write ("\n")
target.write (line3)
target.write ("\n")                                     # 将输入的三行内容写入，每行结尾换行

print ("And finally, we close it.")                     # 关闭文件
target.close()
