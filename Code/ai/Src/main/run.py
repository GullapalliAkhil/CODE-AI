from Code.ai.Src.main.browser import BrowserCall
from Code.ai.Src.main.check import Check
from Code.ai.Src.main.createFile import CreateCode


class Run:
    @staticmethod
    def run_files():
        CreateCode.create_file()  # Create the Java or Python Files.
        BrowserCall.call_browser()  # Open browser through power shell.
        Check.syntax_validation()  # Syntax Validations


if __name__ == '__main__':
    Run.run_files()
