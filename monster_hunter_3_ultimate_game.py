from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MonsterHunter3UltimateArchipelagoOptions:
    monster_hunter_3_ultimate_aged_text_monsters: MonsterHunter3UltimateIncludeRankMonsters
    monster_hunter_3_ultimate_include_dlcs: MonsterHunter3UltimateIncludeDLC


class MonsterHunter3UltimateGame(Game):
    name = "Monster Hunter 3 Ultimate"
    platform = KeymastersKeepGamePlatforms.WIIU

    platforms_other = [
        KeymastersKeepGamePlatforms._3DS
    ]

    is_adult_only_or_unrated = False

    options_cls = MonsterHunter3UltimateArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Use an element, or status, that the monster resists",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Clear 2 Subquests",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Only run 8 or fewer Decorations",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Run a full set of MONSTER Armor",
                data={
                    "MONSTER": (self.monsters, 1)
                },
            ),
            GameObjectiveTemplate(
                label="Run a MONSTER Weapon (if possible)",
                data={
                    "MONSTER": (self.monsters, 1)
                },
            ),
            GameObjectiveTemplate(
                label="Your weapon type must be rarity level 4 or lower",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Slay MONSTER",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Slay MONSTER using the following weapon: WEAPON",
                data={
                    "MONSTER": (self.monsters, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Hunt MONSTER with its own Weapon",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Hunt MONSTER within TIMER",
                data={
                    "MONSTER": (self.monsters, 1),
                    "TIMER": (self.timers, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Capture MONSTER",
                data={
                    "MONSTER": (self.capturable, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Capture MONSTER using the following weapon: WEAPON",
                data={
                    "MONSTER": (self.capturable, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Carve the following Tail: TAIL",
                data={
                    "TAIL": (self.tails, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Break 2 MONSTER parts",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Hunt 2 monsters in the STAGE",
                data={
                    "STAGE": (self.stages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Hunt 3 monsters in the STAGE",
                data={
                    "STAGE": (self.stages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Hunt 3 VARIANT monsters",
                data={
                    "VARIANT": (self.variants, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Hunt MONSTER without dying",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Wielding the WEAPON, obtain the following Drop: DROP",
                data={
                    "WEAPON": (self.weapons, 1),
                    "DROP": (self.drops, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Obtain the following Drops as Broken Part Rewards (when possible): DROPS",
                data={
                    "DROPS": (self.drops, 2),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

        return templates

    @property
    def include_rank_dependent_monsters(self) -> bool:
        return bool(self.archipelago_options.monster_hunter_3_ultimate_aged_text_monsters.value)

    @property
    def include_dlc(self):
        return bool(self.archipelago_options.monster_hunter_3_ultimate_include_dlcs.value)

    @staticmethod
    def monsters_base() -> List[str]:
        return [
            "Great Jaggi",
            "Great Baggi",
            "Great Wroggi",
            "Arzuros",
            "Lagombi",
            "Volvidon",
            "Qurupeco",
            "Crimson Qurupeco",
            "Barroth",
            "Jade Barroth",
            "Uragaan",
            "Steel Uragaan",
            "Duramboros",
            "Rust Duramboros",
            "Rathian",
            "Pink Rathian",
            "Rathalos",
            "Azure Rathalos",
            "Diablos",
            "Black Diablos",
            "Gigginox",
            "Baleful Gigginox",
            "Barioth",
            "Sand Barioth",
            "Royal Ludroth",
            "Purple Ludroth",
            "Gobul",
            "Nibelsnarf",
            "Lagiacrus",
            "Ivory Lagiacrus",
            "Agnaktor",
            "Glacial Agnaktor",
            "Nargacuga",
            "Green Nargacuga",
            "Zinogre",
            "Stygian Zinogre",
            "Plesioth",
            "Green Plesioth",
            "Brachydios",
            "Ceadeus",
            "Goldbeard Ceadeus",
            "Deviljho",
            "Savage Deviljho",
            "Hallowed Jhen Mohran",
            "Alatreon",
            "Dire Miralis"
        ]

    def monsters_rank(self) -> List[str]:
        monsters = [
            "Gold Rathian",
            "Silver Rathalos",
            "Abyssal Lagiacrus",
            "Lucent Nargacuga",
        ]

        return monsters

    def monsters_g_dlc(self) -> List[str]:
        monsters = [
            "Jhen Mohran",
        ]

        return monsters

    def monsters(self) -> List[str]:
        monsters: List[str] = self.monsters_base()

        if self.include_rank_dependent_monsters:
            monsters.extend(self.monsters_rank())

        if self.include_dlc:
            monsters.extend(self.monsters_g_dlc())

        return sorted(monsters)

    def capturable(self) -> List[str]:
        monsters = self.monsters()

        non_capture = [
            "Ceadeus",
            "Goldbeard Ceadeus",
            "Jhen Mohran",
            "Hallowed Jhen Mohran",
            "Alatreon",
            "Dire Miralis",
        ]

        return sorted(set(monsters).difference(non_capture))

    def variants(self) -> List[str]:
        variants = [
            "Subspecies",
            "Variant Species",
        ]
        if self.include_rank_dependent_monsters:
            variants.append("Rare Species")

        return variants

    @staticmethod
    def weapons() -> List[str]:
        return [
            "Great Sword",
            "Long Sword",
            "Sword and Shield",
            "Dual Blades",
            "Hammer",
            "Hunting Horn",
            "Lance",
            "Gunlance",
            "Switch Axe",
            "Light Bowgun",
            "Heavy Bowgun",
            "Bow",
        ]

    @functools.cached_property
    def stages_base(self) -> List[str]:
        return [
            "Deserted Island/Moga Woods",
            "Sandy Plains",
            "Flooded Forest",
            "Tundra",
            "Volcano",
            "Misty Peaks",
            "Great Desert",
            "Ruins",
            "Tower",
            "Tainted Sea",
            "Sacred Land",
            "Land Arena",
            "Water Arena",
        ]

    def stages(self) -> List[str]:
        stages: List[str] = self.stages_base[:]

        return sorted(stages)

    @functools.cached_property
    def drops_base(self) -> List[str]:
        return [
            "Bird Wyvern Gem",
            "Fey Wyvern Gem",
            "Wyvern Stone",
            "Lrg Wyvern Stone",
            "Uragaan Marrow",
            "Uragaan Ruby",
            "Uragaan Pallium",
            "Duram Sacrum",
            "Durambolite",
            "Rathian Plate",
            "Rathian Ruby",
            "Rathian Mantle",
            "Rathalos Plate",
            "Rathalos Ruby",
            "Rathalos Mantle",
            "Rath Marrow",
            "Rath Medulla",
            "Lagiacrus Plate",
            "Lagia Sapphire",
            "Lagiacrus Mantle",
            "Narga Medulla",
            "Nargacuga Mantle",
            "Zinogre Jasper",
            "Zin Skymerald",
            "S.Zin Skymerald",
            "Brachydios Gem",
            "Brach Pallium",
            "Deep Dragongem",
            "Dark Dragongem",
            "Deviljho Gem",
            "Deviljho Crook",
            "Earth Dragongem",
            "Earth Drgnsphire",
            "Azure Dragongem",
            "Azure Drgnsphire",
            "Dire Dragongem",
        ]

    @functools.cached_property
    def drops_rank(self):
        return [
            "A.Lagi Dynamo",
            "Cloudy Moonshard",
        ]

    def drops(self) -> List[str]:
        drops: List[str] = self.drops_base[:]

        if self.include_rank_dependent_monsters:
            drops.extend(self.drops_rank)

        return sorted(drops)

    @functools.cached_property
    def tails_base(self) -> List[str]:
        return [
            "R. Ludroth Tail",
            "R. Ludroth Lash",
            "Barroth Tail",
            "Barroth Lash",
            "J. Barroth Tail",
            "J. Barroth Lash",
            "Rathalos Tail",
            "Rathalos Lash",
            "A. Rathalos Tail",
            "A. Rathalos Lash",
            "Lagiacrus Tail",
            "Lagiacrus Flail",
            "Barioth Tail",
            "Barioth Lash",
            "S. Barioth Tail",
            "S. Barioth Lash",
            "Diablos Tailcase",
            "Diablos Hardtail",
            "Agnaktor Tail",
            "G. Agnak Tail",
            "Brachydios Tail",
            "Duram Tailcase",
            "Duram Tailcase+",
            "Duram Hardtail",
            "R. Duram Hardtail",
            "Zinogre Tail",
            "Zinogre Lash",
            "S. Zinogre Lash",
            "Nargacuga Tail",
            "Nargacuga Lash"
            "Deviljho Tail",
            "Deviljho Flail",
            "Alatreon Tail",
            "Alatreo Diretail"
        ]

    @functools.cached_property
    def tails_rank_base(self) -> List[str]:
        return [
            "S. Rathalos Lash",
        ]

    def tails(self) -> List[str]:
        tails: List[str] = self.tails_base[:]

        if self.include_rank_dependent_monsters:
            tails.extend(self.tails_rank_base)

        return sorted(tails)

    @staticmethod
    def timers() -> List[str]:
        return [
            "30 Minutes",
            "25 Minutes",
            "20 Minutes",
        ]

    def arenas(self) -> List[str]:
        arenas = [
            "Grudge Match: Lagombi",
            "Grudge Match: Purple Ludroth",
            "Grudge Match: Barioth",
            "Grudge Match: Plesioth",
            "Grudge Match: Gigginox",
            "Grudge Match: Pink Rathian",
            "Grudge Match: Rathalos",
            "Grudge Match: Nargacuga",
            "Grudge Match: Lagiacrus",
            "Grudge Match: R. Duramboros",
            "Grudge Match: Sea Power",
            "Grudge Match: S. Zinogre",
        ]

        if self.include_dlc:
            arenas.extend([f"Challenge Quest {i}" for i in range(1, 11)])

        return arenas


class MonsterHunter3UltimateIncludeRankMonsters(DefaultOnToggle):
    """
    Indicates whether to include Monster Hunter 3 Ultimate rank-dependent monsters when generating objectives.
    """

    display_name = "Monster Hunter 3 Ultimate Include Rank Monsters"


class MonsterHunter3UltimateIncludeDLC(DefaultOnToggle):
    """
    Indicates whether to include Monster Hunter 3 Ultimate DLC-exclusive monsters when generating objectives.
    Only G-Rank DLC-exclusive monsters are considered.
    """

    display_name = "Monster Hunter 3 Ultimate Include DLC Monsters"
