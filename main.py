import pandas

from app.io.input import input_text, read_file_pandas, read_file
from app.io.output import output_text, write_file, write_file_pandas


def main():
    console_text = input_text()
    output_text(console_text)
    write_file('output.txt', console_text)

    file_text = read_file('output.txt')
    output_text(file_text)
    write_file('text_from_file.txt', file_text)

    new_row = pandas.DataFrame({'Column1': [console_text]})
    write_file_pandas('new_csv_file.csv', new_row)

    df_from_file = read_file_pandas('new_csv_file.csv')
    df_text = str(df_from_file)
    output_text(df_text)
    write_file('pandas_read_output.txt', df_text)


if __name__ == '__main__':
    main()