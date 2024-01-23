fh = open('Practical-2.txt','w')
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
fh.write('Area Of Rectangle: '+str(area)+'\n')
fh.write('Perimeter Of Rectangle: '+str(perimeter)+'\n')
fh.close()
