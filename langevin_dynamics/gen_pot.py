# to geneate potential energy file
# a double well potential is used here
# y=c(b-a*(x - d)**2)**2

# parameters for potential energy function
a = 1
b = 2.25
c = 2
# range
n = 8001 # intended upper limit +1
# move lower limit to 0
d = (n-1)*0.001

output = open('potential.txt','w')
print('# Current potential equation is y = {}({}-{}x^2)^2\n# The boundary is [{},{}]'.format(c,b,a,0,2*d),file=output)
output.write('# index postion potential force\n')

for i in range(-n+1,n):
    x = 0.001*i + d
    y = c*(b-a*(x - d)**2)**2
    f = 4*a*c*(x - d)*(a*(x - d)**2-b)
#    f.write(i,x,y,f)
#    output.write(i,x,y,f)
    print('{:5d} {:7.3f} {:10.7f} {:11.7f}'.format(i+n,x,y,f),file=output)
#    print('{}'.format(i),'{}'.format(x),'{}'.format(y),'{}'.format(f),file=output)
#f.close()
