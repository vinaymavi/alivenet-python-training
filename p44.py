file1 = open("./deepak.txt",'r')
file2 = open("./deepak1.txt",'w')
vowels = ['Deepak']
file_content = file1.read()
file_content_list = file_content.split(" ")
print file_content_list
for word in file_content_list:
    if word in vowels:
        file2.write(word.upper()+" ")
    else:
        file2.write(word+" ")

file1.close()
file2.close()