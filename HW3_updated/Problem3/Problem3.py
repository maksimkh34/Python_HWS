text = input("Enter string: ")
result = ""
indexes = []

for i in range(len(text)):
    if(text[i]=='o'): indexes.append(i)

if (len(indexes)==0):
    print("No 'o' letters found.")
    exit()

if (len(indexes)==1):
    print("Letter 'o' is repeated only one time.")
    exit()

min = indexes[0]
max = indexes[0]
for i in range(len(indexes)):
    if  (indexes[i]<min): min = indexes[i]
    if (indexes[i]>=max): max = indexes[i]

for i in range(min + 1, max):
    result += text[i]

print(result)