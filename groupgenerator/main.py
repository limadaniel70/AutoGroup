from config.settings import *
from utils.group_generator import GroupGenerator
from utils.json_utils import write_to_json_file

gg = GroupGenerator(number_of_teams, hard_skill, soft_skill, general, team_size)
write_to_json_file(
    gg.teams
)
