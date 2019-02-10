import re

ScriptName = "perm"
Website = "https://github.com/madelsberger/perm_StreamlabsParameter"
Description = "permission-check parameter - $perm(madelsberger, Editor)"
Creator = "madelsberger"
Version = "1.0.0"

def Init():
    pass

def Parse(parseString, user, target, message):
    old = parseString
    new = ""
    pattern = "(.*?)\$perm\s*\(\s*([a-zA-Z0-9_]+)\s*,\s*([A-Za-z]+)\s*\)(.*)"
    match = re.match(pattern, old)
    while match is not None:
        new += match.group(1)
        if Parent.HasPermission(match.group(2), match.group(3), ""):
            new = new + "1"
        else:
            new = new + "0"
        old = match.group(4)
        match = re.match(pattern, old)
    else:
        new += old
    return new
