from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MonsterHunterGenerationsUltimateArchipelagoOptions:
    monster_hunter_generations_ultimate_include_rank_dependent_monsters: \
        MonsterHunterGenerationsUltimateIncludeRankDependentMonsters
    monster_hunter_generations_ultimate_include_dlc: MonsterHunterGenerationsUltimateIncludeDLC


class MonsterHunterGenerationsUltimateGame(Game):
    name = "Monster Hunter Generations Ultimate"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = [
        KeymastersKeepGamePlatforms._3DS
    ]

    is_adult_only_or_unrated = False

    options_cls = MonsterHunterGenerationsUltimateArchipelagoOptions

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
            GameObjectiveTemplate(
                label="Use STYLE style",
                data={"STYLE": (self.styles, 1)}
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
        ]

        return templates

    @property
    def include_rank_dependent_monsters(self) -> bool:
        return bool(self.archipelago_options.monster_hunter_generations_ultimate_include_rank_dependent_monsters.value)

    @property
    def include_dlc(self):
        return bool(self.archipelago_options.monster_hunter_generations_ultimate_include_dlc.value)

    @staticmethod
    def monsters_base() -> List[str]:
        return [
            "Agnaktor",
            "Ahtal-Ka",
            "Arzuros",
            "Astalos",
            "Barioth",
            "Barroth",
            "Basarios",
            "Blangonga",
            "Bloodbath Diablos",
            "Boltreaver Astalos"
            "Brachydios",
            "Bulldrome",
            "Cephadrome",
            "Congalala",
            "Crystalbeard Uragaan",
            "Daimyo Hermitaur",
            "Deadeye Yian Garuga",
            "Deviljho",
            "Diablos",
            "Dreadking Rathalos",
            "Dreadqueen Rathian",
            "Drilltusk Tetsucabra",
            "Duramboros",
            "Elderfrost Gammoth",
            "Furious Rajang",
            "Gammoth",
            "Gendrome",
            "Giadrome",
            "Glavenus",
            "Gore Magala",
            "Gravios",
            "Great Maccao",
            "Grimclaw Tigrex",
            "Gypceros",
            "Hellblade Glavenus",
            "Iodrome",
            "Kecha Wacha",
            "Khezu",
            "Kirin",
            "Lagiacrus",
            "Lagombi",
            "Lao-Shan Lung",
            "Lavasioth",
            "Malfestio",
            "Mizutsune",
            "Najarala",
            "Nakarkos",
            "Nargacuga",
            "Nerscylla",
            "Nibelsnarf",
            "Nightcloak Malfestio",
            "Plesioth",
            "Rajang",
            "Rathalos",
            "Rathian",
            "Redhelm Arzuros",
            "Royal Ludroth",
            "Rustrazor Ceanataur",
            "Seltas",
            "Seltas Queen",
            "Seregios",
            "Shagaru Magala",
            "Shogun Ceanataur",
            "Silverwind Ceanataur",
            "Snowbaron Lagombi",
            "Soulseer Mizutsune",
            "Stonefist Hermitaur",
            "Tetsucabra",
            "Thunderlord Zinogre",
            "Tigrex",
            "Uragaan",
            "Valstrax",
            "Velocidrome",
            "Volvidon",
            "Yian Garuga",
            "Yian Kut-Ku",
            "Zamtrios",
            "Zinogre",
        ]

    @staticmethod
    def monsters_rank() -> List[str]:
        return [
            "Chaotic Gore Magala",
            "Teostra",
            "Chameleos",
            "Kushala Daora",
            "Gold Rathian",
            "Silver Rathalos",
            "Furious Rajang",
            "Savage Deviljho",
            "Raging Brachydios",
            "Akantor",
            "Ukanlos",
            "Amatsu",
            "Alatreon",
            "Fatalis",
            "Crimson Fatalis",
            "Old Fatalis"
        ]

    def monsters(self) -> List[str]:
        monsters: List[str] = self.monsters_base()

        if self.include_rank_dependent_monsters:
            monsters.extend(self.monsters_rank())

        return sorted(monsters)

    def capturable(self) -> List[str]:
        monsters = self.monsters()

        non_capture = [
            "Ahtal Ka",
            "Akantor",
            "Alatreon",
            "Amatsu",
            "Kirin",
            "Shagaru Magala",
            "Kushala Daora",
            "Rusted Kushala Daora",
            "Teostra",
            "Chameleos",
            "Lao-Shan Lung",
            "Nakarkos",
            "Valstrax",
            "Fatalis",
            "Crimson Fatalis",
            "Old Fatalis"
        ]

        return sorted(set(monsters).difference(non_capture))

    def variants(self) -> List[str]:
        variants = [
            "Rare Species",
            "Variant Species",
            "Deviant",
            "Hyper",
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
            "Prowler",
        ]

    @functools.cached_property
    def stages_base(self) -> List[str]:
        return [
            "Jurassic Frontier",
            "Verdant Hills",
            "Arctic Ridge",
            "Misty Peaks",
            "Dunes",
            "Deserted Island",
            "Marshlands",
            "Volcano",
            "Ancestral Steppe",
            "Volcanic Hollow",
            "Primal Forest",
            "Frozen Seaway",
            "Desert",
            "Jungle",
            "Ruined Pinnacle",
            "Sanctuary",
            "Forlorn Arena",
            "Sacred Pinnacle",
            "Ingle Isle",
            "Polar Field",
            "Wyvern's End",
            "Castle Schrade",
            "Fortress",
            "Forlorn Citadel",
            "Arena",
            "V. Slayground",
            "F. Slayground",  # TODO: find out wth F and V stand for
        ]

    def stages(self) -> List[str]:
        stages: List[str] = self.stages_base[:]

        return sorted(stages)

    @functools.cached_property
    def drops_base(self) -> List[str]:
        return [
            "Wyvern Gem",
            "Lrg Wyvern Gem",
            "Bird Wyvern Gem",
            "Fey Wyvern Gem",
            "S. Queen Extract",
            "D.S. Queen Concentrate",
            "Ahtal Ka Alluring Gem",
            "Giant Beak",
            "Splendid Beak",
            "Rajang Tail",
            "Rajang Hardhorn",
            "Rajang Nerve",
            "Gammoth Ice Orb",
            "Gammoth Pallium",
            "Lagiacrus Plate",
            "Lagiacrus Sapphire",
            "Lagiacrus Mantle",
            "Mizutsune Plate",
            "Mizutsune Water Orb",
            "Mizutsune Pallium",
            "Chilling Beak",
            "Heart-stopping Beak",
            "Deviljho Gem",
            "Deviljho Crook",
            "Uragaan Marrow",
            "Uragaan Ruby",
            "Uragaan Pallium",
            "Duram Sacrum",
            "Brach Marrow",
            "Brach Gem",
            "Brach Pallium",
            "Glavenus Plate",
            "Glavenus Fire Orb",
            "Glavenus Pallium",
            "Nargacuga Marrow",
            "Narga Medulla",
            "Nargacuga Mantle",
            "Rathian Plate",
            "Rathian Ruby",
            "Rathian Mantle",
            "Rathalos Plate",
            "Rathalos Ruby",
            "Rathalos Mantle",
            "Rath Marrow",
            "Rath Medulla",
            "Basarios Pallium",
            "Gravios Pallium",
            "Khezu Special Cut",
            "Tigrex Scalp",
            "Tigrex Maw",
            "Tigrex Mantle",
            "Seregios Dissenter",
            "Seregios Lens",
            "Astalos Plate",
            "Astalos Electrogem",
            "Astalos Mantle",
            "Blos Medulla",
            "Akantor Gem",
            "Ukanlos Gem",
            "Gore Magala Plate",
            "Gore Magala Nyctgem",
            "Gore Magala Mantle",
            "Zinogre Plate",
            "Zinogre Jasper",
            "Zinogre Skymerald",
            "S. Magala Plate",
            "S. Magala Phosgem",
            "S. Magala Mantle",
            "Red Dragon Mindstone",
            "Ruby Dragon Mindstone",
            "Daora Gem",
            "Chameleos Gem",
            "Teostra Gem",
            "Lao-Shan Mantle",
        ]

    @functools.cached_property
    def drops_rank_base(self) -> List[str]:
        return [
            "Lrg Elder Dragon Gem",
            "Contrary Scale",
            "Rajang Heart",
            "Ghoulish Gold Gorer",
            "Immortal Reactor",
            "Conquest Sphere",
            "Ukanlos Stone",
            "Azure Dragongem",
            "Azure Dragonsphire",
            "Heavenly Dragongem",
            "Heavenly Dragonsphire",
            "Nakarkos Soul Orb",
            "Nakarkos SecretSoulOrb",

        ]


    def drops(self) -> List[str]:
        drops: List[str] = self.drops_base[:]

        if self.include_rank_dependent_monsters:
            drops.extend(self.drops_rank_base)

        return sorted(drops)

    @functools.cached_property
    def tails_base(self) -> List[str]:
        return [
            "Garuga Tail",
            "Garuga Lash",
            "R.Ludroth Tail",
            "R.Ludroth Lash",
            "Lagiacrus Tail",
            "Lagiacrus Flail",
            "Agnaktor Tail",
            "Barroth Tail",
            "Barroth Lash",
            "Brach Tail",
            "Brach Lash",
            "Duram Tailcase+",
            "Duram Hardtail",
            "Nargacuga Tail",
            "Nargacuga Lash",
            "Barioth Tail",
            "Barioth Lash",
            "Rathalos Tail",
            "Rathalos Lash",
            "S. Rathalos Tail",
            "Zinogre Tail",
            "Zinogre Lash",
            "Astalos Scissortail",
            "Astalos Scissortailblade",
            "Mizutsune Tail",
            "Purple Mizutsune Tail",
            "Soulseer Tail",
            "Glavenus Tail",
            "Glavenus Tailedge",
            "Tigrex Tail",
            "Tigrex Lash",
            "Diablos Tailcase",
            "Diablos Tailcase+",
            "Gore Magala Tail",
            "Gore Magala Lash",
            "S. Magala Tail",
            "S. Magala Lash",
            "Deviljho Tail",
            "Deviljho Flail",
            "Daora Tail",
            "Daora Lash",
            "Teostra Tail",
            "Teostra Lash",
            "Chameleos Tail",
            "Chameleos Lash",
            "Akantor Tail",
            "Akantor Flail",
            "Ukanlos Tail",
            "Ukanlos Flail",
            "Alatreon Tail",
            "Alatreo Diretail",
            "Amatsu Tail",
            "Amatsu Stormtail",
            "Valstrax Tail",
            "Valstrax Helixtail",

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

    @staticmethod
    def styles() -> List[str]:
        return [
            "Guild",
            "Aerial",
            "Striker",
            "Adept",
            "Valor",
            "Alchemy"
        ]

    def arenas(self) -> List[str]:
        arenas = [
            "Grudge Match: Malfestio",
            "Grudge Match: Khezu",
            "Grudge Match: Najarala",
            "Grudge Match: Rathalos",
            "Grudge Match: Kecha Wacha",
            "Grudge Match: Plesioth",
            "Grudge Match: Brachydios",
            "Grudge Match: Barioth",
            "Grudge Match: Yian Garuga",
            "Grudge Match: Uragaan",
            "Grudge Match: Seregios",
            "Grudge Match: Great Maccao",
            "Grudge Match: Gypceros",
            "Grudge Match: Bird Wyverns",
            "Grudge Match: Barroth",
            "Grudge Match: Tetsucabra",
            "Grudge Match: Congalala",
        ]

        if self.include_dlc:
            arenas.extend([
                "XX Trials: Dreadqueen",
                "XX Trials: Thunderlord",
                "XX Trials: Silverwind",
                "XX Trials: Dreadking",
                "XX Trials: Grimclaw",
                "XX Trials: Gravios",
                "XX Trials: Elderfrost",
                "XX Trials: Hunt-a-thon I",
                "XX Trials: Hunt-a-thon II",
                "XX Trials: Stonefist",
                "XX Trials: Drilltusk",
                "XX Trials: Redhelm",
                "XX Trials: Deadeye",
                "XX Trials: Snowbaron",
                "XX Trials: Hunt-a-thon III",
                "Event: Slay a Mizutsune",
                "Event: Slay a Glavenus",
                "Event: Slay an Astalos",
                "Event: Slay a Gammoth",
                "Event: Slay a Lagiacrus",
                "Event: Hunt-a-thon 1",
                "Event: Hunt-a-thon 2",
                "Event: Hunt-a-thon 3",
                "Event: Slay a Zinogre",
                "Event: Slay a Gore Magala",
                "Event: Slay a Tigrex",
                "Event: Slay a Rathalos",
                "Event: Slay a Nargacuga",
                "Event: Hunt-a-thon 4",
                "XX Trials: Rathalos",
                "XX Trials: Tigrex",
                "XX Trials: Nargacuga",
                "XX Trials: Zinogre",
                "XX Trials: Brachydios",
                "XX Trials: Hunt-a-thon IV",
                "Event: Slay a Volvidon",
                "Event: Slay a Royal Ludroth",
                "Event: Slay a Lagombi",
                "Event: Slay a Yian Kut-Ku",
                "Event: Slay an Arzuros",
                "Event: Hunt-a-thon 5"
            ])
        return arenas


class MonsterHunterGenerationsUltimateIncludeRankDependentMonsters(DefaultOnToggle):
    """
    Indicates whether to include Monster Hunter Generations Ultimate rank-dependent monsters when generating objectives.
    """

    display_name = "Monster Hunter Generations Ultimate Include Rank Dependent Monsters"


class MonsterHunterGenerationsUltimateIncludeDLC(DefaultOnToggle):
    """
    Indicates whether to include Monster Hunter Generations Ultimate DLC quests when generating objectives
    """

    display_name = "Monster Hunter Generations Ultimate Include DLC"
