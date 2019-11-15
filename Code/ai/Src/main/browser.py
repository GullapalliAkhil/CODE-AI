import subprocess
import json

import self as self


class BrowserCall:
    @staticmethod
    def call_browser():
        with open(r"C:\Users\AKHIL\Desktop\CODE-AI\Code\ai\Src\main\config.json", "r") as read_file:
            data = json.load(read_file)
            p = subprocess.Popen(["powershell.exe", f"start-process -FilePath 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' -ArgumentList '{data['urlToHit']}' "])
            p.communicate()


if __name__ == '__main__':
    BrowserCall.call_browser()