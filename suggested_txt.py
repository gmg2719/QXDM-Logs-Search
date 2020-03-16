import re
file_txt = open('QXDM.txt', 'r')

date = input("Please enter date of your log in 'YYYY Mon' format e.g. 2020 Feb: ")
print('Preparing for you a list of suggested messages for your next input, enjoy!')
suggest_Search = []
for line in file_txt:
    if date in line:
        line = re.sub('.*0x.*  ', '', line)
        nrs = ('Re$$$$$$', 'Diag$$$$$$', 'An$$$$$$$$', 'Dis$$$$$$$', 'E$$$$ Re$$$$ Con$$$$', 'S$$ Event M$$$', 'Times$$$$', 'Re$$$$$', 'EVENT_$$$')
        if not any(words in line for words in nrs):
            if line not in suggest_Search:
                suggest_Search.append(line)
for entry in suggest_Search:
    print(entry)
