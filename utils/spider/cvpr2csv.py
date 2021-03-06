import requests
from bs4 import BeautifulSoup
import re


def main():
    root_link = 'http://openaccess.thecvf.com/'
    conference = 'ICCV'  # conference name
    year = 2019  # conference year
    filename = conference + str(year) + '.csv'
    with open(filename, 'w') as f:
        f.write('id, title, authors, conference, year, download_link, abstract\n')
    from_page(root_link=root_link, conference=conference, year=year, filename=filename)


def from_page(root_link, conference, year, filename):
    url = root_link + conference + str(year) + '.py'
    r0 = requests.get(url)
    if r0.status_code == 200:  # get all dates from r0
        datelist = re.findall(r'\d\d\d\d-\d\d-\d\d', r0.text)
        dateset = set(datelist)  # delete repeated dates
        dates = list(dateset)
        dates.sort()
    else:
        print("ERRORS occur!")
    id = 1
    for date in dates:
        r = requests.get(url, params={'day': date})
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "lxml")
            for ptitle in soup.find_all('dt', class_='ptitle'):
                title = ptitle.a.string
                link = ptitle.a['href']
                link = root_link + link
                r1 = requests.get(link)
                soup1 = BeautifulSoup(r1.text, "html5lib")
                ab = soup1.find('div', id='abstract')
                if ab.string:
                    abstract = ab.string
                elif ab.nn:
                    abstract = ab.contents[0] + ab.nn.string
                abstract = abstract.replace('\n', '')
                abstract = abstract.replace('"', '""')
                link = link.replace('html/', 'papers/')
                link = link.replace('.html', '.pdf')
                authors = []
                dd = ptitle.next_sibling.next_sibling
                for form in dd.find_all('form'):
                    authors.append(form.a.string)
                for author in authors:
                    author = author.replace('"', '""')
                write_row(
                    filename, id, conference, year, authors, title, link, abstract
                )
                id += 1
            print('Successfully completed.')
        else:
            print("ERRORS occur!")


def write_row(csv_path, id, conference, year, authors, title, link, abstract):
    '''
    write data into csv
    '''
    with open(
        csv_path, 'a', encoding="utf-8"
    ) as data:  # id, title, authors, conference, year, download_link, abstract
        data.write(
            ','.join(
                [
                    str(id),
                    '"' + title + '"',
                    '"' + ','.join(authors) + '"',
                    conference,
                    str(year),
                    link,
                    '"' + abstract + '"',
                ]
            )
            + '\n'
        )
    print("Completed Writing: {}: {:30}".format(id, title))


if __name__ == "__main__":
    main()
