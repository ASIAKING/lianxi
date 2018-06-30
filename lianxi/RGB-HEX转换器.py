"""
在这个项目中，我们将使用位操作符来构建一个可以转换的计算器RGB值到十六进制(十六进制)值反之亦然。

我们将向项目添加三种方法：

一种将RGB转换为十六进制的方法
一种将十六进制转换为RGB的方法
启动提示周期的方法。
该方案应做以下工作：

提示用户输入他们想要的转换类型。
要求用户输入rgb或十六进制值。
使用按位运算符和移位以转换值
将转换后的值打印给用户
"""


def rgb_hex():
    invalid_msg = "Some error message goes here..."
    red = int(input("Enter red (R) value: "))
    if (red < 0 or red > 255):
        print(invalid_msg)
        return
    green = int(input("Enter green (R) value: "))
    if (green < 0 or green > 255):
        print(invalid_msg)
        return
    blue = int(input("Enter blue (R) value: "))
    if (blue < 0 or blue > 255):
        print(invalid_msg)
        return
    val = (red << 16) + (green << 8) + blue
    print("%s" % (hex(val)[2:]).upper())


def hex_rgb():
    hex_val = input("Enter the color (six hexadecimal digits): ")
    if len(hex_val) != 6:
        print("Invalid hexidecimal value. Try again.")
        return
    else:
        hex_val = int(hex_val, 16)
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print("Red: %s Green: %s Blue: %s" % (red, green, blue))


def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
        if option == '1':
            print("RGB to Hex...")
            rgb_hex()
        elif option == '2':
            print("HEX to RGB...")
            hex_rgb()
        elif option == 'X' or option == 'x':
            break
        else:
            print('Error')
convert()
