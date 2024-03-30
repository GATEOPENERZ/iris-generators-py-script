import os
import random

def generate_random_name():
    words = [
        "mountain", "peak", "ridge", "highland",
        "summit", "elevation", "promontory", "plateau",
        "knoll", "massif", "butte", "crag",
        "plains", "flatlands", "fields", "meadows",
        "prairie", "savannah", "steppe", "tundra",
        "grassland", "pasture", "pampas", "veldt",
        "desert", "wasteland", "barrens", "badlands",
        "moor", "heath", "scrubland", "wilderness",
        "hilly", "undulating", "rolling", "mounded",
        "bumpy", "lumpy", "rounded", "humpbacked",
        "dunes", "sands", "drifts", "banks",
        "mounds", "hillocks", "duneland", "sandbanks",
        "arctic", "polar", "glacial", "icy",
        "subzero", "wintry", "nippy", "gelid",
        "frozen", "chilled", "frigid", "frosty",
        "cold", "icebound", "snowy", "algid",
        "twilight", "dusk", "evening", "sunset",
        "nightfall", "gloaming", "eventide", "sundown",
        "vale", "valley", "glen", "ravine",
        "gorge", "canyon", "gully", "dell",
        "brook", "stream", "river", "creek",
        "waterfall", "cascade", "cataract", "rapids",
        "forest", "woodland", "jungle", "grove",
        "thicket", "brushwood", "copse", "bushland",
        "coast", "shoreline", "seaside", "beach",
        "cliff", "bluff", "escarpment", "ledge",
        "volcano", "crater", "caldera", "cone",
        "lava", "magma", "pyroclastic", "vent",
        "oasis", "haven", "retreat", "sanctuary",
        "bog", "swamp", "marsh", "fen",
        "quagmire", "morass", "mire", "slough",
        "lagoon", "bayou", "pond", "pool",
        "atoll", "islet", "isle", "island",
        "peninsula", "isthmus", "promontory", "cape",
        "delta", "estuary", "fjord", "inlet",
        "strait", "channel", "passage", "sound",
        "plateau", "mesa", "tableland", "upland",
        "terrain", "landscape", "topography", "geography",
        "horizon", "skyline", "vista", "panorama"         
    ]
    word1, word2 = random.sample(words, 2)
    return f"{word1}-{word2}.json"

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            new_name = generate_random_name()
            while new_name in os.listdir(directory): 
                new_name = generate_random_name()
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")


directory = r"Your\Path" # Your path goes here, if you are using / slashes, remove the prefix "r" before the double quotes.
rename_files_in_directory(directory)
