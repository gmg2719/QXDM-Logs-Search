import suggested_txt
from suggested_txt import date

file_txt = open('QXDM.txt', 'r')


suggested_txt

def find_line_in_full_txt(element):
    try:
        index_line = line.index(element)
        return index_line
    except ValueError:
        return None


str_input = input("Enter the text to search from the QXDM log :\n")
print('Searching ...')
l = 0
dictSinglePhrase = {}
dictRestPhrase = {}
for line in file_txt:
    l = l + 1
    if find_line_in_full_txt(line) is not None:
        if str_input in line:
            dictSinglePhrase[l] = line
        else:
            dictRestPhrase[l] = line

if len(dictSinglePhrase.keys()) > 0:
    choice = 'y'
    search = input("\nWould you like to start browsing after the Msg line(s), resulted from this text search amongst " + str(sorted(dictSinglePhrase.keys())) + "\nEnter y for Yes or any other key to quit the program : ")
    while search == 'y':
        if choice == 'y':
            lineNumber = input("Choose the number amongst " + str(sorted(dictSinglePhrase.keys())) + ", you would like to start from : ")
            lineNumber = int(lineNumber)
            if lineNumber in dictSinglePhrase.keys():
                print("\nHere is the text of ", lineNumber, " : ", dictSinglePhrase[lineNumber])
                print("\nHere is further detail of the Msg \n")
                for i in range(lineNumber+1, lineNumber+30):
                    if date in dictRestPhrase[i]:
                        break
                    else:
                        print(dictRestPhrase[i])
            else:
                print("Sorry, the number must be amongst the search result above")
        choice = input("\nEnter y to choose another number amongst" + str(sorted(dictSinglePhrase.keys())))
        search = choice

