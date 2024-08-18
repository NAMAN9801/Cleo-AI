import webbrowser


def search_chrome(query):
    """constructs url, opens chrome and searches for it."""
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
        # webbrowser.get("chrome").open(search_url)


search_chrome("What is python")
