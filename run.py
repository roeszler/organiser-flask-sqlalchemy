import os
from organiser import app

if __name__ == "__main__":
    """
    Checks to see if the the file is being run directly or as an import. 
    If an import, it will not run the instructions contained within.
    """
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )