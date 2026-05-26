import matplotlib.pyplot as plt
from styles.colors import (BACKGROUND_COLOR, PRIMARY_CHART_COLOR, EDGE_COLOR, GOAL_LINE_COLOR)

GOAL_KCAL = 2100

def bar_chart(daily_kcal):
    fig, ax = plt.subplots(figsize=(5, 2.5))
    
    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)

    ax.bar(
    daily_kcal.index,
    daily_kcal.values,
    color=PRIMARY_CHART_COLOR,
    edgecolor=EDGE_COLOR,
    linewidth=1 )

    ax.axhline(
        y=GOAL_KCAL,
        color=GOAL_LINE_COLOR,
        linestyle="--",
        linewidth=2,
        label=f"Goal: {GOAL_KCAL} kcal"
    )

    ax.set_title("Calories per day (last 7 days)")
    ax.set_ylabel("Calories")
    ax.set_xlabel("Date")

    plt.xticks(rotation=45)

    return fig