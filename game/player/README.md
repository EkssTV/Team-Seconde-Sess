# EPHEC QUEST – Player Class

## 📌 Overview
This module defines the `Player` class, which represents a player in the EPHEC QUEST game. It handles player identity, inventory, health, location, and script progression. It also provides save/load functionality for persistent game state.

---

## 🧱 Attributes

| Attribute        | Type   | Description                                  |
|------------------|--------|----------------------------------------------|
| `inv`            | `list` | Player's inventory (list of item IDs)        |
| `__name`         | `str`  | Private name of the player                   |
| `health`         | `int`  | Current health points                        |
| `current_area`   | `str`  | Current area ID                              |
| `current_script` | `str`  | Current script ID                            |
| `save_path`      | `str`  | Path to the player's save file               |

---

## ⚙️ Methods

### Inventory Management
- `add_inv(id_obj: str)`  
  Adds an item to the player's inventory.

- `supp_inv(id_obj: str)`  
  Removes an item from the inventory if it exists.

### Health Management
- `add_health(much: int)`  
  Increases the player's health.

- `supp_health(much: int)`  
  Decreases the player's health safely. Prints a message if health reaches zero.

### Movement & Script
- `move_area(new_area: str)`  
  Updates the player's current area.

- `change_script(new_script: str)`  
  Updates the current script.

### Identity
- `name` (property)  
  Gets or sets the player's name with validation (non-empty).

### Persistence
- `save()`  
  Saves the player's current state to a JSON file.

- `load()`  
  Loads the player's state from a JSON file. Handles missing or invalid files gracefully.

### Display
- `__str__()`  
  Returns a readable summary of the player's state.

---

## 🛡️ Error Handling
- `load()` handles:
  - `FileNotFoundError`: Save file is missing.
  - `JSONDecodeError`: Save file is corrupted or invalid.
  - `IOError`: General I/O issues.

- `name` setter raises:
  - `ValueError`: If the name is empty or only whitespace.

---

## 🧪 Example Usage

```python
ekss = Player('Ekss')
ekss.add_inv('sword')
ekss.add_health(10)
ekss.save()
print(ekss)
```
---
## 👨‍💻 Author

**Matthieu**  
EPHEC QUEST – 2025  
Responsible for the Player module
---
