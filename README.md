# a big list

For this assignment I scraped the New York Times weddings announcements. I was able to get around two years worth (2017-2019); about 2000 in total.

The web-scraping is in `weddings.py`, and the data lives in `data.csv`. Image downloading was done by `download-images.py` and those files are stored in `big-images/`.

## couple photos ##

Opening `index.html` will show a webpage that allows you to display all couples whose descriptive text or names match the query.

The NYT particularly enjoys featuring couples that went to Ivy League schools. Here's the result for Harvard:

![alt text](https://drive.google.com/uc?export=view&id=1zId-9WgpVKDoaqoFUdVCw720LJrI51zE)

You can also search by name. Here are all the Stephanies:
![alt text](https://drive.google.com/uc?export=view&id=14KWT2joyijRjz9E8a1TCMkW2uH5gdZNV)

## facial similarity ##

I tried using the [face_recognition](https://github.com/ageitgey/face_recognition) library to find couples with very similar faces. These were the results for most similar:

![alt text](https://drive.google.com/uc?export=view&id=17eq7AfZoAtVPIhpmsJNDGkypOPk27OGL)

and least similar:

![alt text](https://drive.google.com/uc?export=view&id=1kTpCuWCWVF6laXDEgWAm6eg50EBy3mtM)

As you can see, the algorithm seems to think Asian couples look very similar, even when there were many non-Asian couples that looked more similar than these results!

## names & descriptions ##

Every announcement comes with the names of the couple and a brief summary. As Sam noted, most of these summaries have a similar format: "The couple met ...".

I played around with various ways of chopping up and re-arranging the text (see outputs in `outputs/` and the scripts `names.py` and `couple-met.py`). 

This led to creating a script `they-met.py` which takes an input name and gender (for mixed gender couples, the NYT puts female names first). The script creates a "relationship history" for the input person by looking for couples that contain that name, taking how they met, and sorting by length.

Here's some sample output:

```
$ python they-met.py Stephanie 0

Stephanie met Kyle (on OkCupid, the dating website)
She met Chad (at Loyola University in Chicago)
She met Joseph (at Duke University Hospital in Durham)
She met Jeffrey ( on a blind date arranged by a mutual friend)
She met John (in September through a mutual friend in New York)
She met Calgary (at Bell, Book & Candle, a restaurant in New York)
She met Jared (while working as lawyers at a Manhattan law firm)
She met Andrew (through their younger sisters, who were college friends)
She met Thomas (in July while working on a project for Accenture Strategy)
She met James (through mutual friends, who planned a party to introduce them)
She met Joel (in Chicago, as high-school students at Walter Payton College Prep)
She met Jared (while the bride was interviewing for a job at a school in Brooklyn)
She met Stanley (on the way to the Matzoball, a Christmas Eve event for Jewish singles)
She met Stephen (in Washington when both worked for the Democratic Congressional Campaign Committee)
And finally, Stephanie met Azi through the dating app Bumble, and had Belgian waffles for their first date, while sitting by the fountain at Lincoln Center
```
