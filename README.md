# Welcome to the GitRepoScraper Project! 🚀

Hey there, fellow coder! Eager to chart the vast landscapes of GitHub's repositories? Your quest awaits! The GitRepoScraper is not merely a tool; it's a mystical companion on your journey to transcribe the arcane knowledge hidden within GitHub's hallowed repositories into the sacred texts of JSON and READMEs. 🎩✨

## What's This Magic? 🧙‍♂️

The Repo Scraper is a nifty tool that gallivants through the files and directories of a specified GitHub repository, and like a skilled archivist, catalogs its contents into a structured JSON file. But wait - there’s more! It can also transform that JSON into a sleek and stylish README.md, because who doesn’t love a good README?

## Setting Up Your Gear 🛠️✨

Embark on your coding quest with GitRepoScraper, your digital scroll to unravel the mysteries of GitHub repositories. But first, a preparation ritual is required:

## Prerequisites 🗝️

Ensure the presence of Python 3.11 or higher in your armory. Should you find yourself without it, fear not! Acquire it from the hallowed halls of [python.org](https://www.python.org/downloads/).

## Cloning the Repository 📜

Invoke the clone spell to replicate the repository into your local realm:

```bash
git clone https://github.com/gui25/GitRepoScraper.git
```

## Installation Incantation 🧙‍♂️

With the repository cloned, venture into the GitRepoScraper directory with a swift command:

```bash
cd GitRepoScraper
```

Now, summon the setup.py script to weave the necessary enchantments and bind the project and its dependencies to your environment:

```bash
python setup.py install
```

## Commencing the Quest 🗺️

Summon the Repo Scraper with the ancient incantation:

```bash
python main.py --owner exampleOwner --repo exampleRepo --branch exampleBranch --generate-readme
```

And you must give our sacred `owner`, `repo`, and `branch` names. Fear not, for it shall guide you through the process with the wisdom of ages, if you wish to conjure a README.md doc file you can include `--generate-readme`, then a README shall be brought into existence.

## The Repository Reliquary 🗃️

Your treasures, the JSON and Markdown files, shall rest within the sacred `data/results_json` and `data/results_md` chambers, ready for you to peruse at your leisure.

## Farewell and Good Fortune! 🎉

And now, brave coder, go forth with this arcane tool at your command. May your repositories always be organized, and your READMEs be ever readable!

Made with ❤️ and a sprinkle of magic by Gui25
