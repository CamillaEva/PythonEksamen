import matplotlib.pyplot as plt

#plt.style.use('_mpl-gallery')

#make data
#days = ["Man", "Tir", "Ons", "Tor", "Fre", "Lør", "Søn"]
#values = [1610, 1555, 1880, 1532, 1969, 2000, 1545]

#fig, ax = plt.subplots()

#ax.bar(days, values)

#ax.set_xlabel("Ugedage")
#ax.set_ylabel("kcal")
#ax.set_title("ugens kcal")

#ax.bar(days, values, color="#F9C5C4", edgecolor="#3A3A3A")

#plt.show()

#st.pyplot(fig)


def weekly_calorie_chart(days, values):
    plt.style.use('_mpl-gallery')

    fig, ax = plt.subplots()

    ax.bar(days, values, color="#F9C5C4", edgecolor="#3A3A3A")

    ax.set_xlabel("Ugedage")
    ax.set_ylabel("kcal")
    ax.set_title("Ugens kcal")

    return fig