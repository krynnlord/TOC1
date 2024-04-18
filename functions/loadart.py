# Load Art form DAT file Function
def loadart(filetitle, data):
    with open(filetitle, 'r') as file:
        data = file.read().rstrip()
        return(data)