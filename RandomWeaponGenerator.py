# For my Capstone Project, I’m creating a Magic Weapon Generator in Python. This program will randomly generate unique magical weapons with different types, rarities, enchantments, and lore. Users can save and load generated weapons using JSON files, allowing for long-term storage. The project will showcase my understanding of OOP, randomization, file handling, and data structures in Python.
import random
import json
import re


class MagicWeapon:
    
    weapon_types = ["Club","Dagger","Greatclub","Handaxe","Javelin","Light hammer",
                    "Mace","Quarterstaff","Sickle","Spear","Battleaxe","Flail","Glaive",
                    "Greataxe","Greatsword","Halberd","Lance","Longsword","Maul",
                    "Morningstar","Pike","Rapier","Saber","Shortsword","Trident","War pick",
                    "Warhammer","Whip","Light Crossbow","Dart","Shortbow","Sling","Blowgun",
                    "Hand Crossbow", "Heavy Crossbow","Longbow","Pistol","Rifle"]
    
    rarities = ["Common", "Uncommon","Rare","Legendary","Mythic"]
    
    magic_effects_list =[ 
        ["Flame Wreath","and Burning touch"],
        ["Frostbite","and Lethargy Affliction"],
        ["Unbreaking","and Armor Piercing"],
        ["Lightning Strike","and Chain Attack"],
        ["Life Steal","and Dark Aura"],
        ["Poisoned","and Venomous Bite"]
        ]
    
    
    def __init__(self, name, weapon_type, rarity, magic_effects):
        self.name = name 
        self.weapon_type = weapon_type
        self.rarity = rarity
        self.magic_effects = magic_effects
        self.lore = self.generate_lore()
        
    def generate_lore(self):
        """Generate a randomized lore description for the weapon."""
        lore_templates = [
            "Forged in the {material} of {legendary_place}, this {weapon_type} was once wielded by {famous_wielder}.",
            "Legends say this {weapon_type} was blessed by {mystical_entity}, granting it the power of {element}.",
            "Discovered in the ruins of {ancient_place}, this {weapon_type} still hums with the echoes of past battles.",
            "This {weapon_type}, imbued with {magic_effects}, was created for {notable_purpose} during the {historical_event}."
                          ]
        #Lists of possible values for lore
        materials = ["fires", "depths", "sands", "storm clouds"]
        legendary_places = ["the Abyssal Forge", "Celestial Spire", "the Lost Temple", "the Dragon Forge"]
        famous_wielders = ["King Vaelor", "the Crimson Reaper", "an unknown warrior", "Royvan"]
        mystical_entities = ["a celestial dragon", "an ancient god", "a vengeful spirit"]
        elements = ["fire", "ice", "lightning", "shadow", "earth"]
        ancient_places = ["the Fallen Keep", "the Sunken City", "the Necropolis of Ash"]
        notable_purposes = ["a holy war", "the downfall of an empire", "a forbidden ritual"]
        historical_events = ["the Demon Wars", "the Age of Titans", "the Last King’s Rebellion"]

        #Select a random template and fill in the details
        template = random.choice(lore_templates)
        lore = template.format(
            material=random.choice(materials),
            legendary_place=random.choice(legendary_places),
            weapon_type=self.weapon_type,
            famous_wielder=random.choice(famous_wielders),
            mystical_entity=random.choice(mystical_entities),
            element=random.choice(elements),
            ancient_place=random.choice(ancient_places),
            magic_effects=", ".join(self.magic_effects),
            notable_purpose=random.choice(notable_purposes),
            historical_event=random.choice(historical_events),
        )
        return lore
    
    
    
    def get_user_input(prompt, options=None):
        """Helper function to get user input with optional randomization."""
        while True:
            user_input = input(prompt).strip().lower()
            if user_input == "random":
                return None # Signal to randomize this value
            elif not options or user_input in options:
                return user_input
            else: 
                print("Invalid input. Please try again.")
    
    def create_weapon():
        """Handles user input for weapon creation."""
        print("\n === Magic Weapon Generator === ")

        
        # Get weapon type (allowing randomization)
        weapon_type = MagicWeapon.get_user_input("Enter weapon type or type 'random':", MagicWeapon.weapon_types)
        if weapon_type == 'random' or not weapon_type:
            weapon_type = random.choice(MagicWeapon.weapon_types)
        
        # Get rarity (allowing randomization)
        rarity = MagicWeapon.get_user_input("Enter weapon rarity (Common, Uncommon, Rare, Legendary, Mythic) or type 'random': ", MagicWeapon.rarities)
        if rarity == 'random' or not rarity:
            rarity = random.choice(MagicWeapon.rarities)

        # Get magic effects (allowing randomization)
        magic_effects_input = input("Enter a magic effect (or type 'random' to get two random effects): ")
        if magic_effects_input == 'random' or not magic_effects_input:
            magic_effects = random.choice(MagicWeapon.magic_effects_list)
        else:
            magic_effects = [effect.strip() for effect in magic_effects_input.split(',')]

        name = MagicWeapon.generate_weapon_name(weapon_type, rarity, magic_effects)


        weapon = MagicWeapon(name, weapon_type, rarity, magic_effects)
        print("\nGenerated Weapon:")
        print(f"Name: {weapon.name}")
        print(f"Type: {weapon.weapon_type}")
        print(f"Rarity: {weapon.rarity}")
        print(f"Magic Effects: {', '.join(weapon.magic_effects)}")
        print(f"Lore: {weapon.lore}")
        
    
        save_to_file = input("Do you want to save this weapon to a JSON file? (yes/no): ").strip().lower()
        if save_to_file == "yes":
                MagicWeapon.save_weapon_to_json(weapon)
        return weapon 
    
    def generate_weapon_name(weapon_type, rarity, magic_effects):
        """Generates a name for the weapon based on its attributes."""
        name_parts = []
        name_parts.append(f"{rarity} {weapon_type}")

        if magic_effects:
            name_parts.append(f"of {' '.join(magic_effects)}")
        
        name = " ".join(name_parts)
        return name
    
    def get_user_input(prompt, options=None):
        """Helper function to get user input with optional randomization."""
        while True:
            user_input = input(prompt).strip().lower()
            if user_input == "random":
                return None 
            else:
                return user_input.capitalize()
            
    @staticmethod
    def save_weapon_to_json(weapon):
        """Saves the weapon to a JSON file."""
        weapon_dict = {
            "name": weapon.name,
            "weapon_type": weapon.weapon_type,
            "rarity": weapon.rarity,
            "magic_effects": weapon.magic_effects,
            "lore": weapon.lore
        }
        
        sanitized_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', weapon.name)

        filename = f"{sanitized_name}.json"
        with open(filename, 'w') as file:
            json.dump(weapon_dict, file, indent=4)
        print(f"Weapon saved to {filename}.")

    @staticmethod
    def view_weapon_from_json(filename):
        """Loads and displays weapon data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                weapon_data = json.load(file)
                print("\nWeapon Details from JSON:")
                print(f"Name: {weapon_data['name']}")
                print(f"Type: {weapon_data['weapon_type']}")
                print(f"Rarity: {weapon_data['rarity']}")
                print(f"Magic Effects: {', '.join(weapon_data['magic_effects'])}")
                print(f"Lore: {weapon_data['lore']}")
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file '{filename}' is not a valid JSON file.")



def main():
    while True:
        print("\n=== Welcome to the Magic Weapon Generator ===")
        print("1. Create a new weapon")
        print("2. Load an existing weapon from JSON")
        print("3. Quit")
        choice = input("Please enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            MagicWeapon.create_weapon()
        elif choice == '2':
            filename = input("Enter the filename (including .json) to load the weapon: ").strip()
            MagicWeapon.view_weapon_from_json(filename)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
main()

