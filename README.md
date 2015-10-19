# blag
Systems Management 2015-16 Web Design Project.

Credits to [this repo](https://github.com/arocks/qblog) for the basic design of the blog. Thanks!

This is a blogging platform with a bit of twist. It's been optimized for... memes and other similar cool stuff!
It's also a regular blogging platform. Obviously.

In most blogging platforms, if you want to include a popular meme or an xkcd comic, you normally have to search for it separately and paste the URL in the image box, or go to a meme generator, make the meme, download it, upload it... well you get the idea.

Blag changes all this! In our custom flavour of Markdown, we have a snazzy new tag called `<magic>`.
This tag will try and best fit anything between `<magic>` and `</magic>` to what you want.

For example,
* `<magic>y u do dis</magic>` will change to the 'y u do dis' meme in the rendered HTML post.
* `<magic>xkcd: purity of fields</magic>` will change to the 'Purity of fields' comic from xkcd.
* `<magic>doge: much freedom, such 'murrica, wow</magic>` will change to the Doge meme with 'much freedom', 'such 'murrica',
and 'wow' one below the other on the meme.

When `<magic>` won't be able to match your keywords appropriately, it'll return a 'Couldn't find image :(' on the rendered HTML.

## Working keyword patterns

* `<magic>[meme name]</magic>` will return the meme in its canonical form, with no added captions or additions.
* `<magic>[meme name]: [Line 1], [Line 2]</magic>` will return the meme with the given lines.
* `<magic>doge: [Line 1], [Line 2]... [Line n]</magic>` will return the Doge meme with the given lines.
* `<magic>gif: [gif keywords]</magic>` will try and return the best-fitting gif with the given keywords.
* `<magic>xkcd: [comic keywords]</magic>` will try and return the best-fitting xkcd comic with the given keywords.

## Supported memes

* Grumpy Cat
* Doge (only the Doge meme will support more than 2 lines of text)
* Bad Luck Brian
* Futurama Fry (not sure dude)
* Condescending Willy Wonka
* Success Kid (clenched-fist baby)
* Spongebob Rainbow
* Table Flip Guy
* Y U No

# Todo

* Get basic blog functional and come up with sexy web design (Ishbir, Raunkar, Anubhav)
* Make `<magic></magic>` Markdown plugin (Radhika)
* Get comments working
* Make custom admin panel for authors

# Instructions

* Make a virtualenv for Python3. Activate it.
* Finish the Django tutorial from the Django docs before you start anything at all.
* Read up on Git and GitHub. You should be comfortable with cloning, committing, pushing, and branching.
* `git clone https://github.com/RadhikaG/blag.git` into your working directory.
* After making sure you're in your virtualenv, do `pip install -r requirements.txt`. This will install all the Python libraries and modules you need for this project.
* `python manage.py migrate`
* `python manage.py makemigrations blag`
* Replace `<your name>` with your name without the angled brackets: `git branch <your name>`. For example, `git branch radhika`.
* `git checkout <your name>`
* Do your magic.
* `git add <your changed files>`
* `git push origin <your name>`
