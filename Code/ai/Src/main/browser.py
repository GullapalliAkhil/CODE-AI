import subprocess
import json

import self as self


class BrowserCall:
    @staticmethod
    def call_browser():
        with open(r"..\CODE-AI\Code\ai\Src\main\config.json", "r") as read_file:
            data = json.load(read_file)
            typeOfBrowser = data['browserName']
            if typeOfBrowser.upper() in "CHROME":
                p = subprocess.Popen(["powershell.exe",
                                      f"start-process -FilePath 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' -ArgumentList '{data['urlToHit']}' "])
                p.communicate()
            elif typeOfBrowser.upper() in "FIREFOX":
                p = subprocess.Popen(["powershell.exe", f"start-process -FilePath 'C:\\Program Files\\Mozilla "
                                                        f"Firefox\\firefox.exe' -ArgumentList '{data['urlToHit']}' "])
                p.communicate()
            else:
                print("Please give the value which is supported by us.")


if __name__ == '__main__':
    BrowserCall.call_browser()