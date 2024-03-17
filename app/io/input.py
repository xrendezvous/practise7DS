import pandas


def input_text():
    """
    For entering text from the console

    Returns:
        str: text entered by the user
    """
    return input("enter your text: ")


def read_file(filepath):
    """
    Reads the contents of a file

    Args:
        filepath (str): path to the file

    Returns:
        str: content of the file
    """
    with open(filepath, "r") as file:
        return file.read()


def read_file_pandas(filepath):
    """
    Reads the contents of a file using pandas library

    Args:
        filepath (str): path to the file

    Returns:
        DataFrame: content of the file
    """
    return pandas.read_csv(filepath)

