import matplotlib.pyplot as plt


def plot_df_wrappers(df_wrappers, labels=None):
    if labels is None:
        labels = [df_wrapper.name for df_wrapper in df_wrappers]
    plt.figure()
    for df_wrapper, label in zip(df_wrappers, labels):
        plt.plot(df_wrapper.d.index, df_wrapper.d.prob, label=label)
    plt.legend()
    plt.show()
