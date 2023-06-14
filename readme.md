# Intro

This is a simple Web Scraping program inspired by PitoneProgrammatore's Youtube video: Web Scraping ITA - Tutorial Beautiful Soup Python. The idea is to scrape all the latest links of Nintendo Switch ads that appear on Italian secondhand website subito.it for Rome, Italy.

# Nintendo Switch Links Scraper

This program scrapes the links of Nintendo Switch ads from the page https://www.subito.it/annunci-lazio/vendita/usato/roma/roma/?q=nintendo%20switch and stores them in a text file called switch_links.txt. It also opens the new links in the browser automatically, except for the first time the program runs.

## How it works

- The program uses the requests and bs4 modules to fetch and parse the HTML of the website.
- It finds the div element with the class name "ListingContainer_col**1TZpb ListingContainer_items**3lMdo col items" and extracts all the a elements inside it.
- It filters out the links that do not start with https://www.subito.it/.
- It reads the previous links from the switch_links.txt file if it exists, otherwise creates an empty set.
- It compares the current links with the previous links and creates two lists: new_links and old_links.
- It writes the updated lists to the switch_links.txt file, with new_links first and old_links second.
- It checks if there are any new links. If there are, it opens them in the browser automatically, unless it is the first time the program runs. If there are no new links, it prints the message "No new links...".

## Requirements

- Python 3
- requests
- bs4
- webbrowser

## Usage

- Run the program as `python WebScrapingSwitch.py`
- The program will print the current links and store them in switch_links.txt
- The program will also open the new links in the browser automatically, except for the first time
