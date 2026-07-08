#!/usr/bin/env python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda x: x["power"] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda n: '* ' + n + ' *', spells)


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = round(sum(m["power"] for m in mages) / len(mages), 2)
    return {
        "max_power": max_power, 
        "min_power": min_power, 
        "avg_power": avg_power
        }


def display(lst: dict):
    for dct in lst:
        print(dct)


def test_sorter() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "artifact"},
    ]
    print("Testing artifact sorter...")
    sorted_list = artifact_sorter(artifacts)
    for i in range(len(sorted_list) - 1):
        a, b = sorted_list[i], sorted_list[i + 1]
        print(f"{a['name']} ({a['power']} power) comes before {b['name']} ({b['power']} power)")


def test_filter() -> None:
    lst = [
        {"name": "Samuel", "power": 3, "type": "weapon"},
        {"name": "Ark", "power": 1, "type": "tool"},
        {"name": "Sam", "power": 9, "type": "artifact"},
        {"name": "Bob", "power": 54, "type": "relic"},
    ]
    print("\nTesting power filter...")
    filtered_list = power_filter(lst, 4)
    display(filtered_list)


def test_transformer() -> None:
    lst = [
        "Fireball",
        "Lighting",
        "Laser"
    ]
    print("\nTesting spell transformer...")
    transformed = spell_transformer(lst)
    print(" ".join(transformed))


def test_stats() -> None:
    lst = [
        {"name": "Sword", "power": 3, "type": "weapon"},
        {"name": "Wand", "power": 1, "type": "tool"},
        {"name": "Orb", "power": 9, "type": "artifact"},
        {"name": "Crown", "power": 54, "type": "relic"},
    ]
    print("\nTesting mage stats...")
    stats_list = mage_stats(lst)
    print(stats_list)


def main() -> None:
    test_sorter()
    test_filter()
    test_transformer()
    test_stats()


if __name__ == "__main__":
    main()
