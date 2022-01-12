"""
Defines some HTML for the webpage generator
Treated almost like a dataclass, however I thought a separate file may work best
probably won't be using most of these
"""

DEFAULT_PAGE = \
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Summer Sale</title>
</head>
<body>
    <h1>
        Stay tuned for our amazing summer sale!
    </h1>
</body>
</html>
"""

HEADERS = {
    1: "<h1>",
    2: "<h2>",
    3: "<h3>",
    4: "<h4>",
    5: "<h5>",
    6: "<h6>",
}

c_HEADERS = {
    1: "</h1>",
    2: "</h2>",
    3: "</h3>",
    4: "</h4>",
    5: "</h5>",
    6: "</h6>",
}

PARAGRAPH = "<p>"
c_PARAGRAPH = "</p>"

HEADER = "<header>"
c_HEADER = "</header>"

BODY = "<body>"
c_BODY = "</body>"

TITLE = "<title>"
c_TITLE = "</title>"

DEFAULT_FILENAME = "index.html"

REBUILD_1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>"""  # before title

REBUILD_2 = """</title>
</head>
<body>\n"""  # after title and before body

REBUILD_3 = """</body>
</html>"""  # after body

