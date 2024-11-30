# Random hex codes for colors:
# white: #D5D8B5
# purple: #53354A
# salmon: #8E4D4D
# light green: #809A6F
# dark green: #1C3B29

# PART ZERO: open the files and write to them
input = open("data.txt", "r").read()
output = open("index.html", "w")

# PART ONE: use the html parser to scrape a site and store data in array
trash = {".a,.b{fill:#c2c2c2;}.b{opacity:0;}", "\n", "", "\t", " ", " \n ", " \n  \n", "single-arrow-square"}
courses = [];
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if (data not in trash):
            # course number
            if ('CSE' in data[0:8]):
                courses.append(data[5:20])
            else:
                if (len(data.strip()) != 0 and data[0:1] != '('):
                    courses.append(data)
parser = MyHTMLParser()
parser.feed(input)

# PART TWO: convert array into list of tuples
numbers = []
names = []
descrips = ['']
units = []

name = False 
descrip = False
unit = False

for line in courses:

    # course number
    if ('CSE' in line[0:8]):
        numbers.append(line)
        name = True
    # course name
    elif (name):
        names.append(line)
        name = False

    # course description
    if ('Description' in line):
        descrip = True
    elif(descrip and 'Units' not in line):
        line = line.replace('\n', ' ')
        descrips[-1] += line

    # number of units
    if ('Units' in line):
        descrip = False
        unit = True
        descrips.append('')
    elif(unit):
        units.append(line[1:2])
        unit = False
descrips.pop() # extra element in descriptions due to the  way the code is written

# PART THREE: loop through each tuple and write html
courses.clear()
courses = zip(numbers, names, descrips, units)
#print(tuple(courses))

css_file = "format.css"
output.write('<!DOCTYPE html>\n<html>\n<head>\n\t<link rel="stylesheet" href="format.css">\n')
output.write('\t<title>Harshi Kosaraju</title>\n')
output.write('</head>\n<body>\n')
#output.write('\t<ul>\n\t\t<li><a href="https://harshikosaraju.github.io/">Home</a></li>')
#output.write('\n\t\t<li><a href=pages/about.html>1 Unit</a></li>')
#output.write('\n\t\t<li><a href=pages/cse2231.html>2 Units</a></li>')
#output.write('\n\t</ul>')
output.write('\n\t<main>')
output.write('\n\t\t<h1>Ohio State CSE Courses: Autumn 2022</h1>\n')

for course in courses:
    output.write('\t\t<div id="course">\n')

    output.write('\t\t\t<h2>')
    output.write(course[0])
    output.write('</h2>\n')

    output.write('\t\t\t<h3>')
    output.write(course[1])
    output.write('</h3>\n')

    output.write('\t\t\t<p>Description: ')
    output.write(course[2])
    output.write('</p>\n')

    output.write('\t\t\t<p>Units: ')
    output.write(course[3])
    output.write('</p>\n')

    output.write('\t\t</div>\n')

# PART FOUR: TYING UP LOSE ENDS
output.write('\t</main>\n')

#output.write('\t<aside>\n')
#output.write('\t\t<p>')
#output.write('hello')
#output.write('</p>')
#output.write('\t</aside>\n')

output.write('</body>\n</html>\n') # footer of output file
output.close() # close output file

  
