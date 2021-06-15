# thyncAPI
> The one and only thyncAPI. Used for thync projects

## About
This was originally created just for the thync Bot, a discord bot that syncs with thync. However, I do think this could be more handy in other sub-projects, so I created this a bit more detailed and etc. Some of the code is used from Reflux, a project and module created by frissyn and CoolCoderSJ. However, this issue and suggestion came up, so I decided to create this. thync has also become sub-projects and a major project.

> thync has not come out yet, this is just thyncAPI.

## Using it
To use it, as of right now, you have to open up [this](https://thync-API.jbloves27.repl.co/toggle), and then to use it in python, do the following:
```py
import requests

res = requests.get("https://thync-API.jbloves27.repl.co/toggle")
data = res.text
print(data)
```
**OR**
```py
import requests

res = requests.get("https://thync-API.jbloves27.repl.co/toggle")
data = res.content
print(data)
```
You can either print or return, depending on how you'll use it. Then copy the code, make a bookmark, and paste in the url/link. Then click the bookmark when you are on Replit. You're all set!


## Suggestions and contribute
To leave suggestions, just leave a comment or a PR. To contribute, leave a PR or an issue to ask.

## Conclusion
I hope you enjoy using this API! See you on the next post!