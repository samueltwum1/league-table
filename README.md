# League Table Application
This is generates a league table from match results. The application exists
as a flask app which shows the table in a browser based on match results stored in `live_score`. 

This is meant to be a learning example for writing BDD tests and unit tests
using TDD. See `tests/unit` and `tests/bdd`.

The application is also available as a script with command-line arguments which
generates a league table from an input file. See README in `src/scripts`.

## Installation
* Install poetry: `pip install poetry`
* Install the package and its dependencies using `poetry install`
* Alternatively, skip steps above and build a docker image to use

> **_NOTE:_**  Use port forwarding if running the application from a docker container. Easier if you use VSCode to attach running container (port forwarding is managed automatically).

## Usage
* Run the flask app
* Populate `live_score` using post request or writing directly to file
* Refresh browser to see new standings
