import os
import shutil
import time

def clean_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    new_folder_path = os.path.join(desktop_path, "Organized")

    # Erstelle einen neuen Ordner, wenn er noch nicht existiert
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # Liste von Dateiendungen, die organisiert werden sollen
    allowed_extensions = ["txt", "pdf", "png", "jpg", "jpeg", "gif", "mp4", "mp3", "wav", "zip", "rar", "exe", "msi", "iso"]

    while True:
        # Durchlaufe alle Dateien auf dem Desktop
        for filename in os.listdir(desktop_path):
            file_path = os.path.join(desktop_path, filename)

            # Ignoriere Ordner und das aktuelle Skript
            if os.path.isdir(file_path) or filename == "desktop_cleaner.py":
                continue

            # Überprüfe die Dateiendung
            file_extension = filename.split(".")[-1]
            if file_extension in allowed_extensions:
                # Verschiebe die Datei in den neuen Ordner
                destination_folder = os.path.join(new_folder_path, file_extension.upper())
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Die Datei {filename} wurde in {file_extension.upper()} verschoben.")
            else:
                print(f"Die Datei {filename} hat eine nicht erlaubte Endung und wurde nicht verschoben.")

        # Warte für eine gewisse Zeit, bevor der nächste Durchlauf erfolgt (z.B., alle 60 Sekunden)
        time.sleep(30)

# Rufe die Funktion auf
clean_desktop()
