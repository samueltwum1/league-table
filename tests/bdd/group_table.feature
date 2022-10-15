Scenario Outline: Group table from match results
    Given an example league table application
    When fresh <match_results> come through
    Then group table should reflect the <new_standings>

        Examples:
            | match_results          | new_standings                                               |
            | Ghana 3, Portugal 3    | {"Ghana": 1, "Portugal": 1}                                 |
            | Uruguay 0, Ghana 1     | {"Ghana": 4, "Portugal": 1, "Uruguay": 0}                   |
            | South Korea 1, Ghana 2 | {"Ghana": 7, "Portugal": 1, "Uruguay": 0, "South Korea": 0} |
            | Portugal 3, Uruguay 1  | {"Ghana": 7, "Portugal": 4, "Uruguay": 0, "South Korea": 0} |
