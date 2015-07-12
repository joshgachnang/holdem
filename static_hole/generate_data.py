"""Grab pre-computed hole win percentages from U of Indiana, output to JSON."""
import json
import urllib.request


if __name__ == "__main__":
    url = "http://www.cs.indiana.edu/~kapadia/nofoldem/2_wins.stats"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    # Silly, fragile, quick way to parse out the data..
    lines = text.split("\n")
    # Trim header and footer
    lines = lines[9:-18]
    data = {}
    for line in lines:
        line = line.split()
        data[line[1]] = {
            "rank": line[0],
            "hole": line[1],
            "win": line[2],
            "tie": line[3],
            "total": line[4]
        }
    output = json.dumps(data)
    with open("hole_data.json", "w") as f:
        f.write(output)
        print("{} {}".format(f, output))
