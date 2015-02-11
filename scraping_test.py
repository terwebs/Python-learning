from urllib2 import urlopen
import re

my_address = "https://realpython.com/practice/aphrodite.html"
html_page = urlopen(my_address)

html_text = html_page.read()

start_tag = "<title>"
end_tag = "</title>"

start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

print html_text[start_index:end_index]


my_address2 = "https://realpython.com/practice/dionysus.html"
html_page2 = urlopen(my_address2)

html_text2 = html_page2.read()

for tag in ["Name: ", "Favorite Color: "]:
    start_tag = html_text2.find(tag) + len(tag)
    end_tag = html_text2[start_tag:].find("<")
    print html_text2[start_tag:start_tag+end_tag]

# Using Regular Expresions
# Set tags, ending patterns in new line or <
for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text2)
    # using strip to remove the string used
    print match_results.group().strip(" <\n")
    
    # Subtitute the tag with an empty string
    no_tag_result = re.sub(".*: ", "", match_results.group())
    print no_tag_result.strip(" <\n")


