from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game, AutoGameRegister
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

from Options import OptionList
from schema import And, Schema, Optional


@dataclass
class CustomMedleyOptions:
    custom_medleys: CustomMedleys

class CustomMedleyGame(Game):
    name = "Custom Medley"
    platform = KeymastersKeepGamePlatforms.META

    is_adult_only_or_unrated = False

    options_cls = CustomMedleyOptions

    current_medley: str

    custom_medleys: dict

    def __init__(self,
        random = None,
        include_time_consuming_objectives: bool = False,
        include_difficult_objectives: bool = False,
        archipelago_options = None,):
        super().__init__(random, include_time_consuming_objectives, include_difficult_objectives, archipelago_options)
        self.current_medley = "None"
        self.custom_medleys = {}

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        # This will always run before the current game objective group is generated, use it to pick
        # and display the current custom medley

        if not self.custom_medleys:
            # Parse custom medleys here and store on the class for efficiency
            for medley in self.archipelago_options.custom_medleys:
                name = medley["name"]
                games = [AutoGameRegister.games[game] for game in medley["games"] if
                         (not AutoGameRegister.games[game].is_adult_only_or_unrated or self.archipelago_options.include_adult_only_or_unrated_games) and
                         (not AutoGameRegister.games[game].platform in (KeymastersKeepGamePlatforms.PS5, KeymastersKeepGamePlatforms.XSX, KeymastersKeepGamePlatforms.SW))]

                self.custom_medleys[name] = {
                    "games": games,
                    "difficult": medley.get("exclude_difficult", []),
                    "time": medley.get("exclude_time_consuming", []),
                }

        self.current_medley = self.random.choice(list(self.custom_medleys.keys()))

        return [
            GameObjectiveTemplate(
                label=f"Theme: {self.current_medley}",
                data={}
            )
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = []

        medley = self.custom_medleys.get(self.current_medley, None)
        if medley is None:
            _ = self.optional_game_constraint_templates() # this is a hack, but someone will try putting this in a medley
            medley = self.custom_medleys.get(self.current_medley)

        for game in medley["games"]:
            game_obj = game(random=self.random, archipelago_options=self.archipelago_options)
            game_objectives = [objective for objective in game_obj.game_objective_templates()
                          if (not objective.is_difficult or game.game_name_with_platforms() not in medley["difficult"]) and
                          (not objective.is_time_consuming or game.game_name_with_platforms() not in medley["time"])
                          ]
            for objective in game_objectives:
                # check if any data keys are in the name, lol
                for key in list(objective.data.keys()):
                    if key in game.name:
                        data = objective.data.pop(key)
                        objective.label = objective.label.replace(key, f"{key}1")
                        key = f"{key}1"
                        objective.data[key] = data

                objective.label = f"{game.name}: {objective.label}"

            objectives.extend(game_objectives)

        return objectives


class CustomMedleys(OptionList):
    """
    Definition of custom medleys. Format is as follows
    - name: "Medley Name"
      games: ["Game 1", "Game 2"]
      exclude_difficult: ["Game 1"] (*optional)
      exclude_time_consuming: ["Game 2"] (*optional)
    """

    display_name = "Custom Medleys"
    schema = Schema([
        {
            "name": And(str, len),
            "games": [And(str, lambda game: game in AutoGameRegister.games)],
            Optional("exclude_difficult"): [And(str, lambda game: game in AutoGameRegister.games)],
            Optional("exclude_time_consuming"): [And(str, lambda game: game in AutoGameRegister.games)],
        }
    ])

