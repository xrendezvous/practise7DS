import os


def output_text(text):
    """
    Outputs text to the console

    Args:
        text (str): text to output
    """
    print(f'Output text: {text}')


def write_file(filepath, text):
    """
    Writes text to the file

    Args:
        filepath (str): path to file
        text (str): text to be written to the file
    """
    with open(filepath, 'a') as file:
        file.write(text)
        file.write('\n')


def write_file_pandas(filepath, dataframe):
    """
    Writes text to the file using pandas library

    Args:
        filepath (str): path to file
        dataframe (DataFrame): dataframe to be written to the file
    """
    if not dataframe.empty:
        header = not os.path.exists(filepath)
        dataframe.to_csv(filepath, mode='a', index=False, header=header)
    else:
        print("Dataframe is empty. No data written to file.")

