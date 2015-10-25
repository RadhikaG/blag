# blag
Systems Management 2015-16 Web Design Project.

Credits to [this repo](https://github.com/arocks/qblog) and [this post](http://trevore.com/post/building-blog-django-17-and-python-34) for the basic version of the blog. Thanks!

This is a blogging platform with a bit of twist. It's been optimized for... memes and other similar cool stuff!
It's also a regular blogging platform. Obviously.

In most blogging platforms, if you want to include a popular meme or an xkcd comic, you normally have to search for it separately and paste the URL in the image box, or go to a meme generator, make the meme, download it, upload it... well you get the idea.

Blag changes all this! In our custom flavour of Markdown, we have a snazzy new tag called `[magic]`.
This tag will try and best fit anything between `[magic]` and `[/magic]` to what you want.

The `[magic]` Markdown extension was written by [Radhika Ghosal](https://github.com/RadhikaG).

For example,
* `[magic] meme: y u do dis[/magic]` will change to the 'y u do dis' meme in the rendered HTML post.

When `[magic]` won't be able to match your keywords appropriately, it'll return the appropriate error message on the rendered HTML without breaking the application.

## Working keyword patterns

* `[magic] meme: [Line 1], [Line 2] [/magic]` will return the required meme with the given lines.
* `[magic] gif: <space-separated gif keywords> [/magic]` will try and return the best-fitting gif with the given keywords.

Please check the [markdown-magic](https://github.com/RadhikaG/markdown-magic) repo for full set of instructions.

## Supported memes

Please check the [markdown-magic](https://github.com/RadhikaG/markdown-magic) repo for the full list of supported memes.

# Todo

* Make custom admin panel for authors (apart from the default Django admin panel)

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
