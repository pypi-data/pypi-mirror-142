# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:33:39 2022

@author: bhook
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def main():
    """
    main entry point to program.
    create a wordcloud and display it to the user.

    Returns
    -------
    None.

    """
    stopwords = set(STOPWORDS)

    with open("wordle_solutions.txt", "r") as words_file:
        words = words_file.readlines()

    words = [x.replace("\n", "") for x in words]

    words = " ".join(words)

    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color="white",
        stopwords=stopwords,
        min_font_size=10,
    ).generate(words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()


if __name__ == '__main__':
    main()
