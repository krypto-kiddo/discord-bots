# just a parser untill we get write permissions to stack
# This function opens a txt file, parses them as from given in the example file format into a JSON object and returns it. 
# Code written by Krypto-Kiddo for Strawhats DAO.

def parseQnA(sourceFile):
    import json

    data = open(sourceFile,"r")
    dictData = {}

    for line in data:
        if line.startswith("Q)"):
            currQ = line.split("Q)")[-1].replace("\n","")
        elif line.startswith("A)"):
            currA = line.split("A)")[-1].replace("\n","")
            dictData.update({currQ:currA})
        else: pass

    dataJSON = json.dumps(dictData)

    return(dataJSON)
  
  # Driver code
  res = parseQnA("QnA.txt")
