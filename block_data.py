"""
Block Data for Minecraft X-Ray Resource Pack Generator
=======================================================

This file contains all block definitions, categories, and presets.
Edit this file to add/remove blocks or create new presets.
"""

# =============================================================================
# MINECRAFT VERSION TO PACK FORMAT MAPPING
# =============================================================================

# Maps Minecraft version ranges to their corresponding resource pack format number.
# Source: https://minecraft.wiki/w/Pack_format
VERSION_TO_PACK_FORMAT = {
    "1.21.4": 46,
    "1.21.2 - 1.21.3": 42,
    "1.21 - 1.21.1": 34,
    "1.20.5 - 1.20.6": 32,
    "1.20.3 - 1.20.4": 22,
    "1.20.2": 18,
    "1.20 - 1.20.1": 15,
    "1.19.4": 13,
    "1.19.3": 12,
    "1.19 - 1.19.2": 9,
    "1.18 - 1.18.2": 8,
    "1.17 - 1.17.1": 7,
    "1.16.2 - 1.16.5": 6,
    "1.15 - 1.16.1": 5,
}


# =============================================================================
# BLOCK CATEGORIES
# =============================================================================

# Blocks are organized into categories for easier navigation in the UI.
# Each category maps to a list of block IDs (without "minecraft:" prefix).

BLOCK_CATEGORIES = {
    # --- Ores ---
    "Ores (Overworld)": [
        "coal_ore", "copper_ore", "iron_ore", "gold_ore", "lapis_ore",
        "redstone_ore", "diamond_ore", "emerald_ore",
        "deepslate_coal_ore", "deepslate_copper_ore", "deepslate_iron_ore",
        "deepslate_gold_ore", "deepslate_lapis_ore", "deepslate_redstone_ore",
        "deepslate_diamond_ore", "deepslate_emerald_ore",
    ],
    "Ores (Nether)": [
        "nether_gold_ore", "nether_quartz_ore", "ancient_debris",
    ],

    # --- Natural Blocks ---
    "Stone and Dirt": [
        "stone", "granite", "diorite", "andesite", "tuff",
        "dirt", "coarse_dirt", "rooted_dirt", "grass_block", "podzol", "mycelium", "farmland",
        "gravel", "clay", "sand", "red_sand", "mud", "packed_mud",
        "calcite", "smooth_basalt", "amethyst_block", "budding_amethyst",
        "dripstone_block", "pointed_dripstone",
    ],
    "Cobblestone and Bricks": [
        "cobblestone", "mossy_cobblestone", "cobbled_deepslate",
        "sandstone", "chiseled_sandstone", "cut_sandstone", "smooth_sandstone",
        "red_sandstone", "chiseled_red_sandstone", "cut_red_sandstone", "smooth_red_sandstone",
        "stone_bricks", "cracked_stone_bricks", "mossy_stone_bricks", "chiseled_stone_bricks",
        "deepslate_bricks", "cracked_deepslate_bricks", "deepslate_tiles", "cracked_deepslate_tiles",
        "bricks", "mud_bricks",
    ],
    "Deepslate Variants": [
        "deepslate", "polished_deepslate", "chiseled_deepslate",
        "deepslate_bricks", "cracked_deepslate_bricks",
        "deepslate_tiles", "cracked_deepslate_tiles",
    ],

    # --- Dimension-Specific Blocks ---
    "Nether Blocks": [
        "netherrack", "magma_block", "soul_sand", "soul_soil",
        "blackstone", "gilded_blackstone", "polished_blackstone", "chiseled_polished_blackstone",
        "polished_blackstone_bricks", "cracked_polished_blackstone_bricks",
        "crimson_nylium", "warped_nylium",
        "nether_bricks", "red_nether_bricks", "cracked_nether_bricks", "chiseled_nether_bricks",
        "nether_wart_block", "warped_wart_block", "shroomlight",
        "glowstone", "crying_obsidian", "respawn_anchor",
    ],
    "End Blocks": [
        "end_stone", "end_stone_bricks", "purpur_block", "purpur_pillar",
    ],

    # --- Wood and Logs ---
    "Logs and Wood": [
        "oak_log", "spruce_log", "birch_log", "jungle_log", "acacia_log",
        "dark_oak_log", "mangrove_log", "cherry_log", "bamboo_block",
        "stripped_oak_log", "stripped_spruce_log", "stripped_birch_log",
        "stripped_jungle_log", "stripped_acacia_log", "stripped_dark_oak_log",
        "stripped_mangrove_log", "stripped_cherry_log", "stripped_bamboo_block",
        "oak_wood", "spruce_wood", "birch_wood", "jungle_wood", "acacia_wood",
        "dark_oak_wood", "mangrove_wood", "cherry_wood",
        "stripped_oak_wood", "stripped_spruce_wood", "stripped_birch_wood",
        "stripped_jungle_wood", "stripped_acacia_wood", "stripped_dark_oak_wood",
        "stripped_mangrove_wood", "stripped_cherry_wood",
        "crimson_stem", "warped_stem", "stripped_crimson_stem", "stripped_warped_stem",
        "crimson_hyphae", "warped_hyphae", "stripped_crimson_hyphae", "stripped_warped_hyphae",
    ],
    "Planks": [
        "oak_planks", "spruce_planks", "birch_planks", "jungle_planks",
        "acacia_planks", "dark_oak_planks", "mangrove_planks", "cherry_planks",
        "bamboo_planks", "bamboo_mosaic", "crimson_planks", "warped_planks",
    ],

    # --- Plants and Vegetation ---
    "Leaves and Plants": [
        "oak_leaves", "spruce_leaves", "birch_leaves", "jungle_leaves",
        "acacia_leaves", "dark_oak_leaves", "mangrove_leaves", "azalea_leaves",
        "flowering_azalea_leaves", "cherry_leaves",
        "grass", "tall_grass", "fern", "large_fern", "dead_bush",
        "dandelion", "poppy", "blue_orchid", "allium", "azure_bluet",
        "red_tulip", "orange_tulip", "white_tulip", "pink_tulip",
        "oxeye_daisy", "cornflower", "lily_of_the_valley", "torchflower", "pitcher_plant",
        "wither_rose", "sunflower", "lilac", "rose_bush", "peony",
        "vine", "glow_lichen", "hanging_roots", "moss_block", "moss_carpet",
        "azalea", "flowering_azalea", "spore_blossom", "big_dripleaf", "small_dripleaf",
    ],
    "Fungi and Mushrooms": [
        "brown_mushroom", "red_mushroom", "crimson_fungus", "warped_fungus",
        "brown_mushroom_block", "red_mushroom_block", "mushroom_stem",
    ],
    "Water Plants": [
        "lily_pad", "sugar_cane", "kelp", "kelp_plant", "seagrass", "tall_seagrass",
        "sea_pickle", "tube_coral", "brain_coral", "bubble_coral", "fire_coral", "horn_coral",
        "tube_coral_block", "brain_coral_block", "bubble_coral_block", "fire_coral_block", "horn_coral_block",
    ],
    "Vines and Roots": [
        "twisting_vines", "twisting_vines_plant", "weeping_vines", "weeping_vines_plant",
        "cave_vines", "cave_vines_plant",
    ],
    "Crops": [
        "wheat", "potatoes", "carrots", "beetroots", "nether_wart",
        "pumpkin", "carved_pumpkin", "jack_o_lantern", "melon",
        "cactus", "bamboo", "sweet_berry_bush",
    ],

    # --- Colored Blocks ---
    "Terracotta": [
        "terracotta", "white_terracotta", "orange_terracotta", "magenta_terracotta",
        "light_blue_terracotta", "yellow_terracotta", "lime_terracotta", "pink_terracotta",
        "gray_terracotta", "light_gray_terracotta", "cyan_terracotta", "purple_terracotta",
        "blue_terracotta", "brown_terracotta", "green_terracotta", "red_terracotta", "black_terracotta",
    ],
    "Glazed Terracotta": [
        "white_glazed_terracotta", "orange_glazed_terracotta", "magenta_glazed_terracotta",
        "light_blue_glazed_terracotta", "yellow_glazed_terracotta", "lime_glazed_terracotta",
        "pink_glazed_terracotta", "gray_glazed_terracotta", "light_gray_glazed_terracotta",
        "cyan_glazed_terracotta", "purple_glazed_terracotta", "blue_glazed_terracotta",
        "brown_glazed_terracotta", "green_glazed_terracotta", "red_glazed_terracotta", "black_glazed_terracotta",
    ],
    "Concrete": [
        "white_concrete", "orange_concrete", "magenta_concrete", "light_blue_concrete",
        "yellow_concrete", "lime_concrete", "pink_concrete", "gray_concrete",
        "light_gray_concrete", "cyan_concrete", "purple_concrete", "blue_concrete",
        "brown_concrete", "green_concrete", "red_concrete", "black_concrete",
        "white_concrete_powder", "orange_concrete_powder", "magenta_concrete_powder", "light_blue_concrete_powder",
        "yellow_concrete_powder", "lime_concrete_powder", "pink_concrete_powder", "gray_concrete_powder",
        "light_gray_concrete_powder", "cyan_concrete_powder", "purple_concrete_powder", "blue_concrete_powder",
        "brown_concrete_powder", "green_concrete_powder", "red_concrete_powder", "black_concrete_powder",
    ],
    "Wool": [
        "white_wool", "orange_wool", "magenta_wool", "light_blue_wool",
        "yellow_wool", "lime_wool", "pink_wool", "gray_wool",
        "light_gray_wool", "cyan_wool", "purple_wool", "blue_wool",
        "brown_wool", "green_wool", "red_wool", "black_wool",
    ],
    "Glass": [
        "glass", "tinted_glass",
        "white_stained_glass", "orange_stained_glass", "magenta_stained_glass",
        "light_blue_stained_glass", "yellow_stained_glass", "lime_stained_glass",
        "pink_stained_glass", "gray_stained_glass", "light_gray_stained_glass",
        "cyan_stained_glass", "purple_stained_glass", "blue_stained_glass",
        "brown_stained_glass", "green_stained_glass", "red_stained_glass", "black_stained_glass",
    ],
    "Glass Panes": [
        "glass_pane",
        "white_stained_glass_pane", "orange_stained_glass_pane", "magenta_stained_glass_pane",
        "light_blue_stained_glass_pane", "yellow_stained_glass_pane", "lime_stained_glass_pane",
        "pink_stained_glass_pane", "gray_stained_glass_pane", "light_gray_stained_glass_pane",
        "cyan_stained_glass_pane", "purple_stained_glass_pane", "blue_stained_glass_pane",
        "brown_stained_glass_pane", "green_stained_glass_pane", "red_stained_glass_pane", "black_stained_glass_pane",
    ],
    "Carpets": [
        "white_carpet", "orange_carpet", "magenta_carpet", "light_blue_carpet",
        "yellow_carpet", "lime_carpet", "pink_carpet", "gray_carpet",
        "light_gray_carpet", "cyan_carpet", "purple_carpet", "blue_carpet",
        "brown_carpet", "green_carpet", "red_carpet", "black_carpet",
    ],
    "Beds": [
        "white_bed", "orange_bed", "magenta_bed", "light_blue_bed",
        "yellow_bed", "lime_bed", "pink_bed", "gray_bed",
        "light_gray_bed", "cyan_bed", "purple_bed", "blue_bed",
        "brown_bed", "green_bed", "red_bed", "black_bed",
    ],
    "Banners": [
        "white_banner", "orange_banner", "magenta_banner", "light_blue_banner",
        "yellow_banner", "lime_banner", "pink_banner", "gray_banner",
        "light_gray_banner", "cyan_banner", "purple_banner", "blue_banner",
        "brown_banner", "green_banner", "red_banner", "black_banner",
    ],

    # --- Climate/Temperature Blocks ---
    "Ice and Snow": [
        "ice", "packed_ice", "blue_ice", "frosted_ice",
        "snow_block", "snow", "powder_snow",
    ],

    # --- Metals and Minerals ---
    "Metal Blocks": [
        "iron_block", "gold_block", "diamond_block", "emerald_block",
        "lapis_block", "redstone_block", "coal_block", "netherite_block",
        "raw_iron_block", "raw_gold_block", "raw_copper_block",
        "amethyst_block",
    ],
    "Copper Blocks": [
        "copper_block", "exposed_copper", "weathered_copper", "oxidized_copper",
        "cut_copper", "exposed_cut_copper", "weathered_cut_copper", "oxidized_cut_copper",
        "waxed_copper_block", "waxed_exposed_copper", "waxed_weathered_copper", "waxed_oxidized_copper",
        "waxed_cut_copper", "waxed_exposed_cut_copper", "waxed_weathered_cut_copper", "waxed_oxidized_cut_copper",
        "copper_grate", "exposed_copper_grate", "weathered_copper_grate", "oxidized_copper_grate",
        "waxed_copper_grate", "waxed_exposed_copper_grate", "waxed_weathered_copper_grate", "waxed_oxidized_copper_grate",
        "copper_bulb", "exposed_copper_bulb", "weathered_copper_bulb", "oxidized_copper_bulb",
        "waxed_copper_bulb", "waxed_exposed_copper_bulb", "waxed_weathered_copper_bulb", "waxed_oxidized_copper_bulb",
        "chiseled_copper", "exposed_chiseled_copper", "weathered_chiseled_copper", "oxidized_chiseled_copper",
        "waxed_chiseled_copper", "waxed_exposed_chiseled_copper", "waxed_weathered_chiseled_copper", "waxed_oxidized_chiseled_copper",
    ],
    "Prismarine": [
        "prismarine", "prismarine_bricks", "dark_prismarine",
    ],
    "Quartz": [
        "quartz_block", "chiseled_quartz_block", "quartz_bricks", "smooth_quartz",
    ],

    # --- Pillar Blocks (rotatable) ---
    "Pillar Blocks": [
        "deepslate", "basalt", "polished_basalt", "quartz_pillar", "purpur_pillar",
        "hay_block", "bone_block", "ochre_froglight", "verdant_froglight", "pearlescent_froglight",
    ],

    # --- Functional Blocks ---
    "Crafting and Utility": [
        "crafting_table", "furnace", "smoker", "blast_furnace",
        "cartography_table", "fletching_table", "smithing_table",
        "stonecutter", "grindstone", "loom",
        "enchanting_table", "bookshelf", "chiseled_bookshelf", "lectern",
        "anvil", "chipped_anvil", "damaged_anvil",
        "composter", "barrel", "cauldron", "brewing_stand",
    ],
    "Storage": [
        "chest", "trapped_chest", "ender_chest", "shulker_box",
        "white_shulker_box", "orange_shulker_box", "magenta_shulker_box", "light_blue_shulker_box",
        "yellow_shulker_box", "lime_shulker_box", "pink_shulker_box", "gray_shulker_box",
        "light_gray_shulker_box", "cyan_shulker_box", "purple_shulker_box", "blue_shulker_box",
        "brown_shulker_box", "green_shulker_box", "red_shulker_box", "black_shulker_box",
    ],

    # --- Redstone ---
    "Redstone Components": [
        "redstone_wire", "redstone_block", "redstone_lamp", "redstone_torch",
        "repeater", "comparator", "observer",
        "piston", "sticky_piston", "piston_head",
        "dispenser", "dropper", "hopper",
        "lever", "tripwire", "tripwire_hook",
        "daylight_detector", "target", "tnt", "sculk_sensor", "calibrated_sculk_sensor",
    ],
    "Pressure Plates": [
        "oak_pressure_plate", "spruce_pressure_plate", "birch_pressure_plate",
        "jungle_pressure_plate", "acacia_pressure_plate", "dark_oak_pressure_plate",
        "mangrove_pressure_plate", "cherry_pressure_plate", "bamboo_pressure_plate",
        "crimson_pressure_plate", "warped_pressure_plate",
        "stone_pressure_plate", "polished_blackstone_pressure_plate",
        "light_weighted_pressure_plate", "heavy_weighted_pressure_plate",
    ],
    "Buttons": [
        "oak_button", "spruce_button", "birch_button", "jungle_button",
        "acacia_button", "dark_oak_button", "mangrove_button", "cherry_button", "bamboo_button",
        "crimson_button", "warped_button",
        "stone_button", "polished_blackstone_button",
    ],
    "Rails": [
        "rail", "powered_rail", "detector_rail", "activator_rail",
    ],

    # --- Lighting ---
    "Lighting": [
        "torch", "wall_torch", "soul_torch", "soul_wall_torch",
        "lantern", "soul_lantern", "campfire", "soul_campfire",
        "candle", "white_candle", "orange_candle", "magenta_candle", "light_blue_candle",
        "yellow_candle", "lime_candle", "pink_candle", "gray_candle",
        "light_gray_candle", "cyan_candle", "purple_candle", "blue_candle",
        "brown_candle", "green_candle", "red_candle", "black_candle",
        "sea_lantern", "end_rod",
    ],

    # --- Building Components ---
    "Stairs": [
        "oak_stairs", "spruce_stairs", "birch_stairs", "jungle_stairs",
        "acacia_stairs", "dark_oak_stairs", "mangrove_stairs", "cherry_stairs", "bamboo_stairs",
        "crimson_stairs", "warped_stairs",
        "cobblestone_stairs", "mossy_cobblestone_stairs", "stone_stairs", "stone_brick_stairs", "mossy_stone_brick_stairs",
        "sandstone_stairs", "smooth_sandstone_stairs", "red_sandstone_stairs", "smooth_red_sandstone_stairs",
        "brick_stairs", "mud_brick_stairs", "nether_brick_stairs", "red_nether_brick_stairs",
        "deepslate_brick_stairs", "deepslate_tile_stairs", "polished_deepslate_stairs", "cobbled_deepslate_stairs",
        "polished_blackstone_stairs", "polished_blackstone_brick_stairs",
        "quartz_stairs", "smooth_quartz_stairs", "purpur_stairs",
        "prismarine_stairs", "prismarine_brick_stairs", "dark_prismarine_stairs",
        "end_stone_brick_stairs",
    ],
    "Slabs": [
        "oak_slab", "spruce_slab", "birch_slab", "jungle_slab",
        "acacia_slab", "dark_oak_slab", "mangrove_slab", "cherry_slab", "bamboo_slab",
        "crimson_slab", "warped_slab",
        "cobblestone_slab", "mossy_cobblestone_slab", "stone_slab", "smooth_stone_slab",
        "stone_brick_slab", "mossy_stone_brick_slab",
        "sandstone_slab", "smooth_sandstone_slab", "cut_sandstone_slab",
        "red_sandstone_slab", "smooth_red_sandstone_slab", "cut_red_sandstone_slab",
        "brick_slab", "mud_brick_slab", "nether_brick_slab", "red_nether_brick_slab",
        "deepslate_brick_slab", "deepslate_tile_slab", "polished_deepslate_slab", "cobbled_deepslate_slab",
        "polished_blackstone_slab", "polished_blackstone_brick_slab",
        "quartz_slab", "smooth_quartz_slab", "purpur_slab",
        "prismarine_slab", "prismarine_brick_slab", "dark_prismarine_slab",
        "end_stone_brick_slab",
    ],
    "Fences and Walls": [
        "oak_fence", "spruce_fence", "birch_fence", "jungle_fence",
        "acacia_fence", "dark_oak_fence", "mangrove_fence", "cherry_fence", "bamboo_fence",
        "crimson_fence", "warped_fence", "nether_brick_fence",
        "cobblestone_wall", "mossy_cobblestone_wall", "stone_brick_wall", "mossy_stone_brick_wall",
        "brick_wall", "mud_brick_wall", "sandstone_wall", "red_sandstone_wall",
        "deepslate_brick_wall", "deepslate_tile_wall", "polished_deepslate_wall", "cobbled_deepslate_wall",
        "blackstone_wall", "polished_blackstone_wall", "polished_blackstone_brick_wall",
        "nether_brick_wall", "red_nether_brick_wall",
        "prismarine_wall", "end_stone_brick_wall",
    ],
    "Fence Gates": [
        "oak_fence_gate", "spruce_fence_gate", "birch_fence_gate", "jungle_fence_gate",
        "acacia_fence_gate", "dark_oak_fence_gate", "mangrove_fence_gate", "cherry_fence_gate", "bamboo_fence_gate",
        "crimson_fence_gate", "warped_fence_gate",
    ],
    "Doors": [
        "oak_door", "spruce_door", "birch_door", "jungle_door",
        "acacia_door", "dark_oak_door", "mangrove_door", "cherry_door", "bamboo_door",
        "crimson_door", "warped_door", "iron_door", "copper_door", "exposed_copper_door",
        "weathered_copper_door", "oxidized_copper_door",
        "waxed_copper_door", "waxed_exposed_copper_door", "waxed_weathered_copper_door", "waxed_oxidized_copper_door",
    ],
    "Trapdoors": [
        "oak_trapdoor", "spruce_trapdoor", "birch_trapdoor", "jungle_trapdoor",
        "acacia_trapdoor", "dark_oak_trapdoor", "mangrove_trapdoor", "cherry_trapdoor", "bamboo_trapdoor",
        "crimson_trapdoor", "warped_trapdoor", "iron_trapdoor",
        "copper_trapdoor", "exposed_copper_trapdoor", "weathered_copper_trapdoor", "oxidized_copper_trapdoor",
        "waxed_copper_trapdoor", "waxed_exposed_copper_trapdoor", "waxed_weathered_copper_trapdoor", "waxed_oxidized_copper_trapdoor",
    ],

    # --- Decorative and Misc ---
    "Signs": [
        "oak_sign", "spruce_sign", "birch_sign", "jungle_sign",
        "acacia_sign", "dark_oak_sign", "mangrove_sign", "cherry_sign", "bamboo_sign",
        "crimson_sign", "warped_sign",
        "oak_hanging_sign", "spruce_hanging_sign", "birch_hanging_sign", "jungle_hanging_sign",
        "acacia_hanging_sign", "dark_oak_hanging_sign", "mangrove_hanging_sign", "cherry_hanging_sign", "bamboo_hanging_sign",
        "crimson_hanging_sign", "warped_hanging_sign",
    ],
    "Decoration": [
        "item_frame", "glow_item_frame", "painting", "flower_pot",
        "decorated_pot", "armor_stand", "bell",
        "skeleton_skull", "wither_skeleton_skull", "zombie_head", "player_head", "creeper_head", "dragon_head", "piglin_head",
    ],
    "Sculk": [
        "sculk", "sculk_vein", "sculk_catalyst", "sculk_shrieker",
    ],
    "Miscellaneous": [
        "obsidian", "bedrock", "spawner", "infested_stone", "infested_cobblestone",
        "infested_stone_bricks", "infested_mossy_stone_bricks", "infested_cracked_stone_bricks", "infested_chiseled_stone_bricks",
        "infested_deepslate", "sponge", "wet_sponge", "slime_block", "honey_block", "honeycomb_block",
        "dragon_egg", "beacon", "conduit", "end_portal_frame", "end_gateway",
        "command_block", "chain_command_block", "repeating_command_block",
        "structure_block", "structure_void", "jigsaw", "barrier", "light",
    ],
}


# =============================================================================
# PILLAR BLOCKS
# =============================================================================

# Blocks that use axis-based rotation in their blockstate (logs, pillars, etc.).
# These require a different blockstate format with axis=x/y/z variants.
PILLAR_BLOCKS = {
    # Pillars
    "deepslate", "basalt", "polished_basalt", "quartz_pillar", "purpur_pillar",
    "hay_block", "bone_block", "ochre_froglight", "verdant_froglight", "pearlescent_froglight",
    # Logs
    "oak_log", "spruce_log", "birch_log", "jungle_log", "acacia_log",
    "dark_oak_log", "mangrove_log", "cherry_log", "bamboo_block",
    "stripped_oak_log", "stripped_spruce_log", "stripped_birch_log",
    "stripped_jungle_log", "stripped_acacia_log", "stripped_dark_oak_log",
    "stripped_mangrove_log", "stripped_cherry_log", "stripped_bamboo_block",
    # Wood (bark on all sides)
    "oak_wood", "spruce_wood", "birch_wood", "jungle_wood", "acacia_wood",
    "dark_oak_wood", "mangrove_wood", "cherry_wood",
    "stripped_oak_wood", "stripped_spruce_wood", "stripped_birch_wood",
    "stripped_jungle_wood", "stripped_acacia_wood", "stripped_dark_oak_wood",
    "stripped_mangrove_wood", "stripped_cherry_wood",
    # Nether stems/hyphae
    "crimson_stem", "warped_stem", "stripped_crimson_stem", "stripped_warped_stem",
    "crimson_hyphae", "warped_hyphae", "stripped_crimson_hyphae", "stripped_warped_hyphae",
}


# =============================================================================
# PRESETS
# =============================================================================

# Pre-configured block visibility settings for common use cases.
# Each preset maps to a list of category names that should be visible.
PRESETS = {
    "ore_finder": {
        "name": "Ore Finder",
        "description": "Only ores visible - find diamonds, iron, gold, etc.",
        "categories": ["Ores (Overworld)", "Ores (Nether)", "Metal Blocks"],
    },
    "base_finder": {
        "name": "Base Finder",
        "description": "Find player bases - chests, furnaces, doors visible",
        "categories": ["Storage", "Crafting and Utility", "Doors", "Lighting", "Beds"],
    },
    "cave_explorer": {
        "name": "Cave Explorer",
        "description": "Ores and valuable blocks visible for cave mining",
        "categories": ["Ores (Overworld)", "Ores (Nether)"],
    },
    "nether_xray": {
        "name": "Nether X-Ray",
        "description": "Ancient debris and nether ores only",
        "categories": ["Ores (Nether)"],
    },
    "structure_finder": {
        "name": "Structure Finder",
        "description": "Find structures - doors, chests, spawners visible",
        "categories": ["Storage", "Doors", "Stairs", "Slabs"],
    },
}
