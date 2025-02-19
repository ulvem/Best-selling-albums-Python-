from datetime import datetime
bestSellingAlbums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]

# WRITE YOUR CODE HERE

# Calculate the average sales income
total_sales = sum(album["sale"] for album in bestSellingAlbums)
average_sale = total_sales / len(bestSellingAlbums)

print(average_sale)

# Store the current year
current_year = datetime.now().year

# Calculate the average age of the albums
total_age = sum(current_year - album["year"] for album in bestSellingAlbums)
average_age = total_age / len(bestSellingAlbums)

print(average_age)

# Find the newest and oldest albums
newest_album = max(bestSellingAlbums, key=lambda album: album["year"])
oldest_album = min(bestSellingAlbums, key=lambda album: album["year"])

print("Newest Album:", newest_album)
print("Oldest Album:", oldest_album)

# Filter Eagles albums
eagles_albums = [album for album in bestSellingAlbums if album["artist"] == "Eagles"]

# Calculate total sales
total_sales = sum(album["sale"] for album in eagles_albums)

# Check if both albums are classified under "soft rock"
is_both_soft_rock = all("soft rock" in album["genres"] for album in eagles_albums)

# Create the dictionary
albums_eagles = {
    "sales": total_sales,
    "is_both_soft_rock": is_both_soft_rock
}

print(albums_eagles)

# Add the new album
new_album = {
    "artist": "The Beatles",
    "title": "Abbey Road",
    "year": 1969,
    "genres": ["rock"],
    "sale": 31000000,
}

bestSellingAlbums.append(new_album)

print(bestSellingAlbums)

# Add the i_like_it key to each album
for album in bestSellingAlbums:
    album["i_like_it"] = True  # or False, depending on your preference

print(bestSellingAlbums)


