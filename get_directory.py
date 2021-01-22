import os


class reuseable():
    # def get_driver_path(self):
    #     cwd = os.path.dirname(__file__)
    #     driver_path = os.path.join(cwd, 'Driver/chromedriver')
    #     return driver_path

    def get_download_dir(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, '/home/chetan/Downloads/Atria_Project/AtriaTesting-1.0/Downloads')
        return download_path