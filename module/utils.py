
import os

__author__ = 'Gwena Cunha'

""" Utils Module

    1. Function to get project directory name
    2. Separates sentences in string
    
"""

# Constants
BLEU_NAME = "BLEU"
GOOGLE_BLEU_NAME = "Google-BLEU"
WER_NAME = "WER"
TER_NAME = "TER"


def project_dir_name():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    project_dir = os.path.abspath(current_dir + "/../") + "/"
    # print("Project dir: " + project_dir)
    return project_dir

