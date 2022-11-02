from this import d


def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    i = 0
    s = []
    while i < len(data):
        if data[i].isdigit:
            s.append(i)
        i += 1
    return s
    
# Read data from file
a = open('txt_file/data03.txt')
data = a.read()
print(main(data))