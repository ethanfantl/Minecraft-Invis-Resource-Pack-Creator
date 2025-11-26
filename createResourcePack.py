import os
import json
import base64
import shutil

# --- Configuration ---

# verision to pack format map
VERSION_TO_PACK_FORMAT = {
    "1.20.5 - 1.20.6": 26,
    "1.20.3 - 1.20.4": 22,
    "1.20.2": 18,
    "1.19.4": 15,
    "1.19.3": 12,
    "1.19 - 1.19.2": 9,
    "1.18 - 1.18.2": 8,
    "1.17 - 1.17.1": 7,
    "1.16.2 - 1.16.5": 6,
    "1.15 - 1.16.1": 5,
}


# Simple blocks (one model for all states)
SIMPLE_INVISIBLE_BLOCKS = [
    # dirt stones, sand
    "stone", "granite", "diorite", "andesite", "tuff",
    "dirt", "coarse_dirt", "rooted_dirt", "grass_block", "podzol", "mycelium", "farmland",
    "gravel", "clay", "sand", "red_sand",
    "calcite", "smooth_basalt", "amethyst_block", "budding_amethyst",
    "dripstone_block",
    "cobblestone", "mossy_cobblestone", "cobbled_deepslate",
    "sandstone", "chiseled_sandstone", "cut_sandstone", "smooth_sandstone",
    "red_sandstone", "chiseled_red_sandstone", "cut_red_sandstone", "smooth_red_sandstone",
    "stone_bricks", "cracked_stone_bricks", "mossy_stone_bricks", "chiseled_stone_bricks",
    "deepslate_bricks", "cracked_deepslate_bricks", "deepslate_tiles", "cracked_deepslate_tiles",
    "bricks",

    # Ores
    "coal_ore", "copper_ore", "iron_ore", "gold_ore", "lapis_ore",
    "redstone_ore", "diamond_ore", "emerald_ore",
    "deepslate_coal_ore", "deepslate_copper_ore", "deepslate_iron_ore",
    "deepslate_gold_ore", "deepslate_lapis_ore", "deepslate_redstone_ore",
    "deepslate_diamond_ore", "deepslate_emerald_ore",

    # Nether Blocks
    "netherrack", "nether_gold_ore", "nether_quartz_ore", "magma_block",
    "soul_sand", "soul_soil", "blackstone", "gilded_blackstone", "ancient_debris",
    "crimson_nylium", "warped_nylium", "nether_bricks", "red_nether_bricks", "cracked_nether_bricks",
    "chiseled_nether_bricks", "nether_wart_block", "warped_wart_block",

    # End Blocks
    "end_stone", "end_stone_bricks",

    # plants
    "oak_leaves", "spruce_leaves", "birch_leaves", "jungle_leaves", "acacia_leaves", "dark_oak_leaves",
    "mangrove_leaves", "azalea_leaves", "flowering_azalea_leaves", "cherry_leaves",
    "tall_grass", "fern", "large_fern", "dead_bush", "dandelion", "poppy",
    "blue_orchid", "allium", "azure_bluet", "red_tulip", "orange_tulip", "white_tulip", "pink_tulip",
    "oxeye_daisy", "cornflower", "lily_of_the_valley", "wither_rose", "sunflower", "lilac", "rose_bush", "peony",
    "brown_mushroom", "red_mushroom", "crimson_fungus", "warped_fungus", "brown_mushroom_block", "red_mushroom_block", "mushroom_stem",
    "vine", "lily_pad", "sugar_cane", "kelp", "seagrass", "sea_pickle",
    "twisting_vines", "weeping_vines", "glow_lichen", "hanging_roots", "moss_block", "moss_carpet",
    "pumpkin", "carved_pumpkin", "jack_o_lantern", "melon",
    "wheat", "potatoes", "carrots", "beetroots", "nether_wart", "cactus",
    
    # Wood Planks
    "oak_planks", "spruce_planks", "birch_planks", "jungle_planks", "acacia_planks", "dark_oak_planks",
    "mangrove_planks", "cherry_planks", "bamboo_planks", "crimson_planks", "warped_planks",

    # common blocks
    "ice", "packed_ice", "blue_ice", "snow_block", "snow",
    "terracotta", "white_terracotta", "orange_terracotta", "magenta_terracotta", "light_blue_terracotta",
    "yellow_terracotta", "lime_terracotta", "pink_terracotta", "gray_terracotta", "light_gray_terracotta",
    "cyan_terracotta", "purple_terracotta", "blue_terracotta", "brown_terracotta", "green_terracotta",
    "red_terracotta", "black_terracotta",
    "white_wool", "orange_wool", "magenta_wool", "light_blue_wool", "yellow_wool", "lime_wool",
    "pink_wool", "gray_wool", "light_gray_wool", "cyan_wool", "purple_wool", "blue_wool",
    "brown_wool", "green_wool", "red_wool", "black_wool",
    
    # rafting Blocks
    "crafting_table", "furnace", "smoker", "blast_furnace",
    "cartography_table", "fletching_table", "smithing_table", "stonecutter", "grindstone", "loom",
    "enchanting_table", "bookshelf", "lectern", "bell",
    "anvil", "chipped_anvil", "damaged_anvil", "composter", "barrel",
    
    # redstone
    "redstone_wire", "redstone_block", "repeater", "comparator", "observer",
    "detector_rail", "activator_rail", "powered_rail", "rail", "lever",
    "oak_pressure_plate", "spruce_pressure_plate", "birch_pressure_plate", "jungle_pressure_plate",
    "acacia_pressure_plate", "dark_oak_pressure_plate", "mangrove_pressure_plate", "cherry_pressure_plate",
    "stone_pressure_plate", "polished_blackstone_pressure_plate",
    "light_weighted_pressure_plate", "heavy_weighted_pressure_plate",
    "piston", "sticky_piston", "dispenser", "dropper", "hopper",
    "daylight_detector", "target", "tripwire", "tripwire_hook", "tnt",
    
    # Other Decorations
    "torch", "soul_torch", "lantern", "soul_lantern", "campfire", "soul_campfire",
    "item_frame", "glow_item_frame", "painting", "flower_pot",
]

# Pillar-like blocks (have a rotation axis)
PILLAR_INVISIBLE_BLOCKS = [
    "deepslate", "basalt",
    "oak_log", "spruce_log", "birch_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log", "cherry_log",
    "stripped_oak_log", "stripped_spruce_log", "stripped_birch_log", "stripped_jungle_log", "stripped_acacia_log", "stripped_dark_oak_log", "stripped_mangrove_log", "stripped_cherry_log",
    "oak_wood", "spruce_wood", "birch_wood", "jungle_wood", "acacia_wood", "dark_oak_wood", "mangrove_wood", "cherry_wood",
    "stripped_oak_wood", "stripped_spruce_wood", "stripped_birch_wood", "stripped_jungle_wood", "stripped_acacia_wood", "stripped_dark_oak_wood", "stripped_mangrove_wood", "stripped_cherry_wood",
    "crimson_stem", "warped_stem", "stripped_crimson_stem", "stripped_warped_stem",
    "crimson_hyphae", "warped_hyphae", "stripped_crimson_hyphae", "stripped_warped_hyphae",
]

# Other complex blocks (stairs, slabs, etc.)
# We can just define a simple "invisible" model for all their variants.
# This is a "good enough" approximation for an X-ray pack.
# It's better to hide them imperfectly than to leave them visible.
COMPLEX_INVISIBLE_BLOCKS = [
    # All Stairs
    "oak_stairs", "spruce_stairs", "birch_stairs", "jungle_stairs", "acacia_stairs", "dark_oak_stairs", "mangrove_stairs", "cherry_stairs",
    "cobblestone_stairs", "stone_brick_stairs", "sandstone_stairs", "red_sandstone_stairs", "nether_brick_stairs", "brick_stairs",
    "deepslate_brick_stairs", "deepslate_tile_stairs", "polished_blackstone_brick_stairs", "quartz_stairs", "purpur_stairs",

    # All Slabs
    "oak_slab", "spruce_slab", "birch_slab", "jungle_slab", "acacia_slab", "dark_oak_slab", "mangrove_slab", "cherry_slab",
    "cobblestone_slab", "stone_brick_slab", "sandstone_slab", "red_sandstone_slab", "nether_brick_slab", "brick_slab",
    "deepslate_brick_slab", "deepslate_tile_slab", "polished_blackstone_brick_slab", "quartz_slab", "purpur_slab",
    "stone_slab", "smooth_stone_slab", "cut_sandstone_slab", "cut_red_sandstone_slab",

    # All Fences, Gates, and Walls
    "oak_fence", "spruce_fence", "birch_fence", "jungle_fence", "acacia_fence", "dark_oak_fence", "mangrove_fence", "cherry_fence", "nether_brick_fence",
    "oak_fence_gate", "spruce_fence_gate", "birch_fence_gate", "jungle_fence_gate", "acacia_fence_gate", "dark_oak_fence_gate", "mangrove_fence_gate", "cherry_fence_gate",
    "cobblestone_wall", "mossy_cobblestone_wall", "stone_brick_wall", "deepslate_brick_wall", "nether_brick_wall",

    # All Doors and Trapdoors
    "oak_door", "spruce_door", "birch_door", "jungle_door", "acacia_door", "dark_oak_door", "mangrove_door", "cherry_door", "iron_door",
    "oak_trapdoor", "spruce_trapdoor", "birch_trapdoor", "jungle_trapdoor", "acacia_trapdoor", "dark_oak_trapdoor", "mangrove_trapdoor", "cherry_trapdoor", "iron_trapdoor",

    # All Glasses
    "glass", "white_stained_glass", "orange_stained_glass", "magenta_stained_glass", "light_blue_stained_glass", "yellow_stained_glass",
    "lime_stained_glass", "pink_stained_glass", "gray_stained_glass", "light_gray_stained_glass", "cyan_stained_glass",
    "purple_stained_glass", "blue_stained_glass", "brown_stained_glass", "green_stained_glass", "red_stained_glass", "black_stained_glass",
    "glass_pane", "white_stained_glass_pane", "orange_stained_glass_pane", "magenta_stained_glass_pane", "light_blue_stained_glass_pane",
    "yellow_stained_glass_pane", "lime_stained_glass_pane", "pink_stained_glass_pane", "gray_stained_glass_pane", "light_gray_stained_glass_pane",
    "cyan_stained_glass_pane", "purple_stained_glass_pane", "blue_stained_glass_pane", "brown_stained_glass_pane", "green_stained_glass_pane",
    "red_stained_glass_pane", "black_stained_glass_pane",

    # All Beds and Banners
    "white_bed", "orange_bed", "magenta_bed", "light_blue_bed", "yellow_bed", "lime_bed", "pink_bed", "gray_bed",
    "light_gray_bed", "cyan_bed", "purple_bed", "blue_bed", "brown_bed", "green_bed", "red_bed", "black_bed",
    "white_banner", "orange_banner", "magenta_banner", "light_blue_banner", "yellow_banner", "lime_banner", "pink_banner", "gray_banner",
    "light_gray_banner", "cyan_banner", "purple_banner", "blue_banner", "brown_banner", "green_banner", "red_banner", "black_banner",
    
    # All carpets
    "white_carpet", "orange_carpet", "magenta_carpet", "light_blue_carpet", "yellow_carpet", "lime_carpet",
    "pink_carpet", "gray_carpet", "light_gray_carpet", "cyan_carpet", "purple_carpet", "blue_carpet",
    "brown_carpet", "green_carpet", "red_carpet", "black_carpet",
    # All Ores TBF
    # All 
]


# --- Script Logic ---

def create_resource_pack():
    """Main function to drive the resource pack creation."""
    print("--- Minecraft X-Ray Pack Generator ---")

    pack_name = input("Enter a name for your resource pack (e.g., Structure_Xray): ")
    pack_format = select_pack_format()
    if pack_format is None:
        return

    description = f"§b{pack_name.replace('_', ' ')}\n§7Hides most blocks to find structures."

    base_path = pack_name
    assets_path = os.path.join(base_path, "assets", "minecraft")
    blockstates_path = os.path.join(assets_path, "blockstates")
    models_path = os.path.join(assets_path, "models", "block", "xray")
    textures_path = os.path.join(assets_path, "textures", "block", "xray")

    # Clean up previous build if it exists
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    if os.path.exists(f"{base_path}.zip"):
        os.remove(f"{base_path}.zip")

    print(f"\nCreating folder structure at '{base_path}'...")
    os.makedirs(blockstates_path, exist_ok=True)
    os.makedirs(models_path, exist_ok=True)
    os.makedirs(textures_path, exist_ok=True)
    print("... Structure created.")

    write_pack_mcmeta(base_path, pack_format, description)
    create_transparent_texture(textures_path)
    write_invisible_model(models_path)

    print("Generating blockstate files...")
    total_files = generate_blockstates(blockstates_path)
    print(f"... {total_files} blockstate files generated.")

    zip_resource_pack(pack_name)

    print("\n--- Generation Complete! ---")
    print(f"Resource pack ZIP file created: '{pack_name}.zip'")
    print("\nNext Steps:")
    print(f"1. Move the '{pack_name}.zip' file into your Minecraft 'resourcepacks' folder.")
    print("2. Launch Minecraft, go to Options > Resource Packs, and enable it!")

def select_pack_format():
    """Prompts user for Minecraft version and returns pack_format."""
    print("\nPlease select your Minecraft version:")
    version_map = {str(i+1): (v, f) for i, (v, f) in enumerate(VERSION_TO_PACK_FORMAT.items())}
    for key, (version, _) in version_map.items():
        print(f"  [{key}] {version}")

    choice = input("Enter the number for your version: ")
    if choice in version_map:
        version, fmt = version_map[choice]
        print(f"Selected: {version} (pack_format {fmt})")
        return fmt
    else:
        print("Invalid selection. Aborting.")
        return None

def write_pack_mcmeta(base_path, pack_format, description):
    """Writes the pack.mcmeta file."""
    mcmeta_content = {"pack": {"pack_format": pack_format, "description": description}}
    with open(os.path.join(base_path, "pack.mcmeta"), 'w') as f:
        json.dump(mcmeta_content, f, indent=4)
    print("... pack.mcmeta created.")

def create_transparent_texture(textures_path):
    """Creates a 1x1 transparent PNG file from a base64 string."""
    # transparent png
    png_data = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=')
    with open(os.path.join(textures_path, "transparent.png"), 'wb') as f:
        f.write(png_data)
    print("... Transparent texture file created.")

def write_invisible_model(models_path):
    """Writes the invisible model file, referencing the transparent texture."""
    model_content = {
      "ambientocclusion": False,
      "textures": {
        "particle": "block/xray/transparent", # purple black missing texture problem fixed
        "all": "block/xray/transparent"
      },
      "elements": [
        {
          "from": [0, 0, 0],
          "to": [0, 0, 0],
          "faces": {
              "down":  {"uv": [0, 0, 0, 0], "texture": "#all"}
          }
        }
      ]
    }
    with open(os.path.join(models_path, "xray_invisible.json"), 'w') as f:
        json.dump(model_content, f, indent=4)
    print("... Invisible model file updated.")

def generate_blockstates(blockstates_path):
    """Generates all the necessary blockstate json files."""
    total_files = 0
    simple_model = {"variants": {"": {"model": "block/xray/xray_invisible"}}}
    all_simple_blocks = SIMPLE_INVISIBLE_BLOCKS + COMPLEX_INVISIBLE_BLOCKS
    
    for block_name in all_simple_blocks:
        with open(os.path.join(blockstates_path, f"{block_name}.json"), 'w') as f:
            json.dump(simple_model, f, indent=4)
        total_files += 1

    # for pillar blocks
    axis_blockstate = {
        "variants": {
            "axis=y": {"model": "block/xray/xray_invisible"},
            "axis=z": {"model": "block/xray/xray_invisible", "x": 90},
            "axis=x": {"model": "block/xray/xray_invisible", "x": 90, "y": 90}
        }
    }
    for block_name in PILLAR_INVISIBLE_BLOCKS:
        with open(os.path.join(blockstates_path, f"{block_name}.json"), 'w') as f:
            json.dump(axis_blockstate, f, indent=4)
        total_files += 1
        
    return total_files

def zip_resource_pack(pack_name):
    """Creates a properly structured ZIP file and cleans up the source folder."""
    print("Zipping the resource pack...")
    try:
        shutil.make_archive(pack_name, 'zip', pack_name)
        # Clean up the source folder after zipping
        shutil.rmtree(pack_name)
        print("... Zip file created successfully.")
    except Exception as e:
        print(f"An error occurred while zipping the file: {e}")

if __name__ == "__main__":
    create_resource_pack()
