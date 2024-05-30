import random

# Character Stats (Adjustable for Difficulty)
difficulty = "extreme"  # Choose "normal", "hard", or "extreme"
health_base = 100
mana_base = 50
attack_base = 20
defense_base = 15
inventory = []

# Difficulty Adjustments
difficulty_stats = {
    "normal": {"health_modifier": 0, "mana_modifier": 0, "attack_modifier": 0, "defense_modifier": 0},
    "hard": {"health_modifier": -20, "mana_modifier": -10, "attack_modifier": -5, "defense_modifier": -3},
    "extreme": {"health_modifier": -40, "mana_modifier": -20, "attack_modifier": -10, "defense_modifier": -5},
}

health = health_base + difficulty_stats[difficulty]["health_modifier"]
mana = mana_base + difficulty_stats[difficulty]["mana_modifier"]
attack = attack_base + difficulty_stats[difficulty]["attack_modifier"]
defense = defense_base + difficulty_stats[difficulty]["defense_modifier"]

# Dragon Stats (Highly Adjustable for Difficulty)
dragon_health_base = 400  # Increased base health for extreme difficulty
dragon_attack_base = 50  # Increased base attack
dragon_fire_breath_chance = 35  # Increased fire breath chance
dragon_stats_modifier = {
    "normal": {"health_modifier": 0, "attack_modifier": 0},
    "hard": {"health_modifier": 50, "attack_modifier": 5},
    "extreme": {"health_modifier": 100, "attack_modifier": 15},
}

dragon_health = dragon_health_base + dragon_stats_modifier[difficulty]["health_modifier"]
dragon_attack = dragon_attack_base + dragon_stats_modifier[difficulty]["attack_modifier"]

# Potions (Limited Availability)
potions = {"healing": 1, "mana": 1}  # Potion types and quantities
potion_effectiveness = {
    "normal": {"healing": 20, "mana": 20},
    "hard": {"healing": 15, "mana": 15},
    "extreme": {"healing": 10, "mana": 10},
}

# Skills (High Mana Cost, Cooldown)
skills = {
    "fireball": {
        "mana_cost": 20,
        "damage": 35,
        "description": "A scorching fireball that deals high damage."
    },
    "heal": {"mana_cost": 25, "heal_amount": potion_effectiveness[difficulty]["healing"], "description": "Restores health points."},
    "shield": {
        "mana_cost": 15,
        "defense_bonus": 7,
        "duration": 2,
        "cooldown": 1,  # Cooldown for 1 round after use
        "description": "Increases defense for a short duration."
    },
    "frostbite": {
        "mana_cost": 30,
        "damage": 25,
        "chance_to_freeze": 40,  # Increased chance to freeze
        "freeze_duration": 1,  # Dragon is frozen for 1 round
        "description": "A blast of icy wind that deals moderate damage and may freeze the dragon."
    },
}

# Level Up System (Optional)
experience = 0
level = 1
level_up_xp = 100
level_up_stats = {
    "health": 5,
    "mana": 3,
    "attack": 2,
    "defense": 1,
}


# Game Functions
def fight():
    global health, mana, dragon_health, inventory, experience, level
    shield_active = False  # Flag for shield duration and cooldown
    shield_cooldown = 0  # Counter for shield cooldown

    while health > 0 and dragon_health > 0:
        # Player turn
        print(f"\nYour turn! Health: {health}, Mana: {mana}, Level: {level}")
        print("1. Attack")
        print("2. Use Skill")
        print("3. Use Potion")
        print("4. Check Inventory")

        choice =
        