import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random

def laker_purple_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return 'hsl(262, 76%, 50%)'


page = wikipedia.page('Los Angeles Lakers')
text = page.content

cloud = WordCloud(background_color='gold').generate(text)
plt.title("Los Angeles Lakers")
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(cloud.recolor(color_func=laker_purple_color_func, random_state=3), interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
