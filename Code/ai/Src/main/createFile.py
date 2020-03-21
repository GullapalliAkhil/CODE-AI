import os
import json
import requests

from Code.ai.Src.main.Config import configurations_to_run

"""This class helps us to create the required directory and files. A file named main.java will be created with a 
class name and main method. In that main method depends up on the user inputs code will be get created automatically. 
if user selects the browser as chrome, code which helps to launch the chrome browser will be build automatically in 
the main.java file. 
User Just need to import the required modules and run the file.
Currently for now we are only supporting the chrome and firefox browsers."""


class CreateCode:
    @staticmethod
    def create_file():
        path = configurations_to_run.pathName  # For example /Project/Automaton
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)
        # file creation
        typeOfFile = configurations_to_run.LanguageCode
        if typeOfFile in "java":
            filePath = os.path.join(path, 'main.java')
            f = open(filePath, 'a+')
            productName = configurations_to_run.className
            f.write(f'class {productName}\n')
            f.write("{")
            f.write("\n public static void main(String args[]){\n")
            typeOfBrowser = configurations_to_run.browserName
            if typeOfBrowser.upper() in "CHROME":
                chromeDriverPath = configurations_to_run.chrome_driver_loc
                f.write(f'System.setProperty("webdriver.chrome.driver","{chromeDriverPath}");')
                f.write("\n WebDriver driver = new ChromeDriver();\n")
            elif typeOfBrowser.upper() in "FIREFOX":
                f.write("WebDriver driver = new FirefoxDriver();\n")
            productURL = configurations_to_run.urlToHit
            try:
                r = requests.head(productURL)
                f.write(f'driver.get("{productURL}");\n')
            except requests.ConnectionError:
                print("Connection Error, Your API is not able to make a contact with your server")
                f.write("/*NOTE: - Connection Error, Your API is not able to make a contact with your server.*/\n")
            f.write("}\n")
            f.write("}")
            print("A java file with the above parameters successfully")
            f.close()

        else:
            print("Thanks for remembering us to make this product supports for", typeOfFile)


if __name__ == '__main__':
    CreateCode.create_file()
