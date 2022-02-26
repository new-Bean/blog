file = "interest_rate_and_duration.html"
outtext = ""
with open(file, 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.replace('&amp;', '&')
        if len(line) >= 2:
            if line[-2] in "\\":
                line = line[:-1] + '\\' + line[-1]
        outtext += line

with open(file, mode='w', encoding='UTF-8') as f:
    f.write(outtext)
