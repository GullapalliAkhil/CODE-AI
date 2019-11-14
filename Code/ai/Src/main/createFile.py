import os

"""This class helps us to create the required directory and files. A file named main.java will be created with a 
class name and main method. In that main method depends up on the user inputs code will be get created automatically. 
if user selects the browser as chrome, code which helps to launch the chrome browser will be build automatically in 
the main.java file. 
User Just need to import the required modules and run the file.
Currently for now we are only supporting the chrome and firefox browsers."""


def createFile():
    path = input("Please give the path name: ")  # For example /Project/Automaton
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
    # file creation
    typeOfFile = input("Please give the name to create the type of file: ")
    if typeOfFile in "java":
        filePath = os.path.join(path, 'main.java')
        f = open(filePath, 'a+')
        productName = input("Please provide the name of the class :")
        f.write(f'class {productName}\n')
        f.write("{")
        f.write("\n public static void main(String args[]){\n")
        typeOfBrowser = input("Please type the name of the browser on which you need to run your test cases : ")
        if typeOfBrowser.upper() in "CHROME":
            chromeDriverPath = input("Please provide the chromedriver.exe path : ")
            f.write(f'System.setProperty("webdriver.chrome.driver","{chromeDriverPath}");')
            f.write("\n WebDriver driver = new ChromeDriver();\n")
        elif typeOfBrowser.upper() in "FIREFOX":
            f.write("WebDriver driver = new FirefoxDriver();\n")
        productURL = input("Please give the valid url to hit the servers :")
        f.write(f'driver.get("{productURL}");\n')
        f.write("}\n")
        f.write("}")
        print("A java file with the above parameters successfully")
        f.close()

    else:
        print("Thanks for remembering us to make this product supports for", typeOfFile)


if __name__ == '__main__':
    createFile()
