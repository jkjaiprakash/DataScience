##import re
##var='india  is my country'
##var1=re.match("india",var)
##print(var1)

##import re
##var='india  is my country'
##var1=re.match("india",var)
##print(var1.group())

##import re
##var='india  is my country'
##var1=re.match("INDIA",var)
##print(var1)

##import re
##var='india  is my country'
##var1=re.match("INDIA",var,re.I)         # re.I  is the default syntax for ignoring upper and lower case matching 
##print(var1.group())


##import re
##var='india  is my country'    # Error will pop bcause  it matches with exactly 
##var1=re.match("my",var)
##print(var1.group())

##import re
##var='india is my country'
##var1=re.match("india is my",var)
##print(var1.group())

##import re
##var='india is my country'
##var1=re.search("my",var)
##print(var1.group())

##import re
##var="<htmml><head><html>"
##var1=re.match("<.*>",var)
##print(var1.group())

##import re
##var="<html><head><html>"
##var1=re.match("<.*?>",var)
##print(var1.group())

##import re
##var="india is smarter than china"
##var1=re.match(".* is .*",var)
##print(var1.group())

##import re
##var="india is smarter than china"
##var1=re.match("(.*) is (.*)",var)
##print(var1.group(1))
##print(var1.group(2))

##import re
##var="india is smarter than china"
##var1=re.match("(.*) is (.*) (.*)",var)
##print(var1.group(1))
##print(var1.group(2))
##print(var1.group(3))

##import re
##var="india is smarter than china"
##var1=re.match("(.*) is (.*?) (.*)",var)
##print(var1.group(1))
##print(var1.group(2))
##print(var1.group(3))

##import re
##var="india is smarter than china"
##var1=re.match("(.*) is (.*?) (.*)",var)
##print(var1.group(1))
##print(var1.group(2))
##print(var1.group(3))


##import re
##var="5789"
##var1=re.sub("5","10",var)           ## It substitues 5 to 10 
##print(var1)
##var2=re.sub("10","5",var1)
##print(var2)

##import re
##var=re.compile("[a-z]")
##var1=var.match("india")
##print(var1.group())

##import re
##var=re.compile("[a-z]")
##var1=var.findall("india")
##print(var1)

##import re
##var=re.compile("[a-z]+")
##var1=var.findall("india")
##print(var1)

##import re
##var=re.compile("[a-z]*")
##var1=var.findall("india")
##print(var1)

##import re
##var=re.compile("[0-9]")
##var1=var.findall("7865")
##print(var1)

##import re
##var=re.compile("[0-9]+")
##var1=var.findall("7865")
##print(var1)

##import re
##var=re.compile("[0-9]*")
##var1=var.findall("7865")
##print(var1)

##import re
##var=re.compile("[A-Z]")
##var1=var.findall("india")
##print(var1)
