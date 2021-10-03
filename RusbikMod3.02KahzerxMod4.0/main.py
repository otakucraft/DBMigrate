from RusbikMod import models as r_models, query as r_query
from KahzerxMod import models as k_models, query as k_query

if __name__ == '__main__':
    rusbik_database = r_models.Database("old_databases/server.db")
    rusbik_queries = r_query.Query(rusbik_database)
    player_data: list[r_models.Database.PlayerTable] = rusbik_queries.get_player_data()
    pos_data: list[r_models.Database.PosTable] = rusbik_queries.get_pos_data()
    print(player_data)
    print(pos_data)

    kahzerx_database = k_models.Database("new_database/KServer.db")
    kahzerx_queries = k_query.Query(kahzerx_database)
