---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="k2Jnw-6i7OMk" outputId="ae561c7d-ae78-4b6b-9f77-e0331d8c4894"}
``` python
!ls
```

::: {.output .stream .stdout}
    latest.txt  main.py  __pycache__  sample_data
:::
:::

::: {.cell .code id="5YYhT5JG7n2D"}
``` python
import xkcd
```
:::

::: {.cell .markdown id="DKx8o2To_axA"}
### Updating the latest comic for quick load time 🚀 {#updating-the-latest-comic-for-quick-load-time-}

It is not necessary to use this function as it will automatically update
the latest comic as soon as you run the `get_comic()` function. Only
difference here being that you need to specify for verbose whether it is
`True` for `Flase`

The latest comic is stored in the `latest.txt` file
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="nhyHwoZK-xiL" outputId="af90916e-43e7-4060-dbf7-0bfa2d6e97ac"}
``` python
comic = xkcd.get_latest_comic(verbose=True)
```

::: {.output .stream .stdout}
        current comic =====> 2781
        current comic =====> 2782
:::
:::

::: {.cell .markdown id="9RSNQ9npAnfs"}
## The `get_comic()` function

Parameters

-   verbose : `bool`
    -   by default verbose is set to false. The output is same as the
        output as the cell above as it uses the `get_latest_comic()`
        function
-   comic : `str`
    -   use string `"latest"` for the latest comic
    -   use `"< some integer >"` for getting a specific comic

    ```{=html}
    <!-- -->
    ```
        # Example Code
        xkcd.get_comic(comic="199")
:::

::: {.cell .code id="COlS5cb-AnNw"}
``` python
```
:::

::: {.cell .markdown id="GUygcVfK_mH3"}
## Comic class functions

1.  To display the latest comic

``` python
# Example Code
comic.display()
```

1.  To display the

``` python
# Example Code
comic.show()
```
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="ZlYlldaM-5VJ" outputId="a08d1a3b-063e-40be-ca5f-90aeee733d52"}
``` python
comic.display()
```

::: {.output .stream .stdout}

    XKCD Comic 199
        > year 2006
        > title Right-Hand Rule
        > comic https://imgs.xkcd.com/comics/right_hand_rule.png
        > alt To really expand your mind try some noncartesian porn.  Edwin Abbot Abbott has nothing on 'Girls on Girls in Tightly Closed Nonorientable Spaces'.
            
:::
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":756}" id="0c3mh5RdAC4N" outputId="aeb8eb7b-5a47-4516-a775-ddae9c712c4d"}
``` python
comic.show()
```

::: {.output .display_data}
![](vertopal_6708930426af4c0aad21f1e7c0244cf6/7ea72460e495dea9258943ecb3343def2c557faf.png)
:::
:::
