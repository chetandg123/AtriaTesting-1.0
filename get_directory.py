import os


class DirectoryPath():

    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd,'Driver/chromedriver')
        return download_path

    def get_download_dir(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd,'Downloads')
        return download_path
