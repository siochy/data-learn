# Модуль 2: Базы данных и SQL


В этом модуле знакомимся с SQL. Создание БД, подключение, загрузка, трансформация и прочие манёвры подобия ETL.

---

### Создание БД в PostgreSQL

Поскольку Postgres и DBeaver у меня уже были установлены, я просто зашёл в DBeaver и создал БД Superstore.

---

### Извлечение данных из xls в БД

В силу ограниченных, но всё же знаний я принялся извлекать данные из таблиц Excel через Pandas и psycopg.


- [Что из этой идеи получилось](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/xls_to_sql.py)
- [Таблица Orders](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/stg_orders.sql)
- [Таблица People](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/stg_people.sql)
- [Таблица Returns](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/stg_returns.sql)

---

### Модели данных (Трансформация)

Я решил воспользоваться инструментом sqldbm. Через него я построил Концептуальную и Физическую модели. Логическую же я построил отдельно в draw.io


Получились такие таблицы.

<img src='https://raw.githubusercontent.com/siochy/data-learn/refs/heads/main/DE-101/Module2/conceptual.png' alt='Концептуальная'>

<img src='https://raw.githubusercontent.com/siochy/data-learn/refs/heads/main/DE-101/Module2/logical.png' alt='Логическая'>

<img src='https://raw.githubusercontent.com/siochy/data-learn/refs/heads/main/DE-101/Module2/physical_fix.png' alt='Физическая'>


Далее реализовал модели в БД, перетащив данные из таблиц.

[Transform](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/stg_to_bw.sql)

---

### Загрузка в облачную БД

Ранее я уже пользовался облаком на Amvera, поэтому снова решил разместить там БД. Тем более недавно там появилась возможность подлючаться через сервисы извне.

<img src='https://raw.githubusercontent.com/siochy/data-learn/refs/heads/main/DE-101/Module2/db_pgadmin.png' alt='БД'>


---

### Дашборды

Пришлось хорошенько покопать в поисках рабочего BI-сервиса. В итоге, меня выручил Klip, в который у меня всё же получилось загрузить данные из облачной БД, и я принялся делать дашборд.

<img src='https://raw.githubusercontent.com/siochy/data-learn/refs/heads/main/DE-101/Module2/db_klip.png' alt='Klip'>

Функционал Klipfolio меня не впечатлил, но на безрыбье тоже инструмент.

<img src='https://raw.githubusercontent.com/siochy/data-learn/refs/heads/main/DE-101/Module2/dashboard_klipfolio.png' alt='Dashboard'>

---

Спасибо за внимание!

