# CoreyMS-get-data


## Description:

This is a web scraping script that extracts information from the [CoreyMS website](https://coreyms.com). It collects the following information for each post:

* Title
* Article link
* Abstract
* YouTube link (if available)

The collected information is then stored in a Pandas DataFrame and saved to an Excel file (`coreyMS_link.xlsx`).

## How to use:

You can run the script by calling the `main()` function. The script will scrape the [CoreyMS website](https://coreyms.com), clean the extracted data, and store it in an Excel file named `coreyMS_link.xlsx`.

## Dependencies:

* `requests`
* `beautifulsoup4`
* `pandas`
