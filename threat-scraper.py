import requests
from datetime import datetime

# URL of the threat feed
url = 'https://urlhaus.abuse.ch/downloads/text/'

# Fetch the feed content
response = requests.get(url)
feed_content = response.text

# Split the content by newline to get each URL
malicious_urls = feed_content.split('\n')

# Filter out empty lines
malicious_urls = [url.strip() for url in malicious_urls if url.strip()]

# Get the current timestamp
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Print the header
print(f'URLhaus Malicious URLs Feed - {current_time}')
print('=' * 50)

# Iterate through the malicious URLs and print them
for url in malicious_urls:
    print(url)

print('=' * 50)
print(f'Total Malicious URLs: {len(malicious_urls)}')

# Export the malicious URLs to a file in a format readable by security tools
with open('malicious_urls.txt', 'w') as file:
    file.write('\n'.join(malicious_urls))
