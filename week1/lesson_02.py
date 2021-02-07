# regular expressions
# split on spaces to get individual word tokens
import re
text = "hello #America"
text1 = "hello #America"
a = [w for w in text if w.startswith("#")]

pattern ="@[a-zA-Z0-9_]+"

b = [w for w in text1 if re.search("@[a-zA-Z0-9_]+", w)]
