"""Determine rank of teams based on match results"""

from typing import Dict, List


def determine_match_points(match_result: str) -> Dict:
    """
    Determine the points per each match played

    :return: A dict representing points earned per match for each team
    """
    if not match_result:
        return {}

    match_result = match_result.split(",")
    for idx, team_score in enumerate(match_result):
        match_result[idx] = team_score.split()
        # check for when the team name has spaces
        # e.g. FC Awesome 1 will return ["FC", "Awesome", 1]
        if len(match_result[idx]) > 2:
            team_name = " ".join(match_result[idx][:-1])
            goals = match_result[idx][-1]
            match_result[idx] = [team_name, goals]

    team_a, team_b, points = 0, 1, 1
    team_a_goals = match_result[0][1]
    team_b_goals = match_result[1][1]

    # determine game points based on score
    if team_a_goals == team_b_goals:
        match_result[team_a][points] = 1
        match_result[team_b][points] = 1
    elif team_a_goals < team_b_goals:
        match_result[team_a][points] = 0
        match_result[team_b][points] = 3
    else:
        match_result[team_a][points] = 3
        match_result[team_b][points] = 0

    return dict(match_result)


def generate_league_table(file_data: List) -> Dict:
    """
    Compute the league table from the match results summing all points

    :return: A dict representing the league table
    """
    league_table = {}
    if not file_data:
        return league_table

    def _update_league_table(team_name, points):
        if team_name in league_table:
            league_table[team_name] += points
        else:
            league_table[team_name] = points

    for data in file_data:
        match_points = determine_match_points(data)
        for team_name, points in match_points.items():
            _update_league_table(team_name, points)

    return league_table


def rank_league_table(league_table: dict) -> Dict:
    """
    Orders the calculated points from the match results

    :return: A dict representing the leaderboard
    """
    point_based_ranking = sorted(
        league_table.items(), key=lambda item: item[1], reverse=True
    )

    def _rank_point_based_ranking(initial_ranking):
        # sort ties in alphabetical order of team name
        def sort_team_order(ranking):
            print(ranking)
            for idx, rank in enumerate(ranking):
                tmp = rank[1]
                if idx == len(ranking) - 1:
                    break
                points = ranking[idx + 1][1]
                if points == tmp:
                    neighbour_teams = [rank[0], ranking[idx + 1][0]]
                    if neighbour_teams != sorted(neighbour_teams):
                        swp = rank
                        ranking[idx] = ranking[idx + 1]
                        ranking[idx + 1] = swp
                else:
                    tmp = ranking[idx + 1][1]
            return ranking

        # recursively sort the team order
        if sort_team_order(initial_ranking) == initial_ranking:
            return initial_ranking
        else:
            new_ranking = sort_team_order(initial_ranking)
            _rank_point_based_ranking(new_ranking)

    leader_board = _rank_point_based_ranking(point_based_ranking)
    return dict(leader_board)
