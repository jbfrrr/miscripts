# `basic-static-crawler.py`

### What this script does?
This is a basic crawler script that simply does a `curl` for every `url` found in `urls.txt` and produces a `result.txt` containing the response from each request.

`urls.txt` is a file defined/supplied by a user in this same directory. This file contains a list of all complete/full urls that the user wishes the crawler to check.

`result.txt` is a file produced by the script in this directory. This file contains each `url` that was curled and its corresponding response (e.g. `200`, `404`, etc.)

### How to use this?
1. Create `urls.txt`
2. Simply run
```sh
python basic-static-crawler.py
```
3. Examin `results.txt`

### Additional Info
You can modify the script e.g. adding more constraints / conditions on what / how to `curl` or even modify how `results.txt` is produced.
