import os
from .exeption_saved_player import SaveDirectoryError
def saved_player():
    """
    Returns a list of saved player names (without file extensions) found in the save directory.
    """
    path_to_saves = "saves"

    # Vérifier si le dossier existe
    if not os.path.exists(path_to_saves):
        raise SaveDirectoryError(f"Le dossier '{path_to_saves}' est introuvable.")

    try:
        files = os.listdir(path_to_saves)
    except Exception as e:
        raise SaveDirectoryError(f"Impossible de lire le dossier '{path_to_saves}' : {e}")

    list_saved_player_cleared = []

    for file in files:
        full_path = os.path.join(path_to_saves, file)
        if os.path.isfile(full_path):
            nom_sans_ext = os.path.splitext(file)[0]
            list_saved_player_cleared.append(nom_sans_ext)

    # Tri de la liste
    sorted_list = sorted(
        list_saved_player_cleared,
        key=lambda x: str(x).lower()
    )

    return sorted_list
