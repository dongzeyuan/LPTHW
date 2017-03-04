from sys import argv

script, filename = argv

txt = open(filename)                        # 前三行打开了一个文件，文件名在打开脚本时用参数传递

print ("Here's your file %r:" % filename)   # 显示文件名称
print (txt.read())                          # 显示文件内容

print("Type the filename again:")
file_again = input("> ")                    # 提示用户再次输入一个文件名称，这里还是ex15_sample.txt

txt_again = open(file_again)                # 打开输入的文件名

print (txt_again.read())                    # 打印出输入文件名的内容
