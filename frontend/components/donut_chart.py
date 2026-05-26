import matplotlib.pyplot as plt
from styles.colors import (BACKGROUND_COLOR, PRIMARY_CHART_COLOR, EDGE_COLOR)

DONUT_WIDTH = 0.15
DONUT_RADIUS = 0.8

def donut_chart(calories, daily_goal):

    used_percent = (calories / daily_goal) * 100
    remaining_percent = 100 - used_percent

    sizes = [used_percent, remaining_percent]

    fig, ax = plt.subplots()

    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)

    ax.pie(
        sizes,
        colors=[PRIMARY_CHART_COLOR, BACKGROUND_COLOR],
        startangle=90,
        counterclock=False,
        radius=DONUT_RADIUS,
        wedgeprops={"width": DONUT_WIDTH, 
                    "edgecolor": EDGE_COLOR,
                    "linewidth": 1}
    )

    ax.text(0, 0.15, f"{int(used_percent)}%", ha="center", va="center", fontsize=20, fontweight="bold")
    ax.text(0,-0.15, f"{calories} out of {daily_goal} used", ha="center", va="center", fontsize=10)


    ax.set_aspect("equal")

    return fig