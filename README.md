# 🏗️ Maya + VSCode: Entorno de Desarrollo en Python
Este entorno permite escribir y ejecutar código Python para **Autodesk Maya** directamente desde **Visual Studio Code (VSCode)**, aprovechando las ventajas de **[uv](https://github.com/astral-sh/uv)** para la gestión de dependencias y entornos virtuales.

---

## 🚀 Requisitos Previos
Asegúrate de tener instalado:
- [Python](https://www.python.org/downloads/)
- [VSCode](https://code.visualstudio.com/)
- [pipx](https://pypa.github.io/pipx/) (recomendado para instalar herramientas aisladas)

---

## 1️⃣ Instalación de `uv`
[uv](https://github.com/astral-sh/uv) es una herramienta moderna para manejar entornos Python de forma **rápida** y **eficiente**.

Instálalo con:
```bash
# Instlación con un gestor de paquetes recomendado
pipx install uv

# Intalación de uv como un standalone en Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
````

---

## 2️⃣ (Opcional) Instalación de `ruff`

[ruff](https://github.com/astral-sh/ruff) es un linter y formateador de código extremadamente rápido, útil para mantener un estilo consistente.

Puedes instalarlo de dos maneras:

```bash
# Con uvx (recomendado si ya usas uv)
uvx install ruff

# O con pipx
pipx install ruff
```

---

## 3️⃣ Configurar la versión de Python de Maya

Maya utiliza su propia versión de Python. Para verificarla, abre la **Consola de Python** dentro de Maya y ejecuta:

```python
import sys
print(sys.version)
```

Con esa versión:

* Edita el archivo **`pyproject.toml`** y el archivo **`.python-version`** del proyecto para que coincidan con la versión de Python que usa Maya.
* Esto permite a `uv` crear un entorno compatible.

---

## 4️⃣ Configuración de `userSetup.py`

Para que VSCode pueda enviar el código a Maya, es necesario habilitar un **puerto de escucha** en Maya.

1. Dirígete a:

   ```
   C:\Users\<TU_USUARIO>\Documents\maya\<VERSION_DE_MAYA>\scripts
   ```
2. Verifica si existe un archivo llamado **`userSetup.py`**.

   * Si **no existe**, créalo.
3. Agrega el siguiente código (actualiza la ruta del proyecto):

```python
import maya.cmds as cmds
import sys

# Agregar la ruta del proyecto para importar módulos propios
sys.path.append(r"ruta\del\proyecto")

# Abrir el puerto para comunicación con VSCode
if not cmds.commandPort(":4434", query=True):
    cmds.commandPort(name=":4434")
```

💡 **Tip:** Usa doble barra `\\` o prefijo `r""` para las rutas en Windows.

---

## ⚠️ Archivo crítico: `send2maya.py`

El archivo **`send2maya.py`** es el núcleo de la comunicación entre VSCode y Maya.
Este archivo:

* Envía el código a Maya.
* Gestiona la conexión del socket.
* Controla la ejecución del proyecto.

⚠️ **No modifiques este archivo bajo ninguna circunstancia.**
Cualquier cambio podría romper la conexión y el flujo de trabajo.

---

## 5️⃣ Ejecución del código desde VSCode

Con todo configurado, ya puedes ejecutar código en Maya:

1. Abre en VSCode el archivo que deseas correr (por ejemplo, `main.py`).
2. Presiona **`Ctrl + Shift + B`**.
3. El archivo se enviará automáticamente a Maya a través del puerto configurado.

El archivo `tasks.json` incluido en el proyecto ya está preparado para manejar esta tarea.

---

## ✅ Resumen de Flujo de Trabajo

1. Instala **uv** y (opcional) **ruff**.
2. Ajusta `pyproject.toml` y `.python-version` a la versión de Python de Maya.
3. Configura `userSetup.py` para abrir el puerto y añadir la ruta del proyecto.
4. **No toques `send2maya.py`.**
5. Usa **Ctrl + Shift + B** en VSCode para ejecutar el código en Maya, en consola deberia aparecer algo así:

```
✅ Ejecutado en Maya con UTF-8: C:/ruta/del/proyecto/main.py
```
