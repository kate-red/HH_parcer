import requests
import time
import os


class HHResumeDownloader:
    """Класс предназначен для скачевания страниц резюме, при помощи списка уникальных ссылок на резюме"""
    def __init__(self, page_url: str, data_path: str, number: int, timeout=10):
        self.page_url = page_url
        self.headers = {'User-Agent':
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.timeout = timeout
        self.data_path = data_path
        self.number = number
        self.proxy = {'http': 'http://161.202.226.195:8123'}

    def check_if_exists(self, resume_id: str):
        """Функция проверяет, была ли уже скаченна данная странца"""
        return os.path.exists(os.path.join(self.data_path, f'resume_page_{resume_id}.html'))

    def get_page_url(self, resume_id: str):
        """Склеивает темплейт ссылки на резюме и уникальный номер страницы"""
        return self.page_url.format(resume_id)

    def download_pages(self):
        """Запускает процесс скачивания страниц"""
        with open('id_list.txt', 'r') as id_list:
            rep = 0
            for resume_id in id_list:
                resume_id = resume_id.strip()
                if self.check_if_exists(resume_id):
                    print(f"File {'resume_page_{0}.html'.format(resume_id)} already exists. Skip")
                    continue
                print(f"Start downloading {resume_id} page")
                page_url = self.get_page_url(resume_id)
                print(f"Downloaded {resume_id} page")
                page = self.download_page(page_url)
                self.save_page(page, resume_id)
                print(f"Saved {resume_id} page")
                print("*" * 20)
                time.sleep(self.timeout)
                rep += 1
                if self.number == rep:
                    break

    def download_page(self, url: str):
        """Скачивание страницы"""
        page = requests.get(url, headers=self.headers, proxies=self.proxy)
        return page

    def save_page(self, page, resume_id: str):
        """Сохранение страницы в папку"""
        page_file_name = os.path.join(self.data_path, 'resume_page_{0}.html'.format(resume_id))
        with open(page_file_name, 'w') as resume_request:
            resume_request.write(page.text)


if __name__ == "__main__":
    hh_resume_downloader = HHResumeDownloader("https://hh.ru/resume/{0}", "saved_resumes/", 1520, timeout=5)
    hh_resume_downloader.download_pages()
