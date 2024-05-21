# ![My Skills](https://skillicons.dev/icons?i=python,vscode,git,github) 
# Threat Intel Scraper

This Python script scrapes the Abuse.ch URLhaus feed for malicious URLs and presents them in a human-readable format. Additionally, it exports the list of malicious URLs to a text file that can be consumed by popular security tools.

## Usage

1. Ensure that you have Python installed on your system.
2. Install the `requests` library by running `pip install requests` in your terminal or command prompt.
3. Download or copy the `threat_intel_scraper.py` script to your desired location.
4. Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:
5. The script will fetch the latest malicious URLs from the Abuse.ch URLhaus feed, display them in the terminal, and export them to a file named `malicious_urls.txt` in the same directory.

## Output

The script will generate the following output:

- A header with the current timestamp and a separator line.
- A list of malicious URLs fetched from the Abuse.ch URLhaus feed.
- A separator line and the total count of malicious URLs.
- A text file named `malicious_urls.txt` containing the list of malicious URLs, with each URL on a new line.

## Notes

- The script assumes that the Abuse.ch URLhaus feed URL is accessible and the content format remains consistent. If the feed source changes, you may need to modify the script accordingly.
- The `malicious_urls.txt` file can be easily imported or consumed by various security tools for further analysis or blocking purposes.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
