import os
sorted_list = []
def saved_player():
    """
    Returns a list of saved player names (without file extensions) found in the save directory.

    This function scans the '../../saves' directory, filters out only the files,
    removes their extensions (e.g., '.json'), and returns a clean list of player names.

    Returns:
        list[str]: A list of saved player names without file extensions.
    """
    global sorted_list
    path_to_saves = 'saves'
    list_saved_player = os.listdir(path_to_saves)
    list_saved_player_cleared = []
    for file in list_saved_player:
        full_path = os.path.join(path_to_saves, file)
        if os.path.isfile(full_path):
            nom_sans_ext = os.path.splitext(file)[0]
            list_saved_player_cleared.append(nom_sans_ext)
        sorted_list = sorted(list_saved_player_cleared,key=lambda x:str(x).lower(),reverse=False)
    return sorted_list
