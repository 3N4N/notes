import os
import re
from collections import defaultdict

# folders = ["bookish/", "coding/", ]   # folders to scan
folders = ["site/"]
pages = defaultdict(list)

title_re = re.compile(r"<title>(.*?)</title>", re.IGNORECASE)

def get_title(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                m = title_re.search(line)
                if m:
                    return m.group(1)
    except:
        pass
    return os.path.basename(path)

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(".html") and f != "index.html":
                path = os.path.join(root, f)
                title = get_title(path)
                pages[root].append((title, path))

with open("index.html", "w", encoding="utf-8") as out:
    out.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Notes Index</title>
<style type="text/css">code{white-space: pre;}</style>
<link rel="stylesheet" href="./css/tufte.css">
<link rel="stylesheet" href="./css/pandoc.css">
<link rel="stylesheet" href="./css/tufte-extra.css">
<style>
body{
    font-family: sans-serif;
    max-width: 900px;
    margin: 40px auto;
    line-height: 1.6;
}
h1{
    border-bottom: 2px solid #ccc;
}
h2{
    margin-top: 30px;
}
ul{
    list-style: none;
    padding-left: 0;
}
li{
    margin: 6px 0;
}
a{
    text-decoration: none;
}
a:hover{
    text-decoration: underline;
}
</style>
</head>
<body>
<h1>Notes Index</h1>
""")

    for folder in sorted(pages):
        out.write(f"<h2>{folder}</h2>\n<ul>\n")
        for title, path in sorted(pages[folder]):
            out.write(f'<li><a href="{path}">{title}</a></li>\n')
        out.write("</ul>\n")

    out.write("</body></html>")
