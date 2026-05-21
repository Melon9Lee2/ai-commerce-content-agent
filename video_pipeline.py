def create_storyboard(script):
    storyboard = []
    for line in script.split("\n"):
        storyboard.append({"shot": line, "type": "base"})
    return storyboard
