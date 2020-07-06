import re
from bs4 import BeautifulSoup


def write_links(page: str, pattern: str, start: int, end: int):
    """Осуществляет поиск ссылок на резюме в скаченных страницах"""
    for i in range(start, end + 1):
        with open(page.format(i), 'r') as resume_request, open('id_list.txt', 'a') as id_list:
            soup = BeautifulSoup(resume_request, features="lxml")
            id_lst = soup.find_all('a', {'class': "resume-search-item__name"})
            for raw_id in id_lst:
                id_list.write(re.search(pattern, raw_id['href']).group(1))
                id_list.write('\n')


write_links('data/resume_page_{0}.html', r'resume\/(.+)\?', 0, 75)
