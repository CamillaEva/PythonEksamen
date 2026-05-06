import matplotlib.pyplot as plt
import numpy as np


def donut_chart(used, total):
    free = total - used
    values = [used, free]
    colors = ["#F9C5C4", "#f0f2f6"]

    fig, ax = plt.subplots()

    ax.pie(
        values,
        colors=colors,
        startangle=90,
        counterclock=False,
        radius=0.7,
        wedgeprops={"width": 0.25}
    )

    percent = round((used / total) * 100)

    ax.text(0, 0, f"{percent}%", ha="center", va="center")

    ax.set_aspect("equal")

    return fig