def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = []
    if data.isdigit():
        a.append()
    return a
    
# Read data from file
a = open('txt_file/data03.txt')
data = a.read()
print(main(data))