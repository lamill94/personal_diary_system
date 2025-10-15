def make_snippet(string):
    words = string.split()

    if len(words) > 5:
        first_five_words = words[0:5]
        return " ".join(first_five_words) + "..."
    else:
        return string