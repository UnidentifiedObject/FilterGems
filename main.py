import requests
import json

CATEGORIES = {
    "1": "optimization", "2": "utility", "3": "adventure",
    "4": "magic", "5": "technology", "6": "decoration",
    "7": "worldgen", "8": "equipment", "0": "None"
}

LOADERS = {
    "1": "fabric", "2": "forge", "3": "neoforge", "4": "quilt", "0": "Any"
}


def search_mods():
    print("=" * 55)
    print("💎  MODRINTH HIDDEN GEM HUNTER v6.0  💎")
    print("=" * 55)

    version = input("🎮 Minecraft Version (e.g. 1.20.1): ") or "1.20.1"

    # Loader Selection
    print("\n--- Mod Loader ---")
    print(" [1] Fabric | [2] Forge | [3] NeoForge | [4] Quilt | [0] Any")
    loader_num = input("Select loader: ") or "0"
    selected_loader = LOADERS.get(loader_num, "Any")

    min_dl = input("\n📉 Min Downloads: ") or "5000"
    max_dl = input("📈 Max Downloads: ") or "50000"

    # Category Selection
    print("\n--- Categories ---")
    for k, v in CATEGORIES.items():
        print(f" [{k}] {v.capitalize()}", end=" | " if int(k) % 3 != 0 else "\n")
    cat_num = input("\nSelect category: ") or "0"
    selected_cat = CATEGORIES.get(cat_num, "None")

    limit = input("\n🔢 Results to show: ") or "10"

    # Build API Logic
    facets = [
        [f"versions:{version}"],
        ["project_type:mod"],
        [f"downloads >= {min_dl}"],
        [f"downloads <= {max_dl}"]
    ]

    if selected_loader != "Any":
        facets.append([f"categories:{selected_loader}"])
    if selected_cat != "None":
        facets.append([f"categories:{selected_cat}"])

    # No 'index' parameter means the API uses its default 'Relevance' mix
    params = {
        "facets": json.dumps(facets),
        "limit": limit
    }

    headers = {"User-Agent": "UnidentifiedObject/FilterGems/1.6"}

    try:
        response = requests.get("https://api.modrinth.com/v2/search", params=params, headers=headers)
        data = response.json()

        print(f"\n✅ Showing {len(data['hits'])} results in the {min_dl}-{max_dl} range:")
        print("-" * 55)

        for hit in data['hits']:
            print(f"📦 {hit['title'].upper()}")
            print(f"   👤 Author: {hit.get('author', 'Unknown')}")
            print(f"   📥 Total Downloads: {hit['downloads']:,}")
            print(f"   🔗 https://modrinth.com/mod/{hit['slug']}")
            print("-" * 55)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":

    search_mods()
