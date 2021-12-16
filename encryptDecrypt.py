def EncryptDecrypt(text_input, key):
    # Collect column and row values
    column = range(len(text_input))
    row = range(key)

    # form matrix with rows and columns
    matrix = [["" for i in column] for j in row]
    print(matrix)