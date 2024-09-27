# Модуль 2: Базы данных и SQL


В этом модуле знакомимся с SQL. Создание БД, подключение, загрузка, трансформация и прочие манёвры подобия ETL.

---

### Создание БД в PostgreSQL

Поскольку Postgres и DBeaver у меня уже были установлены, я просто зашёл в DBeaver и создал БД Superstore.

---

### Извлечение данных из xls в БД

В силу ограниченных, но всё же знаний, я принялся извлекать данные из таблиц Excel через Pandas и psycopg.


- [Что из этой идеи получилось](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/xls_to_sql.py)
- [Таблица Orders](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/orders.sql)
- [Таблица People](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/people.sql)
- [Таблица Returns](https://github.com/siochy/data-learn/blob/main/DE-101/Module2/returns.sql)

---

### Модели данных (Трансформация)

Я решил воспользовать инструментом sqldbm. Через него я построил Концептуальную и Физическую модели. Логическую же я построил отдельно в ***


Получились такие таблицы.

<img src='' alt='Концептуальная'>

<img src='' alt='Логическая'>

<img src='' alt='Физическая'>


Далее реализовал модели в БД, перетащив данные из таблиц.

---

### Загрузка в облачную БД


---

### Дашборды

