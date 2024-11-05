import argparse
import json
import yaml


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration '
                                                 'files and shows a '
                                                 'difference.',
                                     epilog="          And that's how "
                                            "you'd foo a bar")

    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    sorted_first_file_dict, sorted_second_file_dict = open_files_return_dicts(args.first_file, args.second_file)
    generate_diff(sorted_first_file_dict, sorted_second_file_dict)


def generate_diff(sorted_first_file_dict, sorted_second_file_dict):
    """
    --Whats is it
    --Tomato sauce
    --... Why
    --For you spaghetti code
    """go
    ans_dict = {}
    for i in sorted_first_file_dict:
        print(type(sorted_first_file_dict[i]))
        print(i)
        if type(sorted_first_file_dict[i]) != dict:
            if i in sorted_second_file_dict:
                if sorted_first_file_dict[i] == sorted_second_file_dict[i]:
                    ans_dict[i] = sorted_first_file_dict[i]
                    sorted_second_file_dict.pop(i)
                else:
                    ans_dict["- " + i] = sorted_first_file_dict[i]
                    ans_dict["+ " + i] = sorted_second_file_dict[i]
                    sorted_second_file_dict.pop(i)
            else:
                ans_dict["- " + i] = sorted_first_file_dict[i]
        else:
            generate_diff(sorted_first_file_dict[i], sorted_second_file_dict[i])

    for i in sorted_second_file_dict:
        ans_dict["+ " + i] = sorted_second_file_dict[i]
    print(str(ans_dict))
    return str(ans_dict)

def open_files_return_dicts(path1, path2):
    try:
        with open(path1) as fh:
            first_file = yaml.load(fh, Loader=yaml.FullLoader)
        with open(path2) as fh:
            second_file = yaml.load(fh, Loader=yaml.FullLoader)
        sorted_first_file_dict = dict(sorted(first_file.items()))
        sorted_second_file_dict = dict(sorted(second_file.items()))
        #print(sorted_first_file_dict)
    except:
        sorted_first_file_dict = dict(sorted(path1.items()))
        sorted_second_file_dict = dict(sorted(path2.items()))
    return sorted_first_file_dict, sorted_second_file_dict




if __name__ == "__main__":
    main()