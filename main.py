from config.settings import *
from utils.groupgenerator import GroupGenerator
from utils.json_utils import write_to_json_file

gg = GroupGenerator()
teams = gg.create_empty_teams(number_of_teams)
write_to_json_file(
    gg.distribute_members(teams, hard_skill, soft_skill, general, team_size)
)
