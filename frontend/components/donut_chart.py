import matplotlib.pyplot as plt
import numpy as np

def donut_chart(calories, daily_goal):

    used_percent = (calories / daily_goal) * 100
    remaining_percent = 100 - used_percent
    colors = ["#F9C5C4", "#f0f2f6"]

    sizes = [used_percent, remaining_percent]

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        radius=0.7,
        wedgeprops={"width": 0.15}
    )

    ax.text(0, 0.5, f"{int(used_percent)}%", ha="center", va="center")
    ax.text(0,-0.12, f"{calories} out of {daily_goal} used", ha="center", va="center")

    ax.set_aspect("equal")

    return fig