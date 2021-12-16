# Decryption function that has two args encrypted message and the key
def Decryption(encrypted, key):
    # Collect column and row values
    columns = range(len(encrypted))
    rows = range(key)

    # re-create matrix with rows and columns
    matrix = [['' for i in columns] for j in rows]
    # print(matrix)

    # create print check to know if we should print or not
    print_check = 0
    # Create a row and column check var to know when to print a character
    row_check = 0
    column_check = 0

    # create space filler '_' for spaces without characters
    for i in columns:
        if row_check == 0:
            print_check = 1
        if row_check == key - 1:
            print_check = 0

        # assign space filler
        matrix[row_check][column_check] = '_'
        # increment column check to move on
        column_check += 1

        # check if you have to go to the next row or take a step back
        if print_check:
            row_check += 1
        else:
            row_check -= 1

    # assign character to available spaces
    counter = 0
    for i in rows:
        for j in columns:
            if (matrix[i][j] == '_') and (counter < len(encrypted)):
                matrix[i][j] = encrypted[counter]
                counter += 1

    # create final list with letter and without space fillers
    final_list = []
    row_check, column_check = 0, 0
    for i in columns:

        # check the direction of flow
        if row_check == 0:
            print_check = 1
        if row_check == key - 1:
            print_check = 0

        # place the marker
        if matrix[row_check][column_check] != '_':
            final_list.append(matrix[row_check][column_check])
            column_check += 1

        # find the next row using
        # direction flag
        if print_check:
            row_check += 1
        else:
            row_check -= 1
    decrypted = "".join(final_list)
    return decrypted
