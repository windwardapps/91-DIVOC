from datetime import datetime

TIMESTAMP = datetime.now().strftime('%Y%m%d')
SCRIPT_TEXT = '<script src="vis.js?v='
SCRIPT_SUFFIX_TEXT = '"></script>'
CSV_TEXT = 'var covidData_promise = d3.csv("jhu-data.csv?d='
CSV_SUFFIX_TEXT = '", function (row) {'

ENTRIES = [
    ['./graph-1.html', SCRIPT_TEXT, SCRIPT_SUFFIX_TEXT],
    ['./graph-2.html', SCRIPT_TEXT, SCRIPT_SUFFIX_TEXT],
    ['./vis.js', CSV_TEXT, CSV_SUFFIX_TEXT],
]

for filename, prefix, suffix in ENTRIES:
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(prefix):
                updated_line = f'{prefix}{TIMESTAMP}{suffix}\n'
                lines[i] = updated_line

    with open(filename, 'w') as f:
        f.writelines(lines)
