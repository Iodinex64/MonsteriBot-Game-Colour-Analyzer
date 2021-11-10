# MonsteriBot-Game-Colour-Analyzer
A program that pulls the top 100 games of each specified genre from IGDB, gets their images and analyzes their average colours.

# Setup:

### You will need to first install some required packages.
`pip install requests colorthief matplotlib PIL seaborn`

# To use:

### In the commandline:
`python getimages.py <IGDB client ID> <IGDB client secret> <images per genre to analyze>`
### then run
`python analyzeimages.py`

Special thanks to Crypdos for helping with the requests part of getimages.py
