import sys
from pathlib import Path

### Global Constants ###

PKGNAME = "tcal"
MODULE = sys.modules[PKGNAME]

### Global Paths ###

MODPATH = Path(MODULE.__file__).parent

DATAPATH = Path.joinpath(MODPATH, "data")

DBMPATH = Path.joinpath(DATAPATH, "dbase")
DESIGNPATH = Path.joinpath(DATAPATH, "designs")
IMGPATH = Path.joinpath(DATAPATH, "img")

ICONPATH = Path.joinpath(IMGPATH, "icon.png")
LOGOPATH = Path.joinpath(IMGPATH, "icon.png")

### Global Links ###

SQLPREFIX = "sqlite:///"

TWITTERLINK = "https://twitter.com/"

SITELINK = Path("https://crazyastrochemist.netlify.app/")

UPLINK = (
    "https://docs.google.com/spreadsheets/d/e/2PACX"
    "-1vQkbCd9kEllq5SpaH13VxJEtw1k7eN3VdFTQetTP7udL"
    "10I0U-erve4IqotzOhDlp9ug-7ANoFqGpka/pub?gid=69"
    "0927575&single=true&output=csv"
)

FORMLINK = Path.joinpath(SITELINK, "tcal", "help")

WEBLINK = Path.joinpath(SITELINK, "tcal", "list")

### Global Variables ###

SKIPLINES = 4

PARASTART = "<p align='{}'>"
PARAEND = "</p>"

DFHEADER = [
    "Name",
    "Institute(s)",
    "Current Position",
    "Email",
    "Personal / Institute Website",
    "Twitter Handle",
]

DBHEADER = ["name", "institute", "position", "email", "website", "thandle"]
