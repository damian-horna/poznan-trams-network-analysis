import requests
from bs4 import BeautifulSoup

BASE_HREF = "https://www.ztm.poznan.pl"


def save_stop_names(filename, stop_names):
    with open(filename, "w") as f:
        for stop_name in stop_names:
            f.write(stop_name + "\n")


def extract_stop_names(li_stops):
    result = []
    for li in li_stops:
        stop_page = requests.get(f"{BASE_HREF}{li.contents[1].attrs['href']}")
        stop_page_soup = BeautifulSoup(stop_page.content, 'html.parser')
        stop_details_name_str = stop_page_soup.find('div', class_='stop-details__info').find('h2').text[12:]
        print(stop_details_name_str)
        result.append(stop_details_name_str)
    return result


if __name__ == '__main__':
    for tram_no in range(7, 19):
        print(f"Scraping stops for tram: {tram_no}")
        URL = f'https://www.ztm.poznan.pl/pl/rozklad-jazdy/{tram_no}'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        div_there = soup.findAll('div', class_='line-direction')[0]
        div_back = soup.findAll('div', class_='line-direction')[1]

        li_stops_there = div_there.find('ul').findAll('li', class_='line-stop--main')
        li_stops_back = div_back.find('ul').findAll('li', class_='line-stop--main')

        # Extract stop names there and back
        stops_there_names = extract_stop_names(li_stops_there)
        stops_back_names = extract_stop_names(li_stops_back)

        # Save stop names to a file
        save_stop_names(f"data/{tram_no}there", stops_there_names)
        save_stop_names(f"data/{tram_no}back", stops_back_names)


        print("Done")