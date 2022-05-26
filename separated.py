""" Graham Brown
    CSC 110 SP22 001-2
    Project -7

    This project is designed to reinforce the techniques around Python lists, dictionaries, and files.
    The program will consist of 6 functions related to “comma-separated values”.
    Some of these functions consist of making comma-separated strings and lists of those strings where each index is dictated by the commas.
    Then some of these functions have us take these strings and lists and write them to a .csv file or read these strings and lists from the .csv file.
    This program overall consists of reading and writing .csv files, string manipulation, list manipulation and dictionary manipulation.


    Functions:
        separate_by_commas(string):
            Has one argument 'strings' which is a string containing characters and commas.
            This function will return a list of strings based on commas. However, if the comma is inside of a quote, it will be ignored and put into the same index.

        create_comma_separated_string(list_of_strings):
            Has one argument 'list_of_strings' which is a list list of strings.
            This function will create a comma-separated string and will add quotation marks to any string that contains a comma.

        csv_file_to_list_of_lists(filename):
            Has one argument 'filename' which is a .csv file.
            This function will read 'filename' and each comma-separated line of the file will become a list of strings. Therefore, the whole file will become a list of those lists.

        list_of_lists_to_csv_file(filename, list_of_lists):
            Has two arguments: 'filename' which is a .csv file and 'list_of_lists' which is a list of lists of strings.
            This function will take 'list_of_lists' and turn it into a comma-separated string which will be written to 'filename'.

        csv_file_to_list_of_dictionaries(filename):
            Has one argument 'filename' which is a .csv file.
            This function will read a comma-separated file that is encoded to represent dictionaries. It returns a list of those dictionaries.

        list_of_dictionaries_to_csv_file(filename, list_of_dictionaries):
            Has two arguments: 'filename' which is a .csv file and 'list_of_dictionaries' which is a list of dictionaries.
            This function creates a file that encodes the dictionaries inside of 'list_of_dictionaries' in the same format as the file in 'csv_file_to_list_of_dictionaries'.
"""

def separate_by_commas(string):
    """
    Args:
        string: A string of characters and quotations split by commas.
    Returns:
        This function returns a list of strings which splits 'string' at every comma unless it is inside of quotations.
    """
    result = []
    temp = ''
    in_quotes = False
    for char in string:
        # Check for no quotes and commas, add our temporary string to result
        if char == ',' and not in_quotes:
            result.append(temp)
            temp = ''
        #check for quotes
        elif char == '"':
            if in_quotes == True:
                in_quotes = False
            else:
               in_quotes = True
        #if not in quotes and not a comma, add to the temporary string.
        #it will be added to result
        else:
            temp += char

    result.append(temp)
    return result

def create_comma_separated_string(list_of_strings):
    """
    Args:
        list_of_strings: A list of strings.

    Returns:
        This function returns a comma-separated string. After every index there will be a comma and if the current index contains a comma, then the function will add quotation marks to the string.
    """
    result = ''
    prev_char = ''
    for char in range(len(list_of_strings)):
        #check for a comma in the string, if there is we need to add quotations
        if ',' in list_of_strings[char]:
            result += '"'
            result += list_of_strings[char]
            result += '"'
        else:
            #if there is no comma in the current index and it's not the list index, add it to result and add a comma to the end
            if char != len(list_of_strings)-1:
                result += list_of_strings[char] + ','
            else:
                if list_of_strings[char] == '' and prev_char != '':
                    result += ','
                else:
                    result += list_of_strings[char]
        prev_char = list_of_strings[char]
    return result

def csv_file_to_list_of_lists(filename):
    """
    Args:
        filename: A .csv named file to read.

    Returns:
        This function reads in a file and each comma-separated line of the file will become a list of strings.
        And, therefore, the whole file will become a list of those lists.
    """
    open_file = open(filename, 'r')
    giant_str = ''
    for line in open_file:
        giant_str += line
    open_file.close()
    split_by_line = giant_str.split('\n')
    result = []
    for line in split_by_line:
        result.append(separate_by_commas(line))
    return result

def list_of_lists_to_csv_file(filename, list_of_lists):
    """
    Args:
        filename: A .csv named file to write to write to.
        list_of_lists: A list of lists of strings.

    Returns:
        This function takes a list of lists of strings and writes it to the named file as comma-separated values.
        The function will then return the number of lines of output it generated to the named file.
    """
    open_file = open(filename, 'w')
    count = 0
    index = 0
    for L in list_of_lists:
        open_file.write(create_comma_separated_string(L))
        if index != len(list_of_lists)-1:
            open_file.write('\n')
        count+=1
        index += 1
    open_file.close()
    return count

def csv_file_to_list_of_dictionaries(filename):
    """
    Args:
        filename: A comma-separated file to read. It is encoded to represent dictionaries.

    Returns:
        This function returns a list of dictionaries. The first row of the file is the list of keys that are are associated with the values in the same column below it in the file.
        Ex: name,number
            Alice,555-1234
            Bob,555-9999
    """
    opened_filed = open(filename,'r')
    information = []
    result = []
    string = ''
    #remove the '\n'
    for line in opened_filed:
        string += line
    split_string = string.split('\n')

    #new lists without '\n'
    for string in split_string:
        information.append(separate_by_commas(string))

    #get the keys of the dict
    keys = []
    for L in range(len(information)):
        for info in information[L]:
            if L == 0:
                keys.append(info)

    #go through each row of the person in 'information'
    #keep a count for our column_count
    #make key the 0 index of information for that column_count
    #make the value the column_count of that person's information
    temp = {}
    column_count = 0
    for info in range(1,len(information)):
        while column_count < len(keys):
            temp[information[0][column_count]] = information[info][column_count]
            if column_count == len(keys)-1:
                result.append(temp)
            column_count+=1
        temp = {}
        column_count = 0

    return result

def list_of_dictionaries_to_csv_file(filename,list_of_dictionaries):
    """
    Args:
        filename: A .csv file to write to.
        list_of_dictionaries: A list of dictionaries

    Returns:
        This function creates a file that writes the dictionaries to it.
        The values are written in the first row and the corresponding values for those keys are written below them in the corresponding column.

    """
    if len(list_of_dictionaries) == 0:
        return None
    else:
        open_file = open(filename,'w')
        temp = []
        #add keys to top
        i = 0
        for D in list_of_dictionaries:
            for key in D:
                value = D[key]
                if key not in temp:
                    temp.append(key)
                    open_file.write(key)
                    if i < len(D)-1:
                        open_file.write(',')
                i+=1
            i=0
        #make sure the dicitonaries are in correct order
        #add them to a new list in correct key order
        key_order = {}
        order = {}
        for D in range(0,1):
            for key in list_of_dictionaries[D]:
                key_order[key] = ''
                order[key] = ''

        new = []
        x = 0
        for D in list_of_dictionaries:
            for key in D:
                value = D[key]
                key_order[key] = value
                if x == len(D)-1:
                    new.append(key_order)
                x+=1
            key_order = order
            x=0

        #add values below keys
        #count amount of times we write '\n'
        #count starts at 1 to account for the first row we wrote in above
        index = 0
        count = 1
        for D in new:
            open_file.write('\n')
            count+=1
            for key in D:
                value = D[key]
                open_file.write(value)
                if index < len(D)-1:
                    open_file.write(',')
                index += 1
            index = 0

    return count



def main():
    create_comma_separated_string(['', '', ''],)
    create_comma_separated_string(['a', '"b,c"', ''],)
    #list_of_lists_to_csv_file('testing.csv',[[''], ['a', 'b', 'c'], ['a', '"b,c"', ''], ['', '', '']])
   # csv_file_to_list_of_dictionaries('lod.csv')
    #list_of_dictionaries_to_csv_file('testing.csv', [{'name': 'Alice', 'age': '21', 'city': 'Tucson'}, {'age': '19', 'city': 'Mesa', 'name': 'Bob'}])
main()
