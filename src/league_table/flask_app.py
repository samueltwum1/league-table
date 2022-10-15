import os
from flask import Flask, request, render_template
from league_table.leader_board import generate_league_table, rank_league_table

app = Flask(__name__, template_folder="./templates")

current_league_table = {}

def generate_fresh_ranking():
    global current_league_table
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open(f"{cwd}/live_score") as reader:
        match_results = reader.read().splitlines()

    league_table = generate_league_table(match_results)

    if not current_league_table:
        current_league_table = rank_league_table(league_table)
        return

    for team, pt in league_table.items():
        if team in current_league_table:
            current_league_table[team] += pt
        else:
            current_league_table[team] = pt
    current_league_table = rank_league_table(league_table)


@app.route("/")
def the_software_league():
    generate_fresh_ranking()
    return render_template("index.html", ltable=current_league_table)

@app.route("/league_table", methods=["POST", "GET"])
def current_league_standings():
    if request.method == "POST":
        cwd = os.path.dirname(os.path.realpath(__file__))
        with open(f"{cwd}/live_score", "a") as f:
            input_data = request.data
            f.write(input_data.decode())
            f.write("\n")
        generate_fresh_ranking()
        return "Success"

    elif request.method == "GET":
        return current_league_table


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
