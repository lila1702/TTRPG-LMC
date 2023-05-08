from connect_to_database import connection

# Main
conn = connection()

cursor = conn.cursor()



conn.commit()
cursor.close()

print("Executado com Sucesso!")