import requests
from bs4 import BeautifulSoup
from googlesearch import search

def google_search(query, num_results=10):
    return search(query, num_results=num_results)

def search_book_in_url(url, book_title):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    for link in links:
        if book_title.lower() in link.text.lower():
            return url + link['href']
    
    return None

def main():
    query = 'intitle:"index of" "Building Microservices with Go"'
    book_title = "Building Microservices with Go"
    
    print("Searching Google for open directories containing the book...")
    urls = google_search(query)
    
    for url in urls:
        print(f"Searching in {url}...")
        result = search_book_in_url(url, book_title)
        if result:
            print(f"Book found: {result}")
        else:
            print("Book not found in this directory.")

if __name__ == '__main__':
    main()

