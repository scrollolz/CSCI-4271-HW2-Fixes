import os, datetime, os.path, re
inputline = input()
pattern = r"^[A-Za-z0-9]+$"
(_, username) = inputline.split('=')

# Fix for mistake #4: Pattern match input username until valid
while (not re.fullmatch(pattern, username)):
    inputline = input()
    (_, username) = inputline.split('=')

times = list(os.popen("last -1000 | grep " + username))
# Fix for Mistake #3: Input username matches an existing username in list  
if (len(times) > 0):
    if (not username == times[0].split(':')[0]):
        exit

of = os.getenv("OUTPUTFILE") # should the output go to a file?
# Fix for Mistake #2: Check if the of environment variable value is a valid path
if (of is not path):
    exit
counter = 0
ofname = of
if of is not None and os.path.exists(ofname):
    counter += 1
    ofname = "{}.{}".format(of, counter)
# Fix for Mistake #1: added error handling for opening ofname 
if of is not None:
    try:
        sys.stdout = open(ofname, "w")
    except FileNotFoundError:
        print("File Not Found!")
print("<HTML><BODY>\n")
print("<h4>Last up to 3 times for user " + username + "</h4>\n")
print("<table>\n")
for i in range(min(3,len(times))):
    print("<tr>")
    for s in times[i].split()[2:]:
        print("<td>{}</td>".format(s))
    print("</tr>\n")
if times == []:
    print("<!-- didn't find any at {} -->".format(datetime.datetime.now()))
print("</table>\n</BODY></HTML>\n")