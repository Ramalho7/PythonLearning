import requests, bs4
res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

with open('page.html', encoding='utf-8') as example_file:
    example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
    print(type(example_soup))