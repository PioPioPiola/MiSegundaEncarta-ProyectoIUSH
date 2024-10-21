from Models.database import query_db, get_db

def crearTablaBd():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS tbl_secciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT
        )
    ''')
    db.commit()

def AgregarSeccion(nombre, descripcion):
    db = get_db()
    db.execute('INSERT INTO tbl_secciones (nombre, descripcion) VALUES (?, ?)', (nombre, descripcion))
    db.commit()

def ObtenerSecciones():
    return query_db('SELECT * FROM tbl_secciones')

def ObtenerSeccion(idSeccion):
    return query_db('SELECT * FROM tbl_secciones WHERE id = ?', [idSeccion], one = True)

def ModificarSeccion(idSeccion, nombre, descripcion):
    db = get_db()
    db.execute('UPDATE tbl_secciones SET nombre = ?, descripcion = ? WHERE id = ?', (nombre, descripcion, idSeccion))
    db.commit()

def EliminarSeccion(idSeccion):
    db = get_db()
    db.execute('DELETE FROM tbl_secciones WHERE id = ?', [idSeccion])
    db.commit()
