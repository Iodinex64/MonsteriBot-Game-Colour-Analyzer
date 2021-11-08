import requests
import sys
from pathlib import Path

# Genres we want
genre_ids = [
    4,  # fighting
    5,  # shooter
    8,  # platformer
    10,  # racing
    12,  # RPG
    36  # MOBA
]

# Twitch client details
CLIENT_ID = sys.argv[1]
CLIENT_SECRET = sys.argv[2]
imgAmount = sys.argv[3]

# Acquire auth key from Twitch servers
response = requests.post(
    f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")
ACCESS_TOKEN = response.json()["access_token"]
print("Access token: " + ACCESS_TOKEN)

def download_image(image_id, size: str = "thumb"):
    '''
    Image sizes:

    cover_small	90 x 128	Fit
    screenshot_med	569 x 320	Lfill, Center gravity
    cover_big	264 x 374	Fit
    logo_med	284 x 160	Fit
    screenshot_big	889 x 500	Lfill, Center gravity
    screenshot_huge	1280 x 720	Lfill, Center gravity
    thumb	90 x 90	Thumb, Center gravity
    micro	35 x 35	Thumb, Center gravity
    720p	1280 x 720	Fit, Center gravity
    1080p	1920 x 1080	Fit, Center gravity
    '''

    url = f"https://images.igdb.com/igdb/image/upload/t_{size}/{image_id}.jpg"
    r = requests.get(url)
    if r.status_code == 200:
        return r.content
    else:
        raise ConnectionError


def store_image(image, genre, filename):
    p = Path(f"images/{genre}/")
    p.mkdir(parents=True, exist_ok=True)
    filepath = p / filename
    with filepath.open("wb") as f:
        f.write(image)


# Get artwork of the top 100 games in the specified genre, get each artworks 3 most common colour values,
# average them all and put them in a graph. repeat for each genre.
for genre in genre_ids:
    # Post for top 100 games in the specified genre
    headers = {"Client-ID": CLIENT_ID, "Authorization": "Bearer " + ACCESS_TOKEN}
    # data = f"fields artworks.image_id; sort rating desc; where genres = {genre}; where artworks.image_id != null; limit {imgAmount};"
    # data = f"fields *; where id = 1942;"
    data = f"fields artworks.url, artworks.image_id, artworks.height, artworks.width; sort rating desc; where genres = {genre} & artworks.image_id != null; limit {imgAmount};"
    r = requests.post('https://api.igdb.com/v4/games/', data=data, headers=headers)
    response = r.json()
    if r.status_code == 200:
        for artworks in response:
            for artwork in artworks['artworks']:
                img = download_image(artwork['image_id'])
                store_image(img, genre, artwork['image_id'] + '.jpg')
    print(response)


