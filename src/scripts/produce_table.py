"""League table generator"""

import argparse
import os
import sys

from league_table.leader_board import generate_league_table, rank_league_table

parser = argparse.ArgumentParser(
    description=(
        "League table generation from match results\n\n"
        "Provide the path to the file"
    )
)

parser.add_argument(
    "-p",
    "--path",
    type=str,
    required=True,
    help="path to the file",
)


def process_file_for_processing(args):
    """Parse input from user and process file"""
    path_to_file = args.path

    # sundry checks for cmd line args
    if not os.path.exists(path_to_file):
        print("The file does not exist")
        sys.exit(0)

    with open(path_to_file) as reader:
        match_results = reader.read().splitlines()

    league_table = generate_league_table(match_results)
    return rank_league_table(league_table)


def main():
    args = parser.parse_args()
    results = process_file_for_processing(args)
    for idx, (team, pts) in enumerate(results.items()):
        print(f"{idx+1}. {team}, {pts} pts ")


if __name__ == "__main__":
    main()
