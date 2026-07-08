from typing import Callable


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate(power: int) -> int:
        nonlocal initial_power
        return initial_power + power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchance(item: str) -> str:
        return enchantment_type + " " + item
    return enchance


def memory_vault() -> dict[str, Callable]:
    vault = {}
    def store(key: str, value: int):
        vault[key] = value

    def recall(key: str):
        if key in vault:
            return vault[key]
        return "Memory not found"
    
    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    print(flaming("Sword"))
    frozen = enchantment_factory("Frozen")
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()