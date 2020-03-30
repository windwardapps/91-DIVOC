from datetime import datetime

TIMESTAMP = datetime.now().strftime('%Y%m%d')
TIMESTAMP2 = datetime.now().strftime('%-m/%-d/%Y')
SCRIPT_TEXT = '<script src="vis.js?v='
SCRIPT_SUFFIX_TEXT = '"></script>'
CSV_TEXT = 'var covidData_promise = d3.csv("jhu-data.csv?d='
CSV_SUFFIX_TEXT = '", function (row) {'
DATE_TEXT = 'var _dateUpdated = "'
DATE_SUFFIX_TEXT = '";'

ENTRIES = [
    ['./graph-1.html', SCRIPT_TEXT, TIMESTAMP, SCRIPT_SUFFIX_TEXT],
    ['./graph-2.html', SCRIPT_TEXT, TIMESTAMP, SCRIPT_SUFFIX_TEXT],
    ['./vis.js', CSV_TEXT, TIMESTAMP, CSV_SUFFIX_TEXT],
    ['./vis.js', DATE_TEXT, TIMESTAMP2, DATE_SUFFIX_TEXT],
]

for filename, prefix, timestamp, suffix in ENTRIES:
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(prefix):
                updated_line = f'{prefix}{timestamp}{suffix}\n'
                lines[i] = updated_line

    with open(filename, 'w') as f:
        f.writelines(lines)
