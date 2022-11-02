def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    count = 0
    for i in data:
        if i.isalpha():
            count += 1
    return count

# Read data from file
a = open('txt_file/data02.txt')
data = a.read()
print(main(data))