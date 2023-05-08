import urllib.parse as up
import psycopg2

def connection():
    arquivo = open("C:/Users/Lila/Documents/Projetos/Privados/db_kob.txt", 'r')
    up.uses_netloc.append("postgres")
    url = up.urlparse(arquivo.readline())
    arquivo.close()
    return psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)