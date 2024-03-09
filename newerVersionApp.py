import json

# Chemin vers le fichier apps.json
input_file_path = "./ipa/apps.json"  # Remplacez /path/to/apps.json par le chemin réel de votre fichier apps.json
# Chemin vers le fichier de sauvegarde
output_file_path = "./main/scarlet_apps.json"  # Remplacez /path/to/modified_apps.json par le chemin réel de votre fichier de sauvegarde

# Charger les données JSON du fichier
with open(input_file_path, 'r') as file:
    json_data = file.read()

# Charger les données JSON
data = json.loads(json_data)

# Modifier les données en extrayant seulement le premier élément de chaque "versions" array
for app in data['apps']:
    if 'versions' in app:
        app['versions'] = app['versions'][:1]

# Créer la structure de données dans le nouveau format
new_data = {
    "META": {
        "repoName": "swaggyP36000 IPA Library By Twear",
        "repoIcon": "https://cdn3.iconfinder.com/data/icons/ultimate-social/150/17_google_play-512.png"
    },
    "Tweaked": []
}

# Convertir les applications
for app in data["apps"]:
    game = {
        "name": app["name"],
        "version": app["versions"][0]["version"],
        "down": app["versions"][0]["downloadURL"],
        "category": "Tweaked Apps",
        "description": app["versions"][0]["localizedDescription"],
        "bundleID": app["bundleIdentifier"],
        "appstore": app["bundleIdentifier"],  # Cela peut nécessiter une mise à jour en fonction de la logique réelle
        "icon": app["iconURL"]  # Lien vers l'icône ajouté
    }
    new_data["Tweaked"].append(game)


# Écrire les données modifiées dans le fichier de sauvegarde
with open(output_file_path, 'w') as file:
    json.dump(new_data, file, indent=4)
