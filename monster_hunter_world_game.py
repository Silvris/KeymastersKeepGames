from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MonsterHunterWorldArchipelagoOptions:
    monster_hunter_world_iceborne: MonsterHunterWorldIceborne
    monster_hunter_world_include_rank: MonsterHunterWorldIncludeRankMonsters
    monster_hunter_world_include_events: MonsterHunterWorldIncludeDLC


class MonsterHunterWorldGame(Game):
    name = "Monster Hunter World"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.XONE,
    ]

    is_adult_only_or_unrated = False

    options_cls = MonsterHunterWorldArchipelagoOptions

    @property
    def include_rank_dependent_monsters(self) -> bool:
        return bool(self.archipelago_options.monster_hunter_world_include_rank.value)

    @property
    def iceborne(self):
        return bool(self.archipelago_options.monster_hunter_world_iceborne.value)

    @property
    def include_dlc(self):
        return bool(self.archipelago_options.monster_hunter_world_include_events.value)

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Use an element, or status, that the monster resists",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Hunt as an investigation (if applicable)",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Only run 5 or fewer Decorations",
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
            GameObjectiveTemplate(
                label="Don't use mantles/hunting tools",
                data=dict()
            )
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
            GameObjectiveTemplate(
                label="Complete a MONSTER investigation",
                data={
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

        if self.iceborne:
            templates.extend([
                GameObjectiveTemplate(
                    label="Hunt NUMBER monsters in the Guiding Lands",
                    data={
                        "NUMBER": (lambda: list(range(2, 7)), 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2
                )
            ])

        return templates

    def monsters_base(self) -> List[str]:
        monsters = [
            "Ancient Leshen",
            "Anjanath",
            "Azure Rathalos",
            "Barroth",
            "Bazelgeuse",
            "Behemoth",
            "Black Diablos",
            "Deviljho",
            "Diablos",
            "Dodogama",
            "Great Girros",
            "Great Jagras",
            "Jyuratodus",
            "Kirin",
            "Kulu-Ya-Ku",
            "Kushala Daora",
            "Lavasioth",
            "Legiana",
            "Leshen",
            "Lunastra",
            "Nergigante",
            "Odogaron",
            "Paolumu",
            "Pink Rathian",
            "Pukei-Pukei",
            "Radobaan",
            "Rathalos",
            "Rathian",
            "Teostra",
            "Tobi Kadachi",
            "Tzitzi-Ya-Ku",
            "Uragaan",
            "Vaal Hazak",
            "Xeno'jiiva",
            "Zorah Magdaros"
        ]

        if self.include_dlc:
            monsters.append("Kulve Taroth")

        if self.iceborne:
            monsters.extend([
                "Acidic Glavenus",
                "Alatreon",
                "Banbaro",
                "Barioth",
                "Beotodus",
                "Blackveil Vaal Hazak",
                "Brachydios",
                "Brute Tigrex",
                "Coral Pukei-Pukei",
                "Ebony Odogaron",
                "Fatalis",
                "Frostfang Barioth",
                "Fulgur Anjanath",
                "Furious Rajang",
                "Glavenus",
                "Namielle",
                "Nargacuga",
                "Nightshade Paolumu",
                "Raging Brachydios",
                "Rajang",
                "Savage Deviljho",
                "Seething Bazelgeuse",
                "Shara Ishvalda",
                "Shrieking Legiana",
                "Stygian Zinogre",
                "Tigrex",
                "Velkhana",
                "Viper Tobi Kadachi",
                "Zinogre"
            ])

            if self.include_rank_dependent_monsters:
                monsters.extend([
                    "Gold Rathian",
                    "Silver Rathalos",
                    "Ruiner Nergigante",
                    "Scarred Yian Garuga",
                    "Yian Garuga",
                ])

            if self.include_dlc:
                monsters.extend([
                    "Safi'jiiva",
                ])
        return monsters

    def monsters(self) -> List[str]:
        monsters: List[str] = self.monsters_base()

        return sorted(monsters)

    def capturable(self) -> List[str]:
        monsters = self.monsters()

        non_capture = [
            "Alatreon",
            "Ancient Leshen",
            "Behemoth",
            "Blackveil Vaal Hazak",
            "Fatalis",
            "Kulve Taroth",
            "Kushala Daora",
            "Leshen",
            "Lunastra",
            "Namielle",
            "Nergigante",
            "Raging Brachydios",
            "Ruiner Nergigante",
            "Safi'jiiva",
            "Shara Ishvalda",
            "Teostra",
            "Vaal Hazak",
            "Velkhana",
            "Xeno'jiiva",
            "Zorah Magdaros",
        ]

        return sorted(set(monsters).difference(non_capture))

    def variants(self) -> List[str]:
        variants = [
            "Subspecies",
            "Rare Species",
            "Variant Species",
            "Tempered",
        ]

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
            "Charge Blade",
            "Insect Glaive",
            "Light Bowgun",
            "Heavy Bowgun",
            "Bow",
        ]

    @functools.cached_property
    def stages_base(self) -> List[str]:
        return [
            "Ancient Forest",
            "Wildspire Wastes",
            "Coral Highlands",
            "Rotten Vale",
            "Elder's Recess",
            "Confluence of Fates",
            "Everstream",
            "Arena",
            "Special Arena",
        ]

    @functools.cached_property
    def stages_g(self) -> List[str]:
        return [
            "Hoarfrost Reach",
            "Guiding Lands",
            "Origin Isle",
            "Castle Schrade",
            "Seliana Supply Cache",
        ]

    def stages(self) -> List[str]:
        stages: List[str] = self.stages_base[:]

        if self.include_dlc:
            stages.append("Caverns of El Dorado")

        if self.iceborne:
            stages.extend(self.stages_g)


        return sorted(stages)

    @functools.cached_property
    def drops_base(self) -> List[str]:
        return [
            "Bird Wyvern Gem",
            "Wyvern Gem",
            "Anjanath Plate",
            "Anjanath Gem",
            "Rathian Plate",
            "Rathian Ruby",
            "Legiana Plate",
            "Legiana Gem",
            "Odogaron Plate",
            "Odogaron Gem",
            "Rathalos Plate",
            "Rathalos Ruby",
            "Diablos Marrow",
            "Uragaan Marrow",
            "Uragaan Ruby",
            "Bazelgeuse Gem",
            "Deviljho Gem",
            "Zorah Magdaros Gem",
            "Nergigante Gem",
            "Teostra Gem",
            "Lunastra Gem",
            "Daora Gem",
            "Vaal Hazak Gem",
            "Xeno'jiiva Gem",
        ]

    @functools.cached_property
    def drops_g_dlc(self) -> List[str]:
        return [
            "Fey Wyvern Gem",
            "Large Wyvern Gem",
            "Large Elder Dragon Gem",
            "Anjanath Mantle",
            "Fulgur Anjanath Mantle",
            "Rathian Mantle",
            "Legiana Mantle",
            "Odogaron Mantle",
            "Ebony Odogaron Mantle",
            "Rathalos Mantle",
            "Blos Medulla",
            "Uragaan Pallium",
            "Nargacuga Mantle",
            "Tigrex Mantle",
            "Glavenus Mantle",
            "Brachydios Pallium",
            "Immortal Reactor",
            "Zinogre Skymerald",
            "Stygian Zinogre Skymerald",
            "Bazelgeuse Mantle",
            "Deviljho Crook",
            "Ghoulish Gold Gorer",
            "Rajang Heart",
            "Velkhana Crystal",
            "Shara Ishvalda Gem",
            "Azure Dragonsphire",

        ]

    def drops(self) -> List[str]:
        drops: List[str] = self.drops_base[:]

        if self.include_dlc:
            drops.append("Kulve Taroth Golden Glimstone")

        if self.iceborne:
            drops.extend(self.drops_g_dlc)

            if self.include_dlc:
                drops.extend([
                    "Zionium Crystal",
                    "Golden Dragonsphire"
                ])

        return sorted(drops)

    @functools.cached_property
    def tails_base(self) -> List[str]:
        return [
            "Pukei-Pukei Tail",
            "Barroth Tail",
            "Anjanath Tail",
            "Great Girros Tail",
            "Odogaron Tail",
            "Rathalos Tail",
            "Azure Rathalos Tail",
            "Dodogama Tail",
            "Bazelgeuse Tail",
            "Deviljho Tail",
            "Nergigante Tail",
            "Teostra Tail",
            "Lunastra Tail",
            "Daora Tail",
            "Vaal Hazak Tail",
            "Xeno'jiiva Tail",
            "Behemoth Tail",
        ]

    @functools.cached_property
    def tails_g_dlc(self) -> List[str]:
        return [
            "Pukei-Pukei Lash",
            "Barroth Lash",
            "Anjanath Lash",
            "Great Girros Lash",
            "Odogaron Lash",
            "Rathalos Lash",
            "Azure Rathalos Lash",
            "Dodogama Lash",
            "Bazelgeuse Flail",
            "Deviljho Flail",
            "Nergigante Flail",
            "Teostra Lash",
            "Lunasta Lash",
            "Daora Lash",
            "Vaal Hazak Flail",
            "Coral Pukei-Pukei Lash",
            "Banbaro Lash",
            "Fulgur Anjanath Lash",
            "Ebony Odogaron Lash",
            "Barioth Lash",
            "Nargacuga Lash",
            "Tigrex Lash",
            "Glavenus Tailedge",
            "Acidic Glavenus Tailedge",
            "Brachydios Lash",
            "Zinogre Lash",
            "Stygian Zinogre Lash",
            "Velkhana Lash",
            "Namielle Lash",
            "Alatreon Diretail",
        ]

    @functools.cached_property
    def tails_rank_g(self) -> List[str]:
        return [
            "Garuga Lash",
            "Silver Rathalos Lash",
        ]

    def tails(self) -> List[str]:
        tails: List[str] = self.tails_base[:]

        if self.iceborne:
            tails.extend(self.tails_g_dlc)

            if self.include_rank_dependent_monsters:
                tails.extend(self.tails_rank_g)

            if self.include_dlc:
                tails.append("Safi'jiiva Lash")
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
            f"Arena Quest 0{i}" for i in range(1, 10)
        ]

        if self.iceborne:
            arenas.extend([f"Arena Master Quest 0{i}" for i in range(1, 8)])

        return arenas


class MonsterHunterWorldIncludeRankMonsters(DefaultOnToggle):
    """
    Indicates whether to include Monster Hunter World rank-exclusive monsters when generating objectives.
    """

    display_name = "Monster Hunter World Include MR-Locked Monsters"


class MonsterHunterWorldIceborne(DefaultOnToggle):
    """
    Indicates whether to include Iceborne-specific objectives when generating objectives.
    """

    display_name = "Monster Hunter World Iceborne"


class MonsterHunterWorldIncludeDLC(DefaultOnToggle):
    """
    Indicates whether to include Monster Hunter World siege monsters when generating objectives.
    """

    display_name = "Monster Hunter World Include Siege Monsters"
