from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image



text = open('text.txt', 'r').read()

python_mask = np.array(PIL.Image.open('python.jpg'))
colormap = ImageColorGenerator(python_mask)

wc = WordCloud(stopwords=STOPWORDS,
                mask=python_mask,
                background_color='white',
                min_font_size=3,
                max_words=100).generate(text)
wc.recolor(color_func=colormap)
plt.imshow(wc)
plt.axis("off")
plt.show()



