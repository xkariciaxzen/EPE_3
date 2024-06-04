# -- coding: utf-8 --
import sqlite3
import csv

def crear_tabla():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        producto TEXT,
        categoria TEXT,
        precio REAL,
        cantidad INTEGER,
        total REAL
    )
    ''')
    conexion.commit()
    conexion.close()

def insertToDb(ventas):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', ventas)
    conexion.commit()
    conexion.close()

def leer_datos():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def buscar_por_fecha(fecha):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas WHERE fecha = ?', (fecha,))
    ventas = cursor.fetchall()
    #devolver diccionario con key nombre del campo:
    ventas = [dict(id=venta[0], fecha=venta[1], producto=venta[2], categoria=venta[3], precio=venta[4], cantidad=venta[5], total=venta[6]) for venta in ventas]
    conexion.close()
    return ventas

def exportar_csv():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    with open('ventas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])
        writer.writerows(ventas)

# Crear la tabla
crear_tabla()

# Datos de ejemplo
ventas = [
  ('2023-05-10', 'Bicicleta de Montaña', 'Deportes', 900000, 1, 900000),
    ('2024-01-22', 'Raqueta de Tenis Wilson', 'Deportes', 300000, 2, 600000),
    ('2023-08-15', 'Balón de Fútbol Adidas', 'Deportes', 150000, 3, 450000),
    ('2021-11-30', 'Gafas de Sol Ray-Ban', 'Accesorios', 250000, 2, 500000),
    ('2022-06-14', 'Reloj Casio', 'Accesorios', 200000, 1, 200000),
    ('2023-09-21', 'Mochila Herschel', 'Accesorios', 180000, 3, 540000),
    ('2024-03-05', 'Set de Anillos de Plata', 'Accesorios', 120000, 5, 600000),
    ('2022-12-10', 'Aspiradora Dyson', 'Hogar', 1300000, 1, 1300000),
    ('2023-11-12', 'Lámpara de Mesa Philips', 'Hogar', 70000, 4, 280000),
    ('2023-02-19', 'Sofá de Cuero', 'Hogar', 3000000, 1, 3000000),
    ('2024-05-01', 'Mesa de Comedor', 'Hogar', 1500000, 1, 1500000),
    ('2021-07-23', 'Silla Ergonomica', 'Oficina', 450000, 2, 900000),
    ('2023-03-08', 'Escritorio de Madera', 'Oficina', 750000, 1, 750000),
    ('2023-05-27', 'Lámpara de Escritorio', 'Oficina', 50000, 3, 150000),
    ('2024-01-15', 'Organizador de Archivos', 'Oficina', 30000, 4, 120000),
    ('2023-10-10', 'Impresora HP LaserJet', 'Oficina', 350000, 1, 350000),
    ('2022-08-09', 'Libro "El Quijote"', 'Libros', 40000, 2, 80000),
    ('2023-12-04', 'Libro "Cien Años de Soledad"', 'Libros', 45000, 3, 135000),
    ('2024-04-20', 'Libro "1984" de George Orwell', 'Libros', 30000, 5, 150000),
    ('2021-02-14', 'Juego de Mesa "Catan"', 'Juguetes', 120000, 1, 120000),
    ('2022-11-11', 'Muñeca Barbie', 'Juguetes', 70000, 2, 140000),
    ('2023-04-29', 'Lego Star Wars', 'Juguetes', 150000, 1, 150000),
    ('2024-05-10', 'Puzzle 1000 piezas', 'Juguetes', 60000, 4, 240000),
    ('2023-01-30', 'Drone DJI Mini 2', 'Tecnología', 1300000, 1, 1300000)
]

# Insertar los datos de ejemplo en la base de datos
for venta in ventas:
    insertToDb(venta)

# Imprimir ventas del día
print('Ventas del día:')

# Buscar por fecha
ventas_hoy = buscar_por_fecha('2024-05-20')

for venta in ventas_hoy:
    print(int(venta['total']))

# Exportar datos a CSV
exportar_csv()