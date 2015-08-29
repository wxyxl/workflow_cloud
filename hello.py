import socket

s=raw_input("Input your age:")
if s=="":
   raise Exception("Input must no be empty.")

try:
    i=int(s);
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unknown exception!"
else:
    print "Your are %d" %i, " years old"
finally:
    print "Goodbye!"

hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)

print hostname
print hostip

#get local broadcast address
list = hostip.split('.')
print list
list[-1] = '255'
print list
broadcast = ".".join(list)

#broadcast = "255.255.255.255"

#print local information
print "host name: ", hostname
print "host ip address: ", hostip
print "broadcast address: ", broadcast

print "beijing tianjingshijie jingbiaosai"
