import sqlite3
from scripts import webscrapers as wb


conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()

c.execute("""SELECT url_amazon, url_flipkart, url_bigbasket
             FROM products_product""")
database_urls = c.fetchall()



for rows in database_urls:
    for idx,url in enumerate(rows):
        if idx==0:
            amazon_price = wb.amazon_scrape(url)
            c.execute("""UPDATE products_product
                         SET price_amazon=?
                         WHERE url_amazon=?""", (amazon_price, url))

        elif idx==1:
            flipkart_price = wb.flipkart_scrape(url)
            c.execute("""UPDATE products_product
                         SET price_flipkart = ?
                         WHERE url_flipkart=?""", (flipkart_price, url))

        elif idx==2:
            bigbasket_price = wb.bigbasket_scrape(url)
            c.execute("""UPDATE products_product
                         SET price_bigbasket=?
                         WHERE url_bigbasket=?""", (bigbasket_price, url))

        else:
            print("FLAG: Is the following url correct? {}".format(url))

conn.commit()
c.close()
conn.close()
