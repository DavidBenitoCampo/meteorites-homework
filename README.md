# Earth Meteorite Landings Analysis

## Task 1:
Extract programmatically the list of Earth Meteorite Landings from this dataset: [https://dmachek.github.io/meteorites-homework/meteorite_landings.json](https://dmachek.github.io/meteorites-homework/meteorite_landings.json)  
- How many entries are in the dataset?  
- What is the name and mass of the most massive meteorite in this dataset?  
- What is the most frequent year in this dataset?  

⚠️ **Provide your solution as a Pull Request to this repository.** ⚠️

**NOTE:** Please elaborate how did you get the results, provide the code or any means which you used to get to the results (regardless of the format/tools/framework which were used). Result itself is not sufficient.

---

## Solution

When I started working on the code, I broke the problem down into three main parts:

1. Getting the Data
I used the requests library to fetch the JSON data. I also added a try/except block because I wanted to make sure that if the website was down or the internet disconnected, the script would show a clear error message instead of just crashing.

2. Finding the Heaviest Meteorite
While looking at the data, I noticed that some meteorites didn't have a mass listed. To fix this, I added an if statement to check if the mass key exists before trying to compare it. I used a simple for loop to keep track of the highest number I had seen so far.

3. Counting the Years
The dates in the JSON were quite long (like 1933-01-01T...). Since I only needed the year, I used string slicing—[:4]—to just grab the first four numbers. I then used collections.Counter, which is a really helpful tool in Python for counting how many times an item appears in a list.


### How to Run

```bash
# Ensure requests is installed
pip install requests

# Run the analysis
python3 meteorite_analysis_task.py
```

### Expected Output

```
Total entries found: 1000
The heaviest meteorite is Sikhote-Alin with mass 23000000
The most frequent year is 1933
```

### Verification

I wanted to be 100% sure that my Python script was giving me the right answers, so I used some handy command-line tools to double-check the data.

Results were cross-verified using command-line tools (`curl` and `jq`):
- curl (The Fetcher): I used this to "grab" the raw data from the link without having to open a web browser. It’s a fast way to see exactly what the computer is reading.
- jq (The Analyzer): This is a specialized tool for working with JSON data on the command line. It allowed me to filter, sort, and count the data in a few simple commands, which is much faster than writing a whole script for a quick check.


```bash
# Verify heaviest meteorite
curl -s https://dmachek.github.io/meteorites-homework/meteorite_landings.json | \
  jq 'max_by(.mass | tonumber?) | {name, mass}'
# Output: {"name": "Sikhote-Alin", "mass": "23000000"}

# Verify most frequent year
curl -s https://dmachek.github.io/meteorites-homework/meteorite_landings.json | \
  jq -r '.[].year | select(. != null)' | cut -c 1-4 | sort | uniq -c | sort -nr | head -1
# Output: 16 1933
```

---
