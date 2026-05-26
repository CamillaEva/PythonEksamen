import matplotlib.pyplot as plt

def bar_chart(daily_kcal):
    fig, ax = plt.subplots(figsize=(5, 2.5))

    ax.bar(daily_kcal.index, daily_kcal.values, color="#F9C5C4")
    
    fig.patch.set_facecolor("#FDF0E6")
    ax.set_facecolor("#FDF0E6")


    goal = 2100
    ax.axhline(
        y=goal,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Goal: {goal} kcal"
    )

    ax.set_title("Calories per day (last 7 days)")
    ax.set_ylabel("Calories")
    ax.set_xlabel("Date")
    
    ax.bar(
    daily_kcal.index,
    daily_kcal.values,
    color="#F9C5C4",
    edgecolor="#3A3A3A",
    linewidth=1 )

    plt.xticks(rotation=45)

    return fig