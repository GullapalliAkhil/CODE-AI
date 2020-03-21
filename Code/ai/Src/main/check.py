# This class checks whether any close bracket or open brackets is missing in code.
import json
import time

from Code.ai.Src.main.Config import configurations_to_run


class Check:
    @staticmethod
    def check_file():
        path = configurations_to_run.pathName
        f = open(f'{path}/main.java', "r")
        if f.mode == 'r':
            contents = f.read()
            specialChar = []
            chars = ['{', '}', '(', ')', ']', '[']
            for char in contents:
                if char in chars:
                    specialChar.append(char)
            stack = []
            for i in range(len(specialChar)):
                if specialChar[i] is '{' or specialChar[i] is '[' or specialChar[i] is '(':
                    stack.append(specialChar[i])
                    continue
                elif specialChar[i] is '}' or specialChar[i] is ']' or specialChar[i] is ')':
                    if len(stack) == 0:
                        return False
                    else:
                        x = stack.pop()
                        syntaxValidation = Check.match(x, specialChar[i])
                        if syntaxValidation is False:
                            return False
            if len(stack) == 0:
                return True
            else:
                return False

    @staticmethod
    def match(char1, char2):
        if char1 == '{' and char2 == '}':
            return True
        elif char1 == '(' and char2 == ')':
            return True
        elif char1 == "[" and char2 == "]":
            return True
        else:
            return False

    @ staticmethod
    def syntax_validation():
        value = Check.check_file()
        path = configurations_to_run.pathName
        f = open(f'{path}/main.java', "a")
        if value:
            print("No Syntax errors in the java file created.")
            f.write("/*NOTE: - No Syntax Errors */\n")
            f.close()
        else:
            print("Syntax error")
            f.write("/*NOTE: - OOPS!, I need to improve my coding skills. Sorry there is some problem with the "
                    "Syntax in this file, please fix that in order to run this program.*/\n")
            f.close()


if __name__ == '__main__':
    Check.syntax_validation()
