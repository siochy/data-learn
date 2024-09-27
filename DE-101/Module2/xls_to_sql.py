import pandas as pd
import psycopg as pg
import os

DB = os.environ['DB']  # "dbname=Superstore user=postgres password=YOURPASSWORD host=localhost port=5432"

df_orders = pd.read_excel('Sample - Superstore.xls', sheet_name='Orders')
df_people = pd.read_excel('Sample - Superstore.xls', sheet_name='People')
df_returns = pd.read_excel('Sample - Superstore.xls', sheet_name='Returns')

df_orders.to_csv('/tmp/tb_orders.csv', index=False)
df_people.to_csv('/tmp/tb_people.csv', index=False)
df_returns.to_csv('/tmp/tb_returns.csv', index=False)

with pg.connect(DB) as cn:
    curs = cn.cursor()
    sql_query = '''
        create table if not exists Orders(
        row_id int,
        order_id text,
        order_date text,
        ship_date text,
        ship_mode text,
        customer_id text,
        customer_name text,
        segment text,
        country text,
        city text,
        state text,
        postal_code numeric,
        region text,
        product_id text,
        category text,
        sub_cutegory text,
        product_name text,
        sales numeric,
        quantity int,
        discount numeric,
        profit numeric
        );
    '''
    curs.execute(sql_query)
    
    sql_query = '''
        create table if not exists People(
        person text,
        region text
        );
    '''
    curs.execute(sql_query)

    sql_query = '''
        create table if not exists Returns(
        returned text,
        order_id text
        );
    '''
    curs.execute(sql_query)
    
    sql_query = '''
        copy Orders
        from '/tmp/tb_orders.csv'
        delimiter ','
        csv header
    '''
    curs.execute(sql_query)

    sql_query = '''
        copy People
        from '/tmp/tb_people.csv'
        delimiter ','
        csv header
    '''
    curs.execute(sql_query)

    sql_query = '''
        copy Returns
        from '/tmp/tb_returns.csv'
        delimiter ','
        csv header
    '''
    curs.execute(sql_query)
