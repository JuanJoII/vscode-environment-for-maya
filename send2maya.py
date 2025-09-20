import socket
import sys
from pathlib import Path

# Ip local y puerto por defecto de Maya
HOST = "127.0.0.1"
PORT = 4434


def enviar_a_maya(script_text: str):
    try:
        # Crear socket y conectar a Maya
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # Enviar cada línea del script 
            for line in script_text.splitlines():
                if line.strip():  # evitar líneas vacías
                    comando = line.replace('"', '\\"') 
                    s.send(f'python("{comando}")\r\n'.encode()) # Enviar todo a Maya
            print("✅ Script enviado a Maya")
    except Exception as e:
        print("❌ Error al enviar a Maya:", e)

# Función main recibe el archivo .py como argumento, pathlib se encarga de leer el archivo para procesarlo en la función anterior
def main():
    if len(sys.argv) < 2:
        print("⚠️ Debes pasar un archivo .py como argumento")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print("⚠️ Archivo no encontrado:", file_path)
        sys.exit(1)

    script_text = file_path.read_text(encoding="utf-8")
    enviar_a_maya(script_text)


if __name__ == "__main__":
    main()
