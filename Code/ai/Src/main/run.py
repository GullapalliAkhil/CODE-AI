from Code.ai.Src.main.browser import BrowserCall
from Code.ai.Src.main.createFile import CreateCode


class Run:
    @staticmethod
    def run_files():
        CreateCode.create_file()  # Create the Java or Python Files.
        BrowserCall.call_browser()  # Open browser through power shell.


if __name__ == '__main__':
    Run.run_files()

