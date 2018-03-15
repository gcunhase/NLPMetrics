
import os
import random
import shutil

__author__ = 'Gwena Cunha'

""" Utils Module

    1. Separate train and test data (80 and 20% respectively)
    2. Optional shuffle function
    3. [Modification 1] Get train and test data from 2 separate files, no percentage needed
    4. [Modification 2] Added function to get project directory name

    Link: https://github.com/gcunhase/SentenceCorrection/blob/master/Datasets/separate_train_test_data.py

    Date: Jan 24th 2017
    Modified on Sep. 1st 2017 as a module
    Second function added on Feb 27th 2018
"""


def project_dir_name():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    project_dir = os.path.abspath(current_dir + "/../") + "/"
    # print("Project dir: " + project_dir)
    return project_dir


def copy_part_of_file(num_lines, filename, filename_out):
    # Save part of file in another file
    file_in = open(filename, "r")
    file_out = open(filename_out, "w")
    count = 0
    for line in file_in:
        if count < 4:
            file_out.write(line)
        else:
            break
        count += 1


def separate(data_dir, input_filename, output_filename, shuffle_var, train_percentage=0.8):
    ''' Function to separate train and test data into translate format

        Input:
            shuffle_var: boolean that determines whether sentences will be shuffled or not.
            data_dir = "./signalmedia-1m-jsonl/"
            input_filename = "input.txt"
            output_filename = "output.txt"

        Output (saved files):
            input_train = "giga-fren.release2.fixed.en"
            output_train = "giga-fren.release2.fixed.fr"
            input_test = "newstest2013.en"
            output_test = "newstest2013.fr"
            training-giga-fren.tar: compressed file with giga files
    '''

    input_path = data_dir + input_filename
    output_path = data_dir + output_filename

    input_train_p = "giga-fren.release2.fixed.en"
    input_train_path = data_dir + input_train_p
    output_train_p = "giga-fren.release2.fixed.fr"
    output_train_path = data_dir + output_train_p

    input_test_path = data_dir + "newstest2013.en"
    output_test_path = data_dir + "newstest2013.fr"

    #train_percentage = 0.8  # 80%
    test_percentage = 1 - train_percentage

    # Open files
    print("Opening files...")
    input_file = open(input_path, "r")
    input_train_file = open(input_train_path, "w")
    input_test_file = open(input_test_path, "w")

    output_file = open(output_path, "r")
    output_train_file = open(output_train_path, "w")
    output_test_file = open(output_test_path, "w")

    input_file_info = input_file.read().split("\n")
    output_file_info = output_file.read().split("\n")
    n_total = len(input_file_info)
    n_train = int(round(n_total * train_percentage))
    # n_test = n_total-n_train


    # Shuffle
    print("Shuffling sentences...")
    if (shuffle_var == True):
        c = list(zip(input_file_info, output_file_info))
        random.shuffle(c)
        input_file_info, output_file_info = zip(*c)

    # Divide train and test
    for j in range(0, n_train):
        input_train_file.write(input_file_info[j] + "\n")
        output_train_file.write(output_file_info[j] + "\n")

    for j in range(n_train, n_total):
        input_test_file.write(input_file_info[j] + "\n")
        output_test_file.write(output_file_info[j] + "\n")

    os.system('gzip ' + input_train_path)
    os.system('gzip ' + output_train_path)

    os.system('cd ' + data_dir + '; tar -cf training-giga-fren.tar ' + input_train_p + '.gz ' + output_train_p + '.gz')

    # Close open files
    print("Closing files...")
    input_file.close()
    input_train_file.close()
    input_test_file.close()

    output_file.close()
    output_train_file.close()
    output_test_file.close()


def shuffle_files(train_input_path, train_output_path, input_train_path, output_train_path):
    train_input_file = open(train_input_path, "r")
    train_input_file_info = train_input_file.read().split("\n")
    train_output_file = open(train_output_path, "r")
    train_output_file_info = train_output_file.read().split("\n")
    input_train_file = open(input_train_path, "w")
    output_train_file = open(output_train_path, "w")

    # Shuffle sentences
    c = list(zip(train_input_file_info, train_output_file_info))
    random.shuffle(c)
    train_input_file_info, train_output_file_info = zip(*c)
    for j in range(0, len(train_input_file_info)):
        input_train_file.write(train_input_file_info[j] + "\n")
        output_train_file.write(train_output_file_info[j] + "\n")
    train_input_file.close()
    train_output_file.close()
    input_train_file.close()
    output_train_file.close()


def separate_from_train_and_test(result_data_dir, train_data_dir, train_input_filename, train_output_filename, test_data_dir, test_input_filename, test_output_filename, shuffle_var=False):
    ''' Function to transform train and test files into translate format

        Input:
            result_data_dir = "titleGenerationDataset/cnn_result/train_test/"
            train_data_dir = "titleGenerationDataset/cnn_result/train/"
            test_data_dir = "titleGenerationDataset/cnn_result/test/"
            train_input_filename = "train_input.txt"
            train_output_filename = "train_output.txt"
            test_input_filename = "test_input.txt"
            test_output_filename = "test_output.txt"
            shuffle_var: boolean that determines whether sentences will be shuffled or not.

        Output (saved files):
            input_train = "giga-fren.release2.fixed.en"
            output_train = "giga-fren.release2.fixed.fr"
            input_test = "newstest2013.en"
            output_test = "newstest2013.fr"
            training-giga-fren.tar: compressed file with giga files
    '''

    train_input_path = train_data_dir + train_input_filename
    train_output_path = train_data_dir + train_output_filename
    test_input_path = test_data_dir + test_input_filename
    test_output_path = test_data_dir + test_output_filename

    input_train_p = "giga-fren.release2.fixed.en"
    input_train_path = result_data_dir + input_train_p
    output_train_p = "giga-fren.release2.fixed.fr"
    output_train_path = result_data_dir + output_train_p

    input_test_path = result_data_dir + "newstest2013.en"
    output_test_path = result_data_dir + "newstest2013.fr"


    if shuffle_var:
        print("Open train files and shuffle sentences...")
        shuffle_files(train_input_path, train_output_path, input_train_path, output_train_path)

        print("Open test files and shuffle sentences...")
        shuffle_files(test_input_path, test_output_path, input_test_path, output_test_path)
    else:
        print("Copying files...")
        shutil.copy2(train_input_path, input_train_path)
        shutil.copy2(train_output_path, output_train_path)
        shutil.copy2(test_input_path, input_test_path)
        shutil.copy2(test_output_path, output_test_path)

    os.system('gzip ' + input_train_path)
    os.system('gzip ' + output_train_path)

    os.system('cd ' + result_data_dir + '; tar -cf training-giga-fren.tar ' + input_train_p + '.gz ' + output_train_p + '.gz')

    print("Finished separating files...")
