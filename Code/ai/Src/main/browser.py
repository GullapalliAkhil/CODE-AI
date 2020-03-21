import subprocess
import json
import webbrowser

from Code.ai.Src.main.Config import configurations_to_run


class BrowserCall:
    @staticmethod
    def call_browser():
        typeOfBrowser = configurations_to_run.browserName
        product_url = configurations_to_run.urlToHit
        if typeOfBrowser.upper() in "CHROME":
            if configurations_to_run.Operating_System == 'MacOS':
                chrome_path = 'open -a /Applications/Google\\ Chrome.app %s'
                webbrowser.get(chrome_path).open(product_url)
            elif configurations_to_run.Operating_System == 'Windows':
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(product_url)
            elif configurations_to_run.Operating_System == 'Linux':
                chrome_path = '/usr/bin/google-chrome %s'
                webbrowser.get(chrome_path).open(product_url)
            else:
                print("We didn't support for the operating system you had.")

        elif typeOfBrowser.upper() in "FIREFOX":
            p = subprocess.Popen(["powershell.exe", f"start-process -FilePath 'C:\\Program Files\\Mozilla "
                                                    f"Firefox\\firefox.exe' -ArgumentList '{data['urlToHit']}' "])
            p.communicate()
        else:
            print("Please give the value which is supported by us.")


if __name__ == '__main__':
    BrowserCall.call_browser()
