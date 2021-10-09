from flask import Flask
from flask import render_template
import os
from os import listdir
from os.path import isfile, join


app = Flask(__name__)

@app.route("/")
def hello(name=None):
  base_name = os.path.join(os.path.dirname(__file__), 'data')

#   Get all point and locations
# Location lat and long get from:
# https://nominatim.openstreetmap.org/search?format=json&q=

  files = {}
  for file_name in [f for f in sorted(listdir(base_name))]:
       file = open(base_name+'/'+file_name,mode='r')
       files[file_name.replace('.json','')[3:]] = file.read()
       file.close()

  return render_template('map.html',
   locations_params={'files': list(files.keys()),'files_contents':list(files.values()) })

if __name__ == "__main__":
  app.run()