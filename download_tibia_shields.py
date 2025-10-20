#!/usr/bin/env python3

from __future__ import annotations

import shutil
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

SHIELDS = {
    "Adamant Shield": "https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif",
    "Alicorn Quiver": "https://www.tibiawiki.com.br/images/7/71/Alicorn_Quiver.gif",
    "Amazon Shield": "https://www.tibiawiki.com.br/images/f/ff/Amazon_Shield.gif",
    "Ancient Shield": "https://www.tibiawiki.com.br/images/a/ab/Ancient_Shield.gif",
    "Aurora's Collection": "https://www.tibiawiki.com.br/images/b/b5/Aurora%27s_Collection.gif",
    "Aylie": "https://www.tibiawiki.com.br/images/a/a7/Aylie.gif",
    "Battle Shield": "https://www.tibiawiki.com.br/images/e/e2/Battle_Shield.gif",
    "Biscuit Barrier": "https://www.tibiawiki.com.br/images/1/12/Biscuit_Barrier.gif",
    "Black Shield": "https://www.tibiawiki.com.br/images/e/e7/Black_Shield.gif",
    "Blessed Shield": "https://www.tibiawiki.com.br/images/1/1f/Blessed_Shield.gif",
    "Blue Quiver": "https://www.tibiawiki.com.br/images/6/63/Blue_Quiver.gif",
    "Bone Shield": "https://www.tibiawiki.com.br/images/b/be/Bone_Shield.gif",
    "Bonelord Shield": "https://www.tibiawiki.com.br/images/6/6a/Bonelord_Shield.gif",
    "Brass Shield": "https://www.tibiawiki.com.br/images/c/c3/Brass_Shield.gif",
    "Broken Wooden Shield": "https://www.tibiawiki.com.br/images/2/2f/Broken_Wooden_Shield.gif",
    "Candy-Coated Quiver": "https://www.tibiawiki.com.br/images/9/92/Candy-Coated_Quiver.gif",
    "Carapace Shield": "https://www.tibiawiki.com.br/images/5/54/Carapace_Shield.gif",
    "Castle Shield": "https://www.tibiawiki.com.br/images/8/87/Castle_Shield.gif",
    "Copper Shield": "https://www.tibiawiki.com.br/images/c/cc/Copper_Shield.gif",
    "Crown Shield": "https://www.tibiawiki.com.br/images/4/41/Crown_Shield.gif",
    "Dark Shield": "https://www.tibiawiki.com.br/images/6/64/Dark_Shield.gif",
    "Death Gaze": "https://www.tibiawiki.com.br/images/2/2c/Death_Gaze.gif",
    "Demon Shield": "https://www.tibiawiki.com.br/images/4/4f/Demon_Shield.gif",
    "Dragon Shield": "https://www.tibiawiki.com.br/images/1/13/Dragon_Shield.gif",
    "Dwarven Shield": "https://www.tibiawiki.com.br/images/5/58/Dwarven_Shield.gif",
    "Eagle Shield": "https://www.tibiawiki.com.br/images/2/21/Eagle_Shield.gif",
    "Ectoplasmic Shield": "https://www.tibiawiki.com.br/images/7/78/Ectoplasmic_Shield.gif",
    "Eerie Song Book": "https://www.tibiawiki.com.br/images/f/fe/Eerie_Song_Book.gif",
    "Eldritch Quiver": "https://www.tibiawiki.com.br/images/9/94/Eldritch_Quiver.gif",
    "Eldritch Shield": "https://www.tibiawiki.com.br/images/5/5b/Eldritch_Shield.gif",
    "Falcon Escutcheon": "https://www.tibiawiki.com.br/images/e/ef/Falcon_Escutcheon.gif",
    "Falcon Shield": "https://www.tibiawiki.com.br/images/2/29/Falcon_Shield.gif",
    "Fiery Rainbow Shield": "https://www.tibiawiki.com.br/images/d/da/Fiery_Rainbow_Shield.gif",
    "Gnome Shield": "https://www.tibiawiki.com.br/images/1/1c/Gnome_Shield.gif",
    "Golden Blessed Shield": "https://www.tibiawiki.com.br/images/c/c2/Golden_Blessed_Shield.gif",
    "Great Shield": "https://www.tibiawiki.com.br/images/4/43/Great_Shield.gif",
    "Guardian Shield": "https://www.tibiawiki.com.br/images/4/4e/Guardian_Shield.gif",
    "Haunted Mirror Piece": "https://www.tibiawiki.com.br/images/6/6e/Haunted_Mirror_Piece.gif",
    "Icy Rainbow Shield": "https://www.tibiawiki.com.br/images/5/5f/Icy_Rainbow_Shield.gif",
    "Journal Shield": "https://www.tibiawiki.com.br/images/0/05/Journal_Shield.gif",
    "Jungle Quiver": "https://www.tibiawiki.com.br/images/c/c9/Jungle_Quiver.gif",
    "Lion Shield": "https://www.tibiawiki.com.br/images/b/bc/Lion_Shield.gif",
    "Mastermind Shield": "https://www.tibiawiki.com.br/images/1/10/Mastermind_Shield.gif",
    "Mathmaster Shield": "https://www.tibiawiki.com.br/images/8/89/Mathmaster_Shield.gif",
    "Meat Shield": "https://www.tibiawiki.com.br/images/5/5c/Meat_Shield.gif",
    "Medusa Shield": "https://www.tibiawiki.com.br/images/f/fe/Medusa_Shield.gif",
    "Mino Shield": "https://www.tibiawiki.com.br/images/b/bb/Mino_Shield.gif",
    "Morshabaal's Mask": "https://www.tibiawiki.com.br/images/a/a0/Morshabaal%27s_Mask.gif",
    "Naga Quiver": "https://www.tibiawiki.com.br/images/7/78/Naga_Quiver.gif",
    "Necromancer Shield": "https://www.tibiawiki.com.br/images/3/33/Necromancer_Shield.gif",
    "Nightmare Shield": "https://www.tibiawiki.com.br/images/d/d0/Nightmare_Shield.gif",
    "Norse Shield": "https://www.tibiawiki.com.br/images/f/f0/Norse_Shield.gif",
    "Ornamented Shield": "https://www.tibiawiki.com.br/images/f/fb/Ornamented_Shield.gif",
    "Ornate Shield": "https://www.tibiawiki.com.br/images/4/41/Ornate_Shield.gif",
    "Painted Gourd Rattle": "https://www.tibiawiki.com.br/images/7/7e/Painted_Gourd_Rattle.gif",
    "Phoenix Shield": "https://www.tibiawiki.com.br/images/e/ef/Phoenix_Shield.gif",
    "Plate Shield": "https://www.tibiawiki.com.br/images/8/86/Plate_Shield.gif",
    "Prismatic Shield": "https://www.tibiawiki.com.br/images/b/b7/Prismatic_Shield.gif",
    "Quiver": "https://www.tibiawiki.com.br/images/2/2e/Quiver.gif",
    "Rainbow Shield": "https://www.tibiawiki.com.br/images/3/38/Rainbow_Shield.gif",
    "Red Quiver": "https://www.tibiawiki.com.br/images/f/f8/Red_Quiver.gif",
    "Rift Shield": "https://www.tibiawiki.com.br/images/1/12/Rift_Shield.gif",
    "Rose Shield": "https://www.tibiawiki.com.br/images/e/e3/Rose_Shield.gif",
    "Runic Ice Shield": "https://www.tibiawiki.com.br/images/7/72/Runic_Ice_Shield.gif",
    "Salamander Shield": "https://www.tibiawiki.com.br/images/4/47/Salamander_Shield.gif",
    "Scarab Shield": "https://www.tibiawiki.com.br/images/d/d1/Scarab_Shield.gif",
    "Sentinel Shield": "https://www.tibiawiki.com.br/images/2/22/Sentinel_Shield.gif",
    "Shield of Care": "https://www.tibiawiki.com.br/images/4/4a/Shield_of_Care.gif",
    "Shield of Corruption": "https://www.tibiawiki.com.br/images/2/2b/Shield_of_Corruption.gif",
    "Shield of Destiny": "https://www.tibiawiki.com.br/images/5/5e/Shield_of_Destiny.gif",
    "Shield of Endless Search": "https://www.tibiawiki.com.br/images/5/5c/Shield_of_Endless_Search.gif",
    "Shield of Honour": "https://www.tibiawiki.com.br/images/b/be/Shield_of_Honour.gif",
    "Shield of the White Knight": "https://www.tibiawiki.com.br/images/a/a5/Shield_of_the_White_Knight.gif",
    "Soulbastion": "https://www.tibiawiki.com.br/images/b/bd/Soulbastion.gif",
    "Sparking Rainbow Shield": "https://www.tibiawiki.com.br/images/7/73/Sparking_Rainbow_Shield.gif",
    "Spike Shield": "https://www.tibiawiki.com.br/images/6/6b/Spike_Shield.gif",
    "Steel Shield": "https://www.tibiawiki.com.br/images/1/17/Steel_Shield.gif",
    "Strange Good Night Songs": "https://www.tibiawiki.com.br/images/0/0e/Strange_Good_Night_Songs.gif",
    "Studded Shield": "https://www.tibiawiki.com.br/images/5/5f/Studded_Shield.gif",
    "Tempest Shield": "https://www.tibiawiki.com.br/images/0/00/Tempest_Shield.gif",
    "Terran Rainbow Shield": "https://www.tibiawiki.com.br/images/4/45/Terran_Rainbow_Shield.gif",
    "The Dragon Spirit": "https://www.tibiawiki.com.br/images/7/75/The_Dragon_Spirit.gif",
    "Tortoise Shield": "https://www.tibiawiki.com.br/images/b/bc/Tortoise_Shield.gif",
    "Tower Shield": "https://www.tibiawiki.com.br/images/4/4b/Tower_Shield.gif",
    "Tusk Shield": "https://www.tibiawiki.com.br/images/e/e0/Tusk_Shield.gif",
    "Vampire Shield": "https://www.tibiawiki.com.br/images/5/59/Vampire_Shield.gif",
    "Viking Shield": "https://www.tibiawiki.com.br/images/1/1c/Viking_Shield.gif",
    "Warrior's Shield": "https://www.tibiawiki.com.br/images/5/51/Warrior%27s_Shield.gif",
    "Wooden Shield": "https://www.tibiawiki.com.br/images/2/2d/Wooden_Shield.gif",
    "Demon Powered Shield": "https://www.tibiawiki.com.br/images/4/40/Demon_Powered_Shield.gif",
    "Mercenary Shield": "https://www.tibiawiki.com.br/images/f/f8/Mercenary_Shield.gif",
}


def download_shield(name: str, url: str, target_dir: Path) -> None:
    file_path = target_dir / f"{name}.gif"
    if file_path.exists():
        print(f"Skipping {name} (already exists)")
        return
    try:
        with urlopen(url) as response, file_path.open("wb") as out_file:
            shutil.copyfileobj(response, out_file)
    except (HTTPError, URLError) as exc:
        print(f"Failed to download {name}: {exc}")
    else:
        print(f"Downloaded {name} -> {file_path}")


def main() -> None:
    target_dir = Path(__file__).resolve().parent / "TIBIA_SHIELDS"
    target_dir.mkdir(parents=True, exist_ok=True)
    for name, url in SHIELDS.items():
        download_shield(name, url, target_dir)


if __name__ == "__main__":
    main()
