import os
import json

# Chemin absolu vers le dossier de travail
workspace_path = os.getenv('GITHUB_WORKSPACE')

# Chemin relatif vers le fichier apps.json dans le dépôt cloné
input_file_path = os.path.join(workspace_path, 'ipa', 'apps.json')

# Chemin vers le fichier de sauvegarde
output_file_path = os.path.join(workspace_path, 'scarlet_apps.json')

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