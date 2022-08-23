"""Test leader_board"""

# pylint: disable=missing-function-docstring

from assertpy import assert_that
from league_table.leader_board import (
    determine_match_points,
    generate_league_table,
    rank_league_table,
)


def test_appropriate_match_points_are_assigned_for_each_game():
    sample_match_result = "Lions 3, Snakes 3"
    points_assignment = determine_match_points(sample_match_result)

    assert_that(points_assignment).is_equal_to({"Lions": 1, "Snakes": 1})


def test_league_table_is_generated_from_match_results():
    sample_match_results = [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0",
        "Lions 1, FC Awesome 1",
        "Tarantulas 3, Snakes 1",
        "Lions 4, Grouches 0",
    ]

    league_table = generate_league_table(sample_match_results)
    expected_outcome = {
        "Lions": 5,
        "Snakes": 1,
        "Tarantulas": 6,
        "FC Awesome": 1,
        "Grouches": 0,
    }

    assert_that(league_table).is_equal_to(expected_outcome)


def test_leader_board_is_generated_from_league_table():
    sample_generated_league_table = {
        "Lions": 5,
        "Snakes": 1,
        "Tarantulas": 6,
        "FC Awesome": 1,
        "Grouches": 0,
    }

    leader_board = rank_league_table(sample_generated_league_table)
    expected_outcome = {
        "Tarantulas": 6,
        "Lions": 5,
        "FC Awesome": 1,
        "Snakes": 1,
        "Grouches": 0,
    }

    assert_that(leader_board).is_equal_to(expected_outcome)
