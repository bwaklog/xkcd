# XKCD VIEWER v1.2
<a target="_blank" href="https://colab.research.google.com/github/bwaklog/xkcd_view/blob/master/xkcd_comic.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Demo

    I created an alias in ~/.zshrc do this
    Hence explaining why I used an absolute file reference

![xkcd_cli](https://github.com/bwaklog/xkcd_view/assets/91192289/e475f168-6286-4636-a4f4-fc8ba1e00351)


---
**NOTE :** Change the file path for accessing `latest.txt`

``` python

def get_latest_comic(verbose):
    # -- snip --
    with open(< path to latest.txt >, "r") as f:
        # -- snip --
    while exists:
        # -- snip --
        if req.status_code != 404:
            # -- snip --
            with open(< path to latest.txt >, "w") as f:
                # -- snip --

```
