import bs4
import requests
import webbrowser
from pprint import pprint

MAIN_URL = "https://www.subito.it/annunci-lazio/vendita/usato/roma/roma/?q=nintendo%20switch"
FILE_NAME = "switch_links.txt"  # name of the file to store the results
LINK_PREFIX = "https://www.subito.it/"  # prefix of the relevant links

# initialize a variable to keep track of whether it is the first run or not
first_run = True

# read the previous links from the file if it exists, otherwise create an empty set
try:
    with open(FILE_NAME, "r") as f:
        prev_links = set(f.read().splitlines())
    # if the file exists, then it is not the first run
    first_run = False
except FileNotFoundError:
    prev_links = set()

# scrape the current links from the website
response = requests.get(MAIN_URL)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_annunci = soup.find('div', class_="ListingContainer_col__1TZpb ListingContainer_items__3lMdo col items")
if div_annunci:
    a_annunci = div_annunci.find_all('a')
    curr_links = []
    for a_annuncio in a_annunci:
        try:
            link_annuncio = a_annuncio.get('href')
            curr_links.append(link_annuncio)
        except Exception as e:
            print(f"Error: {e}")
    pprint(curr_links)
else:
    print("No div element found with the given class name.")

# filter out the links that do not start with LINK_PREFIX
curr_links = [link for link in curr_links if link.startswith(LINK_PREFIX)]

print(curr_links)

# compare the current links with the previous links and create two lists: new_links and old_links
curr_links = set(curr_links) # convert curr_links to a set
new_links = curr_links - prev_links # find the difference between curr_links and prev_links
old_links = curr_links & prev_links # find the intersection between curr_links and prev_links
new_links = list(new_links) # convert new_links back to a list
old_links = list(old_links) # convert old_links back to a list

# write the updated lists to the file, with new_lines first and old_lines second
with open(FILE_NAME, "w") as f:
    f.write("new_links:\n")
    f.writelines("\n".join(new_links))
    f.write("\n\nold_links:\n")
    f.writelines("\n".join(old_links))

print("The results have been stored in", FILE_NAME)

# if there are new links, open them directly in browser, else print a message
if len(new_links) > 0: # check if new_links is not empty
    # check if it is the first run or not
    if first_run: # if it is the first run
        print("This is the first run. The links will not be opened automatically.") # print a message
        first_run = False # set first_run to False for future runs
    else: # if it is not the first run
        for link in new_links: # iterate over new_links
            webbrowser.open(link) # open each link in a new tab
else: # if new_links is empty
    print("No new links...") # print a message

