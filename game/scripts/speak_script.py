from ..npc.npc_scripting import load_csv_npc
from ..scripts.area_deplacement import player,people,world,objs

def speak_script(gui, command, npc_id):
    npc =  people[npc_id]
    gui.display("\n═══════════════════════════════")
    gui.display(f"👤 {npc.name}")
    gui.display("═══════════════════════════════")
    gui.display(f" {npc.description}")
    # --- NPC neutre ---
    if npc.role == 'neutral':
        if npc.id == 'CAFE':
            gui.display("☕ Tu as reçu du café !")
            player.add_inv("CAFE")
        if npc.id == "DISTRIBUTEUR":
            gui.display("🥞 Tu as reçu une marmout !")
            player.add_inv("MARMOUT")

    # --- NPC amical ---
    if npc.role == 'friendly':
        if npc_id == "PROFSECR":
            gui.display("📚 Bonjour nouvel élève, voici ta carte étudiante !")
            gui.display("🎖️ Tu as reçu une Carte Étudiante !")
            player.add_inv("CARTEETU")
        else:
            gui.display("👋 Salut, c'est Johnny !\n")

    gui.update_info(player)

    if npc.role =='hostile' :
        gui.display("⚔️ Ce professeur veut te défier dans un quizz ! [ENTER]")
        return f"fight_script {npc_id}"
    gui.display("\n🔎(Le dialogue se termine. Tu peux regarder autour de toi avec [look].)\n")
    return "area_deplacement"
