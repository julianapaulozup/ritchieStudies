#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool


def Run(input1, input2, input3):
    print(f"{fg(5)}Calculator!{attr(0)}")
    print(f"{fg(6)}My first number is {input1}.{attr(0)}")
    print(f"{fg(4)}My second number is {input2}.{attr(0)}")
    print(f"{fg(3)}I want to {input3} them.{attr(0)} ")

    op = 0 

    if input3 == "sum":
        op = int(input1)+ int(input2)
    elif input3 == "divide":
        op = int(input1)/int(input2)
    elif input3 == "subtract":
        op = int(input1)-int(input2)
    elif input3 == "multiply" :
        op = int(input1)*int(input2)

    print(f"{fg(2)}The result of the operation is {op}.{attr(0)} ")

