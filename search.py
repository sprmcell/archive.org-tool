# none of this works without internetarchive
# pip install internetarchive

from internetarchive import search_items

# REPLACE
# logan-paul-dead-body-re-upload
# with the search query of your choice

for i in search_items('identifier:https://archive.org/details/logan-paul-dead-body-re-upload'):
    print(i["identifier"])
