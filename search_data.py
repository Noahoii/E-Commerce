from common import Common


def search_Data(keyword):
    output_filename = f"{keyword}.txt"
    with open("data/trainKeyCleaned.txt", "r", encoding="utf") as infile, open(output_filename, "w", encoding="utf-8") as outfile:
        for line in infile:
            if keyword in line:
                outfile.write(line)


for keyword in Common.seed_keys:
    search_Data(keyword)
