"""
Minecraft X-Ray Resource Pack Generator
========================================

Creates Minecraft resource packs that make blocks invisible (x-ray effect).
Users can select which Minecraft version to target and which blocks to keep visible.

Usage:
    python xray_pack_generator.py

The generated .zip file can be placed directly in Minecraft's resourcepacks folder.
"""

import os
import json
import base64
import shutil
from typing import Optional

from block_data import (
    VERSION_TO_PACK_FORMAT,
    BLOCK_CATEGORIES,
    PILLAR_BLOCKS,
    PRESETS,
)


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def clear_screen() -> None:
    """Clear the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header() -> None:
    """Print the program header."""
    print("=" * 60)
    print("  MINECRAFT X-RAY RESOURCE PACK GENERATOR")
    print("=" * 60)
    print()


def print_separator() -> None:
    """Print a visual separator line."""
    print("-" * 50)


def get_all_blocks() -> set[str]:
    """Return a set of all block IDs from all categories."""
    all_blocks = set()
    for blocks in BLOCK_CATEGORIES.values():
        all_blocks.update(blocks)
    return all_blocks


def count_blocks_in_category(category: str, visible_blocks: set[str]) -> tuple[int, int]:
    """
    Count visible and total blocks in a category.

    Returns:
        Tuple of (visible_count, total_count)
    """
    blocks = BLOCK_CATEGORIES[category]
    visible_count = len(set(blocks) & visible_blocks)
    return visible_count, len(blocks)


def parse_number_selection(input_string: str, max_value: int) -> list[int]:
    """
    Parse user input for number selections.

    Supports formats like:
        - "1,2,3" - comma-separated values
        - "1 2 3" - space-separated values
        - "1-5" - ranges
        - "1,3-5,7" - mixed

    Args:
        input_string: User input to parse
        max_value: Maximum valid selection (1-indexed)

    Returns:
        List of 0-indexed values

    Raises:
        ValueError: If input cannot be parsed
    """
    indices = []
    parts = input_string.replace(',', ' ').split()

    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            for i in range(int(start), int(end) + 1):
                if 1 <= i <= max_value:
                    indices.append(i - 1)
        else:
            i = int(part)
            if 1 <= i <= max_value:
                indices.append(i - 1)

    return indices


# =============================================================================
# USER INTERFACE: Version Selection
# =============================================================================

def prompt_version_selection() -> Optional[tuple[str, int]]:
    """
    Display version selection menu and get user choice.

    Returns:
        Tuple of (version_string, pack_format) or None if cancelled
    """
    print("\nSELECT MINECRAFT VERSION")
    print_separator()

    versions = list(VERSION_TO_PACK_FORMAT.items())
    for index, (version, pack_format) in enumerate(versions, start=1):
        print(f"  [{index:2}] {version} (pack format {pack_format})")

    print()

    try:
        choice = input("Enter version number (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            return None

        selected_index = int(choice) - 1
        if 0 <= selected_index < len(versions):
            selected_version = versions[selected_index]
            print(f"\n-> Selected: {selected_version[0]}")
            return selected_version
        else:
            print("ERROR: Invalid selection.")
            return None

    except ValueError:
        print("ERROR: Please enter a valid number.")
        return None


# =============================================================================
# USER INTERFACE: Block Selection
# =============================================================================

def prompt_block_selection() -> Optional[set[str]]:
    """
    Main menu for selecting which blocks should remain visible.

    By default, all blocks are invisible. Users select categories/blocks
    to mark as VISIBLE (not affected by x-ray).

    Returns:
        Set of block IDs that should remain visible, or None if cancelled
    """
    visible_blocks: set[str] = set()

    while True:
        clear_screen()
        print_header()
        print("SELECT BLOCKS TO KEEP VISIBLE")
        print_separator()
        print("By default, ALL blocks will be invisible (x-ray mode).")
        print("Select categories to mark blocks as VISIBLE.")
        print()

        # Display categories with visibility status
        categories = list(BLOCK_CATEGORIES.keys())
        for index, category in enumerate(categories, start=1):
            visible_count, total_count = count_blocks_in_category(category, visible_blocks)

            if visible_count == total_count:
                status = "[ALL VISIBLE]"
            elif visible_count > 0:
                status = f"[{visible_count}/{total_count} visible]"
            else:
                status = "(all invisible)"

            print(f"  [{index:2}] {category:<30} {status}")

        print()
        print_separator()
        print("  [A]  Make ALL blocks visible (disable x-ray)")
        print("  [C]  Clear all (reset to all invisible)")
        print("  [P]  Show preset options")
        print("  [D]  Done - Generate resource pack")
        print("  [Q]  Quit without generating")
        print()

        choice = input("Enter choice: ").strip().lower()

        if choice == 'q':
            return None

        if choice == 'd':
            return visible_blocks

        if choice == 'a':
            visible_blocks = get_all_blocks()
            print("\n-> All blocks set to visible!")
            input("Press Enter to continue...")

        elif choice == 'c':
            visible_blocks.clear()
            print("\n-> All blocks set to invisible!")
            input("Press Enter to continue...")

        elif choice == 'p':
            preset_result = prompt_preset_selection()
            if preset_result is not None:
                visible_blocks = preset_result

        else:
            # Try to parse as category number
            try:
                category_index = int(choice) - 1
                if 0 <= category_index < len(categories):
                    category = categories[category_index]
                    prompt_blocks_in_category(category, visible_blocks)
            except ValueError:
                print("ERROR: Invalid choice. Press Enter to continue...")
                input()

    return visible_blocks


def prompt_preset_selection() -> Optional[set[str]]:
    """
    Display preset options and apply user selection.

    Returns:
        Set of visible blocks from the preset, or None if cancelled
    """
    clear_screen()
    print_header()
    print("PRESET CONFIGURATIONS")
    print_separator()
    print()

    preset_keys = list(PRESETS.keys())
    for index, key in enumerate(preset_keys, start=1):
        preset = PRESETS[key]
        print(f"  [{index}] {preset['name']}")
        print(f"      {preset['description']}")
        print()

    print("  [B] Back to category selection")
    print()

    choice = input("Select preset: ").strip()

    if choice.lower() == 'b':
        return None

    try:
        preset_index = int(choice) - 1
        if 0 <= preset_index < len(preset_keys):
            preset_key = preset_keys[preset_index]
            preset = PRESETS[preset_key]

            # Collect all blocks from preset categories
            visible = set()
            for category_name in preset["categories"]:
                if category_name in BLOCK_CATEGORIES:
                    visible.update(BLOCK_CATEGORIES[category_name])

            print(f"\n-> Applied preset: {preset['name']}")
            input("Press Enter to continue...")
            return visible

    except ValueError:
        pass

    return None


def prompt_blocks_in_category(category: str, visible_blocks: set[str]) -> None:
    """
    Display individual blocks within a category for selection.

    Modifies visible_blocks in place based on user selections.

    Args:
        category: Category name to display
        visible_blocks: Set to modify with user selections
    """
    blocks = BLOCK_CATEGORIES[category]

    while True:
        clear_screen()
        print_header()
        print(f"CATEGORY: {category.upper()}")
        print_separator()

        # Display blocks with visibility status
        for index, block in enumerate(blocks, start=1):
            if block in visible_blocks:
                status = "[VISIBLE]"
            else:
                status = ""
            print(f"  [{index:3}] {block:<40} {status}")

        print()
        print_separator()
        print("  [A] Toggle ALL blocks in this category")
        print("  [V] Make all VISIBLE")
        print("  [I] Make all INVISIBLE")
        print("  [B] Back to categories")
        print()
        print("Enter block number(s) to toggle. Examples: 1,2,3 or 1-5 or 1 3 5")
        print()

        choice = input("Choice: ").strip().lower()

        if choice == 'b':
            break

        if choice == 'a':
            # Toggle all: if all visible, make invisible; otherwise make visible
            all_visible = all(block in visible_blocks for block in blocks)
            if all_visible:
                visible_blocks.difference_update(blocks)
            else:
                visible_blocks.update(blocks)

        elif choice == 'v':
            visible_blocks.update(blocks)

        elif choice == 'i':
            visible_blocks.difference_update(blocks)

        else:
            # Parse block number selections
            try:
                indices = parse_number_selection(choice, len(blocks))
                for idx in indices:
                    block = blocks[idx]
                    if block in visible_blocks:
                        visible_blocks.discard(block)
                    else:
                        visible_blocks.add(block)
            except (ValueError, IndexError):
                print("ERROR: Invalid selection. Press Enter to continue...")
                input()


# =============================================================================
# RESOURCE PACK GENERATION
# =============================================================================

def generate_resource_pack(
    pack_name: str,
    version_string: str,
    pack_format: int,
    visible_blocks: set[str]
) -> tuple[int, int]:
    """
    Generate the resource pack files and create a ZIP archive.

    Args:
        pack_name: Name for the resource pack (used for folder and zip name)
        version_string: Minecraft version string for description
        pack_format: Resource pack format number
        visible_blocks: Set of block IDs that should NOT be made invisible

    Returns:
        Tuple of (invisible_block_count, visible_block_count)
    """
    # Define file paths
    base_path = pack_name
    assets_path = os.path.join(base_path, "assets", "minecraft")
    blockstates_path = os.path.join(assets_path, "blockstates")
    models_path = os.path.join(assets_path, "models", "block", "xray")
    textures_path = os.path.join(assets_path, "textures", "block", "xray")

    # Clean up any previous build
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    if os.path.exists(f"{base_path}.zip"):
        os.remove(f"{base_path}.zip")

    # Create directory structure
    print(f"\nCreating folder structure: '{base_path}'...")
    os.makedirs(blockstates_path, exist_ok=True)
    os.makedirs(models_path, exist_ok=True)
    os.makedirs(textures_path, exist_ok=True)

    # Write pack.mcmeta
    write_pack_metadata(base_path, pack_format, pack_name, version_string)
    print("  - Created pack.mcmeta")

    # Create transparent texture
    write_transparent_texture(textures_path)
    print("  - Created transparent texture")

    # Create invisible model
    write_invisible_model(models_path)
    print("  - Created invisible block model")

    # Generate blockstate files
    print("\nGenerating blockstate files...")
    invisible_count, visible_count = write_blockstate_files(blockstates_path, visible_blocks)
    print(f"  - {invisible_count} blocks set to invisible")
    print(f"  - {visible_count} blocks kept visible")

    # Create ZIP archive
    print("\nCreating ZIP archive...")
    shutil.make_archive(pack_name, 'zip', pack_name)
    shutil.rmtree(pack_name)
    print(f"  - Created {pack_name}.zip")

    return invisible_count, visible_count


def write_pack_metadata(base_path: str, pack_format: int, pack_name: str, version_string: str) -> None:
    """Write the pack.mcmeta file."""
    description = f"{pack_name.replace('_', ' ')} - X-Ray pack for {version_string}"

    mcmeta_content = {
        "pack": {
            "pack_format": pack_format,
            "description": description
        }
    }

    filepath = os.path.join(base_path, "pack.mcmeta")
    with open(filepath, 'w') as file:
        json.dump(mcmeta_content, file, indent=4)


def write_transparent_texture(textures_path: str) -> None:
    """Create a 1x1 transparent PNG texture file."""
    # Base64-encoded 1x1 transparent PNG
    transparent_png_base64 = (
        'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAA'
        'C0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='
    )
    png_data = base64.b64decode(transparent_png_base64)

    filepath = os.path.join(textures_path, "transparent.png")
    with open(filepath, 'wb') as file:
        file.write(png_data)


def write_invisible_model(models_path: str) -> None:
    """Create the invisible block model JSON file."""
    # This model has zero-size elements, making the block invisible
    # while still having a valid texture reference (prevents purple/black errors)
    model_content = {
        "ambientocclusion": False,
        "textures": {
            "particle": "block/xray/transparent",
            "all": "block/xray/transparent"
        },
        "elements": [
            {
                "from": [0, 0, 0],
                "to": [0, 0, 0],
                "faces": {
                    "down": {"uv": [0, 0, 0, 0], "texture": "#all"}
                }
            }
        ]
    }

    filepath = os.path.join(models_path, "xray_invisible.json")
    with open(filepath, 'w') as file:
        json.dump(model_content, file, indent=4)


def write_blockstate_files(blockstates_path: str, visible_blocks: set[str]) -> tuple[int, int]:
    """
    Generate blockstate JSON files for all invisible blocks.

    Args:
        blockstates_path: Directory to write blockstate files
        visible_blocks: Blocks that should NOT have invisible blockstates

    Returns:
        Tuple of (invisible_count, visible_count)
    """
    # Blockstate for simple blocks (no rotation)
    simple_blockstate = {
        "variants": {
            "": {"model": "block/xray/xray_invisible"}
        }
    }

    # Blockstate for pillar/axis blocks (logs, etc.)
    pillar_blockstate = {
        "variants": {
            "axis=y": {"model": "block/xray/xray_invisible"},
            "axis=z": {"model": "block/xray/xray_invisible", "x": 90},
            "axis=x": {"model": "block/xray/xray_invisible", "x": 90, "y": 90}
        }
    }

    invisible_count = 0
    visible_count = 0

    # Process all blocks in all categories
    for category, blocks in BLOCK_CATEGORIES.items():
        for block in blocks:
            if block in visible_blocks:
                # Skip visible blocks - they use default textures
                visible_count += 1
            else:
                # Create invisible blockstate
                if block in PILLAR_BLOCKS:
                    blockstate_data = pillar_blockstate
                else:
                    blockstate_data = simple_blockstate

                filepath = os.path.join(blockstates_path, f"{block}.json")
                with open(filepath, 'w') as file:
                    json.dump(blockstate_data, file, indent=4)

                invisible_count += 1

    return invisible_count, visible_count


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main() -> None:
    """Main program entry point."""
    clear_screen()
    print_header()

    # Step 1: Get pack name
    pack_name = input("Enter a name for your resource pack: ").strip()
    if not pack_name:
        pack_name = "XRay_Pack"
    pack_name = pack_name.replace(' ', '_')

    # Step 2: Select Minecraft version
    version_result = prompt_version_selection()
    if version_result is None:
        print("\nExiting.")
        return

    version_string, pack_format = version_result

    # Step 3: Select which blocks to keep visible
    visible_blocks = prompt_block_selection()
    if visible_blocks is None:
        print("\nExiting.")
        return

    # Step 4: Show summary and confirm
    clear_screen()
    print_header()
    print("SUMMARY")
    print_separator()
    print(f"  Pack Name:         {pack_name}")
    print(f"  Minecraft Version: {version_string}")
    print(f"  Pack Format:       {pack_format}")
    print(f"  Visible Blocks:    {len(visible_blocks)}")

    total_blocks = sum(len(blocks) for blocks in BLOCK_CATEGORIES.values())
    invisible_count = total_blocks - len(visible_blocks)
    print(f"  Invisible Blocks:  {invisible_count}")
    print()

    confirm = input("Generate resource pack? (Y/n): ").strip().lower()
    if confirm not in ('', 'y', 'yes'):
        print("\nCancelled.")
        return

    # Step 5: Generate the pack
    generate_resource_pack(pack_name, version_string, pack_format, visible_blocks)

    # Step 6: Show completion message
    print()
    print("=" * 60)
    print("  RESOURCE PACK GENERATED SUCCESSFULLY")
    print("=" * 60)
    print()
    print("Next Steps:")
    print(f"  1. Move '{pack_name}.zip' to your Minecraft resourcepacks folder")
    print("  2. Launch Minecraft -> Options -> Resource Packs")
    print("  3. Enable the pack and enjoy!")
    print()


if __name__ == "__main__":
    main()
