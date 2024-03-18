import pandas
import os
import pytest
from app.io.input import read_file, read_file_pandas


def test_read_file():
    """
    Test reading from a text file with some data

    Asserts:
         the read content matches the written content
    """
    with open("test_file.txt", "w") as f:
        f.write("tests info")

    assert read_file("test_file.txt") == "tests info"
    os.remove("test_file.txt")


def test_read_file_empty():
    """
    Test reading from an empty text file

    Asserts:
        the read content is an empty string
    """
    open("test_empty_file.txt", "w").close()
    assert read_file("test_empty_file.txt") == ""
    os.remove("test_empty_file.txt")


def test_read_file_not_exist():
    """
    Test reading from a non-existent file

    Asserts:
        raising a FileNotFoundError
    """
    with pytest.raises(FileNotFoundError):
        read_file("not_existing_file.txt")


@pytest.fixture
def csv_file(tmpdir):
    """
    Creates a temporary CSV file with some data

    Args:
        tmpdir: provides a temporary unique directory for tests

    Returns:
        Filepath to the created CSV file
    """
    data = pandas.DataFrame({
        "Column1": ["row1", "row2"],
        "Column2": ["row1", "row2"],
    })
    filepath = tmpdir.join("test_file.csv")
    data.to_csv(filepath, index=False)
    return filepath


def test_read_file_pandas(csv_file):
    """
    Test reading from a CSV file with pandas

    Args:
        csv_file: provides a content to read from

    Asserts:
        the DataFrame is not empty;
        the columns match the expected ones;
        the content match the expected
    """
    df = read_file_pandas(csv_file)
    assert not df.empty
    assert list(df.columns) == ["Column1", "Column2"]
    assert df.iloc[0]["Column1"] == "row1"


def test_read_file_pandas_empty(tmpdir):
    """
    Test reading from an empty CSV file with pandas

    Args:
        tmpdir: provides a temporary unique directory for tests

    Asserts:
        the DataFrame is empty
    """
    filepath = tmpdir.join("empty_file.csv")
    filepath.write("")
    df = read_file_pandas(str(filepath))
    assert df.empty


def test_read_file_pandas_not_exist(tmpdir):
    """
    Test reading from a non-existent CSV file with pandas

    Args:
       tmpdir: provides a temporary unique directory for tests

    Asserts:
       the DataFrame is empty
    """
    filepath = tmpdir.join("not_existing_file.csv")
    df = read_file_pandas(str(filepath))
    assert df.empty
