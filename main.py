from app.io.input import input_text, read_file_pandas, read_file
from app.io.output import output_text, write_file, write_file_pandas


def main():
    console_text = input_text()
    output_text(console_text)
    write_file('output.txt', console_text)

    file_text = read_file('output.txt')
    output_text(file_text)
    write_file('output.txt', file_text)

    # data_frame = read_file_pandas('example.csv')
    # data_frame_text = str(data_frame)
    # output_text(data_frame_text)
    # write_file('pandas_output.txt', data_frame_text)


if __name__ == '__main__':
    main()