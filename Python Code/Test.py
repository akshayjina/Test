#Hello World
#Test Python

x = 'global x'
z = 1
def test(z):
 x = 'local x'
 print(x)

test(1)
print(z, x)
