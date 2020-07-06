# HH_parcer
### Скачивание открытых резюме с сайта hh.ru


1. Первое, что нужно сделать, чтобы скачать резюме - это загрузить страницы, содержащие ссылки на резюме. Для этого нужно зайти на сайт hh.ru, выставить необходимые условия поиска резюме (например, указать название должности или другие параметры). Затем, необходимо скопировать ссылку поменять ссылку в HH_html_pages_Dowloader.py на необходимую вам. 
В данном случае использовалась ссылка, где резюме были отранжированы по называнию должности (Sales manager) и по обязательному наличию ожидаемой зрабаотной платы. Класс HHDowloader в HH_html_pages_Downloader.py автоматически скачивает нужное количество страниц в указанном диапозоне и сохранет их в директорию data. Если фаил с данным именем уже был загружен, программа не скачивает его повторно.
***
2. Второй этап - извлечение ссылок на резюме из скаченных в предыдущем шаге html-страниц. Функция write_links в id_list_writter.py осуществляет поиск уникальных кодов страниц и сохраняет их в id_list.txt.
***
3. Далее, необходимо скачать страницы с резюме. Класс HHResumeDownloader в HH_resume_downloader.py создан как раз для этой цели - он инициализирует скачивание htmp-страниц с резюме спри помощи класса HHResumeDownloader и функции download_pages (HH_resume_downloader.py), которая итерируется по ранее составленному спску ключей (id_list.txt), подставляя id в ссылку "https://hh.ru/resume/{0}", скачивает страницу и сохраняет ее в директорию "saved_resumes/".
***
4. Теперь предстоит решить задачу парсинга резюме. В HH_parser.py реализован класс Resume, извлекающий информацию из скаченных html-страниц, а именно:
- resume_id - уникальная ссылка на резюме
- resume_title - название должности
- city - город проживания
- age - возраст соискателя (int)
- gender - пол соискателя
- area - сфера деятельности
- desired_wage - желаемый уровень заработной платы (int, автоматически переводитя в доллары)
- work_exp - опыт работы в формате float(число до запятой - года, после - месяца), без уточняющего списка
- education - уровень образования (без вуза)
- language_prof - dict, где ключ - язык, значение - уровень владения языком
- skills - list с навыками

Данная информация из каждого резюме сохраняется в отдельный .json фаил в директории 'new_json_resumes/' с уникальным номером резюме в имени. Есл фаил уже был загружен, он автоматически пропускается и не скачивается снова.
***
5. Датасет практически готов! Осталось только "склеить" отдельные json-файлы в один датасет. Для этого используется функция get_dataset в json_dataset_loader.py, которая возвращает словарь со всеми резюме, который нужно сконвертировать обратно в json-формат и записать в фаил.
***
6. Радуемся жизни - теперь у нас есть готовый датасет с небольшими резюме, содержащими основную информацию о соискателях по конкретной должности (без персональных данных) 
