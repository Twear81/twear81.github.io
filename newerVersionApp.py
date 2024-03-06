import json

# Chemin vers le fichier apps.json
input_file_path = "./ipa/apps.json"  # Remplacez /path/to/apps.json par le chemin réel de votre fichier apps.json
# Chemin vers le fichier de sauvegarde
output_file_path = "./scarlet_apps.json"  # Remplacez /path/to/modified_apps.json par le chemin réel de votre fichier de sauvegarde

# Charger les données JSON du fichier
with open(input_file_path, 'r') as file:
    json_data = file.read()

# Charger les données JSON
data = json.loads(json_data)

# Modifier les données en extrayant seulement le premier élément de chaque "versions" array
for app in data['apps']:
    if 'versions' in app:
        app['versions'] = app['versions'][:1]

# Écrire les données modifiées dans le fichier de sauvegarde
with open(output_file_path, 'w') as file:
    json.dump(data, file, indent=4)