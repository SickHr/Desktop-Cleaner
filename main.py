import os
import shutil
import time

def clean_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    new_folder_path = os.path.join(desktop_path, "Organized")

    # Erstelle einen neuen Ordner, wenn er noch nicht existiert
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # Dictionary, das Dateiendungen den entsprechenden Ordnern zuordnet
    extension_categories = {
        "jpg": "Bilder",
        "jpeg": "Bilder",
        "png": "Bilder",
        "gif": "Bilder",
        "txt": "Dokumente",
        "pdf": "Dokumente",
        "mp4": "Anwendungen",
        "mp3": "Anwendungen",
        "wav": "Anwendungen",
        "zip": "Anwendungen",
        "rar": "Anwendungen",
        "exe": "Anwendungen",
        "msi": "Anwendungen",
        "iso": "Anwendungen"
    }

    while True:
        # Durchlaufe alle Dateien auf dem Desktop
        for filename in os.listdir(desktop_path):
            file_path = os.path.join(desktop_path, filename)

            # Ignoriere Ordner und das aktuelle Skript
            if os.path.isdir(file_path) or filename == "desktop_cleaner.py":
                continue

            # Überprüfe die Dateiendung und erhalte den zugehörigen Ordner
            file_extension = filename.split(".")[-1]
            destination_folder = os.path.join(new_folder_path, extension_categories.get(file_extension, "Allgemein"))

            # Verschiebe die Datei in den entsprechenden Ordner
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Die Datei {filename} wurde in den Ordner {destination_folder} verschoben.")

        # Warte für eine gewisse Zeit, bevor der nächste Durchlauf erfolgt (z.B., alle 60 Sekunden)
        time.sleep(30)

# Rufe die Funktion auf
clean_desktop()
