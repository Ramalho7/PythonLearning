import webbrowser
import requests
import sys
import bs4

"""Código não funciona mais devido ao pypi usar proteção anti-bot
"""

print('Searching...')  # Display text while downloading the search results page.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()
with open('debug_pypi.html', 'w', encoding='utf-8') as f:
    f.write(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')
print(f"Pacotes encontrados: {len(link_elems)}")
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)