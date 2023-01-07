
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_info(url):
    """Extracts information from the given URL and returns a list of lists.
    Each inner list contains the text and href of all a elements within an article element,
    followed by the text of all div elements within the same article element,
    followed by the src of all iframe elements within the same article element.
    
    Args:
        url (str): The URL to scrape information from.
    
    Returns:
        list: A list of lists containing the extracted information.
    """
    # Send a GET request to the URL and parse the HTML response
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    
    # Initialize the final list and a temporary list
    final_list, temp_list = [], []
    

    
    # Iterate over each article element
    for article in soup.find_all('article', class_='post'):
        # Extract the href and text of all a elements or b elements within the article
        a_elements = [a.text  for a in article.find_all('a', class_='entry-title-link')]
        b_elements = [a['href'] for a in article.find_all('a', class_='entry-title-link')]        
        # Extract the text of all div elements within the article
        div_elements = [div.text.strip() for div in article.find_all('div', class_='entry-content')]
        # Extract the src of all iframe elements within the article
        iframe_elements = [iframe['src'] for iframe in article.find_all('iframe')]  
        date_post = [i.text for i in article.find_all('time', class_='entry-time')]
        # Combine the information from the a, div, and iframe elements into a single list
        temp_list = a_elements + b_elements + div_elements + date_post + iframe_elements 
        # Add the combined list to the final list
        final_list.append(temp_list)   
  
    return final_list


def info_clean(list_data):
    """Clean the extracted information and create a DataFrame"""
    # Create a DataFrame from the list data
    df = pd.DataFrame(list_data, columns=(['Title', 'Article link', 'Abstract', 'Date of post', 'YouTube link', '?']))
    
    # Combine elements from the 'YouTube link' and '?' columns into a single list for selected rows
    df.loc[df['?'].notna(), 'YouTube link'] = df[df['?'].notna()].apply(lambda row: [row['YouTube link'], row['?']], axis=1)
    
    # Drop the '?' column
    df.drop(columns='?', inplace=True)
    
    return df

def number_of_pages():
    url = 'https://coreyms.com'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    numbers = [i.text for i in soup.find_all('div', class_="archive-pagination pagination")]
    numbers = numbers[0].split('\n')
    numbers = [int(x) for x in numbers if x.isdigit()]
    max_number = max(numbers)
    
    return max_number

def main():
    url = 'https://coreyms.com/page/'
    final = []
    for i in range(1,number_of_pages()+1):
        info = extract_info(f"{url}{i}")
        final.extend(info)
    df_final = info_clean(final)
    
    df_final.to_excel('coreyMS_link.xlsx')
    
    df_final
    
    return df_final

if __name__ == '__main__':
    main()
    

