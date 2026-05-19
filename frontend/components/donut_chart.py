import matplotlib.pyplot as plt

def donut_chart(calories, daily_goal):

    used_percent = (calories / daily_goal) * 100
    remaining_percent = 100 - used_percent
    colors = ["#F9C5C4", "#FDF0E6"]
    

    sizes = [used_percent, remaining_percent]

    fig, ax = plt.subplots()


    fig.patch.set_facecolor("#FDF0E6")
    ax.set_facecolor("#FDF0E6")

    ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        radius=0.8,
        wedgeprops={"width": 0.15, 
                    "edgecolor": "#3A3A3A",
                    "linewidth": 1}
    )

    ax.text(0, 0.15, f"{int(used_percent)}%", ha="center", va="center", fontsize=20, fontweight="bold")
    ax.text(0,-0.15, f"{calories} out of {daily_goal} used", ha="center", va="center", fontsize=10)


    ax.set_aspect("equal")

    return fig