# League Table Generation
This is generates a league table from match results

## Usage
```bash
produce-table --help
usage: produce_table.py [-h] -p PATH

League table generation from match results Provide the path to the file

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to the file
```

#### Example

```bash
$ produce-table -p data/sample_input 
1. Tarantulas, 6 pts 
2. Lions, 5 pts 
3. FC Awesome, 1 pts 
4. Snakes, 1 pts 
5. Grouches, 0 pts 
```
