from sqlalchemy import create_engine, text
import ast
import json

# Configuración de la base de datos
DATABASE_URL = "sqlite:///rutina2025.sqlite"
engine = create_engine(DATABASE_URL)
connection = engine.connect()

# Consulta para obtener las rutinas
result = connection.execute(text("SELECT id, pasos FROM rutinas"))
for row in result:
    id_rutina = row[0]  # Acceso por índice
    pasos_raw = row[1]  # Acceso por índice

    try:
        # Convertir de representación de diccionario a JSON válido
        pasos_dict = ast.literal_eval(pasos_raw)
        pasos_json = json.dumps(pasos_dict)
        
        # Actualizar en la base de datos
        connection.execute(
            text("UPDATE rutinas SET pasos = :pasos WHERE id = :id"),
            {"pasos": pasos_json, "id": id_rutina}
        )
        print(f"Rutina {id_rutina} actualizada correctamente.")
    except Exception as e:
        print(f"Error procesando rutina {id_rutina}: {e}")

connection.close()
