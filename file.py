__author__ = 'Imran Khan'
File = open('student.txt')
#print(File.closed)
#print(File.mode)
#print(File.name)
#print(File.read())
#print(File.readline())
line_read = File.readline()
line_read = int(line_read)
#for i  in range(0,line_read):
    #print(File.readline())
output = list()
File1 = open('out.txt', mode= 'w')
for line in File:
    output.append(line.upper())
for idx , val  in enumerate(output):
    File1.write('Case '+str(idx+1)+ ': '+val)
#for i  in range(0, len(output)):
    #File1.write('Case '+str(i+1)+ ': '+output[i])
    #print('Case '+str(i+1)+ ': '+output[i])

#for line in File:
    #print(line.upper())
File.close()
File1.close()
