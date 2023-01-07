# CoreyMS-get-data


## Description:

This is a web scraping script that extracts information from the [CoreyMS website](https://coreyms.com) and stores it in an Excel file. The script uses the requests library to send a GET request to the website, and the BeautifulSoup library to parse the HTML response and extract the desired information. The script also uses the pandas library to clean the extracted data and create a DataFrame.

## How to use:

You can run the script by calling the `main()` function. The script will scrape the [CoreyMS website](https://coreyms.com), clean the extracted data, and store it in an Excel file named `coreyMS_link.xlsx`.

## Dependencies:

* requests
* beautifulsoup4
* pandas
