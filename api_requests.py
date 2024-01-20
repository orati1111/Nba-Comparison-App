from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints.playercareerstats import PerMode36

LST_OF_STATS = ["GP","MIN","FG_PCT","FG3_PCT","FT_PCT","REB","AST","STL","BLK","TOV","PTS"]
LST_OF_PERCENT_STATS = ["FG_PCT","FG3_PCT","FT_PCT"]
PLAYERS_STATS = players.get_active_players()
LST_OF_ACTIVE_PLAYERS = sorted([dict["full_name"] for dict in PLAYERS_STATS])

def get_player_id(player1,player2):
    player1_common_info = players.find_players_by_full_name(player1)
    player2_common_info = players.find_players_by_full_name(player2)
    try :
        return player1_common_info[0]["id"] , player2_common_info[0]["id"]
    except IndexError:
        return None,None

def request_season_stats(player1_id,player2_id):
    player1_stats = None
    player2_stats = None

    player1_stats = playercareerstats.PlayerCareerStats(player_id=player1_id,per_mode36=PerMode36.per_game).get_normalized_dict()
    player2_stats = playercareerstats.PlayerCareerStats(player_id=player2_id,per_mode36=PerMode36.per_game).get_normalized_dict()
    
    # Player's last season is stored at the last element of the list, hence the -1 index
    player1_stats = player1_stats["SeasonTotalsRegularSeason"][-1]
    player2_stats = player2_stats["SeasonTotalsRegularSeason"][-1]

    return player1_stats,player2_stats

def organize_stats(player1_stats:dict,player2_stats:dict):
    for key in player1_stats.copy().keys():
        if key not in LST_OF_STATS:
            player1_stats.pop(key)
            player2_stats.pop(key)
            
    for key,value in player1_stats.items():
        if key in LST_OF_PERCENT_STATS:
            player1_stats[key] = f"{value*100:.2f}%"

    for key,value in player2_stats.items():
        if key in LST_OF_PERCENT_STATS:
            player2_stats[key] = f"{value*100:.2f}%"
            
    return player1_stats,player2_stats

def api_operations(player1_name,player2_name):
    player1_id,player2_id = get_player_id(player1_name,player2_name)
    if not (player1_id and player2_id):
        return None,None
    else:
        player1_stats,player2_stats = request_season_stats(player1_id,player2_id)
        return organize_stats(player1_stats,player2_stats)
