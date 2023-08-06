import re
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field, root_validator

from .base import BaseCharacter, GenshinModel

__all__ = [
    "HyakuninIkkiCharacter",
    "HyakuninIkkiSkill",
    "HyakuninIkkiBattle",
    "HyakuninIkkiChallenge",
    "HyakuninIkki",
    "LabyrinthWarriorsCharacter",
    "LabyrinthWarriorsRune",
    "LabyrinthWarriorsChallenge",
    "LabyrinthWarriors",
    "ChineseActivity",
    "Activities",
]

# ---------------------------------------------------------
# Hyakunin Ikki:


class HyakuninIkkiCharacter(BaseCharacter):
    """A Hyakunin Ikki character"""

    level: int
    trial: bool = Field(galias="is_trail_avatar")


class HyakuninIkkiSkill(GenshinModel):
    """A Hyakunin Ikki skill"""

    id: int
    name: str
    icon: str
    description: str = Field(galias="desc")


class HyakuninIkkiBattle(GenshinModel):
    """A Hyakunin Ikki battle"""

    characters: List[HyakuninIkkiCharacter] = Field(galias="avatars")
    skills: List[HyakuninIkkiSkill] = Field(galias="skills")


class HyakuninIkkiChallenge(GenshinModel):
    """A Hyakunin Ikki challenge"""

    id: int = Field(galias="challenge_id")
    name: str = Field(galias="challenge_name")
    difficulty: int
    multiplier: int = Field(galias="score_multiple")
    score: int = Field(galias="max_score")
    medal_icon: str = Field(galias="heraldry_icon")

    battles: List[HyakuninIkkiBattle] = Field(galias="lineups")

    @property
    def medal(self) -> str:
        match = re.search(r"heraldry_(\w+)\.png", self.medal_icon)
        return match.group(1) if match else ""


class HyakuninIkki(GenshinModel):
    """A Hyakunin Ikki event"""

    challenges: List[HyakuninIkkiChallenge] = Field(galias="records")


# ---------------------------------------------------------
# Labyrinth Warriors:


class LabyrinthWarriorsCharacter(BaseCharacter):
    """A Labyrinth Warriors character"""

    level: int


class LabyrinthWarriorsRune(GenshinModel):
    """A Labyrinth Warriors rune"""

    id: int
    icon: str
    name: str
    description: str = Field(galias="desc")
    element: str


class LabyrinthWarriorsChallenge(GenshinModel):
    """A Labyrinth Warriors challenge"""

    id: int = Field(galias="challenge_id")
    name: str = Field(galias="challenge_name")
    passed: bool = Field(galias="is_passed")
    level: int = Field(galias="settled_level")

    main_characters: List[LabyrinthWarriorsCharacter] = Field(galias="main_avatars")
    support_characters: List[LabyrinthWarriorsCharacter] = Field(galias="support_avatars")
    runes: List[LabyrinthWarriorsRune]


class LabyrinthWarriors(GenshinModel):
    """A Labyrinth Warriors event"""

    challenges: List[LabyrinthWarriorsChallenge] = Field(galias="records")


# ---------------------------------------------------------
# Energy Amplifier Fruition


class EnergyAmplifierCharacter(BaseCharacter):
    """An energy amplifier character"""

    level: int


class EnergyAmplifierCriteria(GenshinModel):
    """An energy amplifier challenge criteria"""

    id: int
    description: str = Field(galias="desc")
    score: int


class EnergyAmplifierBuff(GenshinModel):
    """An energy amplifier challenge buff"""

    id: int
    name: str
    quality: int
    description: str = Field(galias="desc")
    energy: int


class EnergyAmplifierChallenge(GenshinModel):
    """An energy amplifier challenge"""

    id: int = Field(galias="challenge_id")
    name: str = Field(galias="challenge_name")
    characters: List[EnergyAmplifierCharacter] = Field(galias="avatars")
    energy: int
    difficulty: int
    high_score: int = Field(galias="max_score")
    criteria: List[EnergyAmplifierCriteria] = Field(galias="limit_conditions")
    multiplier: int = Field(galias="score_multiple")
    buffs: List[EnergyAmplifierBuff]


class EnergyAmplifier(GenshinModel):
    """An energy amplifier event"""

    start_time: datetime
    end_time: datetime
    challenges: List[EnergyAmplifierChallenge] = Field(alias="records")


# ---------------------------------------------------------
# A study in potions:


class PotionCharacter(BaseCharacter):
    """A study in potions character"""

    level: int
    trial: bool = Field(galias="is_trial")


class PotionPotion(GenshinModel):
    """A study in potions potion"""

    id: int
    name: str
    quality: int
    quality_icon: str = Field(galias="icon")
    mark_icon: str = Field(galias="cornor_mark")
    description: str = Field(galias="desc")


class PotionStage(GenshinModel):
    """A study in potions stage"""

    name: str = Field(galias="level_name")
    score: int
    difficulty: int
    difficulty_factor: int = Field(galias="factor")
    characters: List[PotionCharacter] = Field(galias="avatars")
    potions: List[PotionPotion] = Field(galias="buffs")


class PotionChallenge(GenshinModel):
    """A study in potions challenge"""

    name: str = Field(galias="stage_name")
    score: int = Field(galias="stage_score")
    finished: bool

    stages: List[PotionStage] = Field(galias="levels")


class Potions(GenshinModel):
    """A study in potions event"""

    challenges: List[PotionChallenge] = Field(galias="records")


# ---------------------------------------------------------
# Chinese activities:


class ChineseActivity(GenshinModel):
    """An arbitrary activty for chinese events"""

    start_time: datetime
    end_time: datetime
    total_score: int
    total_times: int
    records: List[Any]


# ---------------------------------------------------------
# Activities:


class Activities(GenshinModel):
    """A collection of genshin activities"""

    hyakunin_ikki: Optional[HyakuninIkki] = Field(None, gslug="sumo")
    labyrinth_warriors: Optional[LabyrinthWarriors] = Field(None, gslug="rogue")
    energy_amplifier: Optional[EnergyAmplifier] = Field(None, gslug="channeller_slab_copy")
    potions: Optional[Potions] = Field(None, gslug="potion")

    @root_validator(pre=True)
    def __flatten_activities(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if not values.get("activities"):
            return values

        slugs = {
            field.field_info.extra["gslug"]: name
            for name, field in cls.__fields__.items()
            if field.field_info.extra.get("gslug")
        }

        for activity in values["activities"]:
            for name, value in activity.items():
                if "exists_data" not in value:
                    continue

                name = slugs.get(name, name)
                values[name] = value if value["exists_data"] else None

        return values
