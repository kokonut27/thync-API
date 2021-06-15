import os
from flask import request, jsonify, render_template, Flask
from values import DEFAULT, COLORS, JS, CSS
from datetime import datetime

app = Flask(__name__)

now = datetime.now()

cur_time = now.strftime("%H")



def update(stale, new):
    for n, v in new.items():
        stale[n] = v
    return stale
def wrap(name: str, value: str):
    return name + "{" + value + " !important}" 

class thync(object):
    def __init__(self, obj):
        self.obj = update(DEFAULT, obj)
        self.obj["colors"] = COLORS[obj["default"]]
        self.obj["code"] = COLORS["code"]
    
    def set_editor(self, name: str, value: str):
        v = wrap("div.view-lines", f"{name}: {value}")
        self.obj["code"] += v
        return None
    
    def set_color(self, name: str, value: str):
        target = self.obj["colors"][name]
        target = value
        return target

    def set_colors(self, obj: dict):
        self.obj["colors"] = update(self.obj["colors"], obj)
        return None
    """
    def get_color(self, name: str):
        try:
            return self.obj["colors"][name]
        except ValueError:
            return None
    """

    def build(self, path, mode="w+"):
        js = JS
        css = ""
        file = open(path, mode)

        for n, v in self.obj["colors"].items():
            css += f"--color-{n}: {v} !important;"
        
        for n, v in self.obj.items():
            if not isinstance(v, dict):
                js = js.replace(f"!{n}!", str(v))
            else:
              pass

        css = (
            CSS
            .replace("!!css!!", css)
            .replace("!!syntax!!", self.obj["code"])
        )
        js = (
            js
            .replace("!css!", css)
            .replace("\n", "")
            .replace("\t", "")
            .replace("    ", "")
            .replace(" = ", "=")
        )

        file.write(js)
        file.close()
        return True

thync_light = thync({
  "name": None,
  "description": None,
  "default": "light"
})
thync_dark = thync({
  "name": "Dark Theme",
  "description": "Dark theme for Replit",
  "default": "dark"
})

@app.route("/")
def index():
  return "thyncAPI"


@app.route("/toggle")
def toggle():
  if int(cur_time) >= 12:
    for n, v in COLORS["dark"].items():
      thync_dark.set_color(n, "black")
    thync_dark.build("thync.min.js")
    f = open("thync.min.js")
  else:
    thync_light.build("thync.min.js")
    f = open("thync.min.js")
  f = f.read()
  return render_template(
    "toggle.html",
    file=f
  )

app.run(host="0.0.0.0", port=8080)