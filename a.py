import csv
import quickstart

values = quickstart.main()
#print(values)
with open('names.csv', 'w') as csvfile:
    fieldnames = values[0]
    #print(fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for x in range(1,len(values)):
        #print(values[x][0])
        writer.writerow({'Timestamp' : values[x][0], 'Email Address':values[x][1], 'Name': values[x][2], 'Date for Today\'s class': values[x][3], 'Did you attend the class?' : values[x][4], 'Did you complete the assignments given.' : values[x][5], 'Comments on the assigment given' : values[x][6], 'Hackerrank Algorithm Score': values[x][7], 'Hackerrank Python Score': values[x][8], 'Hackerrank Data Structure Score' : values[x][9], 'Project Euler - Number of problems solved': values[x][10], 'Rosalind Info - Number of problems solved': values[x][11], 'Describe how the Today\'s class was' : values[x][12], 'Any suggestions or comments' : values[x][13]})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})