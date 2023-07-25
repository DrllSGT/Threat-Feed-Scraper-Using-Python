# ![My Skills](https://skillicons.dev/icons?i=python,vscode,git,github) 
# Threat-Feed-Scraper-Using-Python
A simple Python script that web scrapes a threat feed using BeautifulSoup

This script fetches the content from the abuse.ch DGA feed, parses it using BeautifulSoup to find the table, and then extracts the domain/URL indicators from each row.

The key steps are:

- Fetch page content using requests
- Parse HTML using BeautifulSoup
- Find relevant data table
- Iterate through rows
- Use text and attributes to extract indicators

You can extend this to extract other attributes like IP addresses, ASN, dates etc. And integrate it into your threat intelligence processing pipeline.
