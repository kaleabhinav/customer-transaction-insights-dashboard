from dataclasses import dataclass
import os

@dataclass

class DirConfig():

    data_path : str = os.path.join(os.getcwd(),'archive','CC GENERAL.csv')

