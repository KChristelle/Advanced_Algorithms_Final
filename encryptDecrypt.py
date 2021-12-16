# Function for encryption takes two args text and key
def EncryptDecrypt(text_input, key):
    # Collect column and row values
    columns = range(len(text_input))
    rows = range(key)

    # form matrix with rows and columns
    matrix = [["" for i in columns] for j in rows]
    # print(matrix)
    # create print check to know if we should print or not
    print_check = 0
    # Create a row check var to know when to print a character
    row_check = 0

    #     Loop through text to get each letter and print in matrix
    for i in range(len(text_input)):
        # Print character of the text into matrix, ex: matrix[0][0]
        matrix[row_check][i] = text_input[i]
        # print(matrix)
        # print(matrix)
        # check if you are on the first row then print in first column
        if row_check == 0:
            print_check = 0
        # if you are on second row then
        elif row_check == key - 1:
            print_check = 1

        if print_check == 0:
            row_check += 1
        else:
            row_check -= 1
    # print(matrix)
    # empty list to contain matrix without empty values
    encrypt_message = []
    for i in rows:
        for j in columns:
            # check if matrix element is empty
            if matrix[i][j] == '':
                continue
            # else append value to new list
            else:
                encrypt_message.append(matrix[i][j])
    # print(encrypt_message)
    message = "".join(encrypt_message)
    # print(message)
    return message
