#file=open('Demo_read_write')
#print(file.read(2))
#print(file.readline())
#obj=file.readline()
#while obj!='':
#    print(obj)
#    obj = file.readline()
#for line in file.readlines():
#    print(line)
#file.close()
with open('Demo_read_write','r') as reader:
    content=reader.readlines()
    reversed(content)
    with open('Demo_read_write','w') as writer:
        for line in reversed(content):
            writer.write(line)