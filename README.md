# League Table Application
This is generates a league table from match results. The application exists
as a flask app which shows the table in a browser based on match results stored in `live_score`.

This is meant to be a learning example for writing BDD tests and unit tests
using TDD. See `tests/unit` and `tests/bdd`.

## Usage
* Run the flask app
* Populate `live_score` using post request or writing directly to file
* Refresh browser to see new standings
