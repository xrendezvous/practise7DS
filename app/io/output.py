import pandas


def output_text(text):
    """
    Outputs text to the console

    Args:
        text (str): text to output
    """
    print(text)


def write_file(filepath, text):
    """
    Writes text to the file

    Args:
        filepath (str): path to file
        text (str): text to be written to the file
    """
    with open(filepath, 'w') as file:
        file.write(text)


def write_file_pandas(filepath, dataframe):
    """
    Writes text to the file using pandas library

    Args:
        filepath (str): path to file
        dataframe (DataFrame): dataframe to be written to the file
    """
    dataframe.to_csv(filepath, index=False)

