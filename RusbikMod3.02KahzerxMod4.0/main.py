import requests

from RusbikMod import models as r_models, query as r_query
from KahzerxMod import models as k_models, query as k_query


def get_uuid(player_name: str) -> str:
    r = requests.get(f"https://playerdb.co/api/player/minecraft/{player_name}")
    res = r.json()
    if res.get("success"):
        return res.get("data").get("player").get("id")
    else:
        return ""


if __name__ == '__main__':
    dims = {
        "Overworld": 0,
        "Nether": 1,
        "End": 2
    }

    r_database = r_models.Database("old_databases/server.db")
    r_queries = r_query.Query(r_database)
    player_data: list[r_models.Database.PlayerTable] = r_queries.get_player_data()
    k_database = k_models.Database("new_database/KServer.db")
    k_queries = k_query.Query(k_database)
    for player in player_data:
        discordID = player.discordId
        if not discordID:
            continue
        uuid = get_uuid(player.name)
        if not uuid:
            continue
        p = k_models.Database.PlayerTable(uuid, player.name)
        k_queries.insert(p)

        pos_data: r_models.Database.PosTable = r_queries.get_player_pos_data(player.name)
        if pos_data.deathDim:
            back = k_models.Database.BackTable(uuid, pos_data.deathX, pos_data.deathY, pos_data.deathZ, dims.get(pos_data.deathDim))
            k_queries.insert(back)
        if pos_data.homeDim:
            home = k_models.Database.HomeTable(uuid, pos_data.homeX, pos_data.homeY, pos_data.homeZ, dims.get(pos_data.homeDim))
            k_queries.insert(home)
        perms = k_models.Database.PermsTable(uuid, int(player.perms))
        k_queries.insert(perms)

        discord = k_models.Database.DiscordTable(uuid, discordID if discordID != 999999 else 69420)
        k_queries.insert(discord)

        if player.isBanned == 1:
            discord_banned = k_models.Database.DiscordBannedTable(discordID)
            k_queries.insert(discord_banned)
