# none of this works without internetarchive
# pip install internetarchive
from internetarchive import download

# LINKS DONT WORK
# instead of using 
# https://archive.org/details/logan-paul-dead-body-re-upload
# USE THIS
# logan-paul-dead-body-re-upload

download("logan-paul-dead-body-re-upload", verbose=True)
