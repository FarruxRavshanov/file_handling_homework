def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)

# Read data from file
a = open('txt_file/data02.txt')
data = a.read()
print(main(data))