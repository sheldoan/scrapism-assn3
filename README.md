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
$ python they-met.py Alexander 0

Alexander met Leah (through the dating website OkCupid)
He met Michelle (in Manhattan through a mutual friend)
He met Chloe (on the app Coffee Meets Bagel in New York)
He met Shweta (at a rock climbing event in Trier, Germany)
He met Johanna (as undergraduates at Wake Forest University)
He met Jessica (in October through the dating app the League)
He met Brooke (over Independence Day weekend at a vineyard in Sonoma, Calif)
He met Katina (at George Washington University, from which they both graduated)
He met Elise (in New York on a blind date set up by a mutual friend in February)
He met Mallory (at Columbia, from which they graduated, the groom summa cum laude)
He met Martha (in October at a club in San Francisco where a mutual friend was the D.J)
He met Neha (at Princeton, from which they graduated, she cum laude and he summa cum laude)
And finally, Alexander met Jessica in Boston, where they were both working on projects involving military veterans
```
