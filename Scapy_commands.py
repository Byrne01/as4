
# coding: utf-8

# In[2]:

scapy


# In[4]:

#Importing all the scapy libraries
from scapy.all import *
import sys


# In[5]:

#displays all of the available protocols
ls()


# In[6]:

#lists all of the scapy command functions.
lsc()


# In[7]:

#the IP() function represents an IPv4 header. 
#When I add the show() function to the IP function it will display all of its fields.
IP().show()


# In[8]:

ip_address = ip()

ip_address.show()


# In[9]:

#ip must be uppercase IP
ip_address = IP()

ip_address.show()


# In[1]:

pkt = wlaN0()


# In[2]:

pkt = wlaN0()
pkt.show()


# In[34]:

from scapy.all import *
import sys


# In[35]:

pkt = wlaN0()
pkt.show()


# In[36]:

pkt = wlan0()
pkt.show()


# In[37]:

#Building a packet
a = IP(ttl=10)


# In[7]:

a


# In[38]:

a.src


# In[39]:

a.dst="192.168.1.252"


# In[40]:

a


# In[41]:

a.src


# In[42]:

del(a.ttl)


# In[43]:

a


# In[44]:

#Stacking layers
IP()


# In[45]:

IP()/TCP()


# In[46]:

Ether()/IP()/TCP()


# In[47]:

IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"


# In[48]:

Ether()/IP()/IP()/UDP()


# In[49]:

#Breaking down packets
str(IP())


# In[50]:

IP(_)


# In[51]:

a=Ether()/IP(dst="www.reddit.com")/TCP()/"GET /index.html HTTP/1.0 \n\n"


# In[52]:

hexdump(a)


# In[53]:

#manipulating IP PROTOCOL IPV4 header
ip=IP(src="172.29.189.138")


# In[54]:

ip.dst="192.168.1.5"


# In[26]:

ip


# In[55]:

ip().show()


# In[56]:

IP().show()


# In[58]:

ip


# In[59]:

#ADDING LAYER FOUR TCP PROTOCOL
ip/TCP()


# In[60]:

#ADDING MORE DETAILED SPECIFICATIONS
tcp=TCP(sport=1025, dport=80)


# In[61]:

(tcp/ip).show()


# In[62]:

send(ip/tcp)


# In[76]:

send(i/p)


# In[66]:

#Framing ICMP Packet
#http://troubleshoot4opensource.blogspot.ie/2015/07/frame-icmp-packets-using-scapy.html
i = IP()


# In[67]:

i.show()


# In[68]:

#setting parameters for above packet
i.dst="google.com"


# In[69]:

i.src="172.29.189.138"


# In[70]:

i.show()


# In[71]:

p=ICMP()


# In[72]:

p.show()


# In[73]:

#putting it all together to send a packet
#method1
send(i/p)


# In[74]:

#method 2
#using the send and receive function sr()

sr(i/p)


# In[77]:

send(IP(dst="1.2.3.4")/ICMP())


# In[78]:

from scapy.all import *


# In[79]:

send(IP(dst="1.2.3.4")/ICMP())


# In[ ]:



