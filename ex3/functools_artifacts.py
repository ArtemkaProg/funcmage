from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": add,
        "multiply": mul,
        "min": min,
        "max": max
    }
    if not spells:
        return 0
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(ops[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power} power) cast on {target}"


def partial_enchanter(
        base_function: Callable
        ) -> dict[str, Callable]:
    fire = partial(base_function, power=50, element="Fire")
    water = partial(base_function, power=50, element="Water")
    ice = partial(base_function, power=50, element="Ice")
    return {
        "fire": fire,
        "water": water,
        "ice": ice
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(power: int) -> str:
        return f"Damage spell: {power} damage"

    @cast.register
    def _(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @cast.register
    def _(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"
    
    return cast
    


def test_spell_reducer() -> None:
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([3, 4, 5], 'add')}")
    print(f"Product: {spell_reducer([3, 4, 5], 'multiply')}")
    print(f"Max: {spell_reducer([3, 4, 5], 'max')}")

    try:
        spell_reducer([3, 4, 5], "divide")
    except ValueError as e:
        print(f"Error: {e}")


def test_partial_enchanter() -> None:
    print("\nTesting partial enchanter...")
    functions = partial_enchanter(base_enchantment)
    print(functions["fire"](target="Dragon"))
    print(functions["water"](target="Knight"))
    print(functions["ice"](target="Raider"))


def test_memoized_fibonacci() -> None:
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0):  {memoized_fibonacci(0)}")
    print(f"Fib(1):  {memoized_fibonacci(1)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(60): {memoized_fibonacci(60)}")
    print(memoized_fibonacci.cache_info())


def test_spell_dispatcher() -> None:
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(5))
    print(dispatcher("Fireball"))
    print(dispatcher(["Fire", "Ice", "Lighting"]))
    print(dispatcher(3.14))


def main() -> None:
    test_spell_reducer()
    test_partial_enchanter()
    test_memoized_fibonacci()
    test_spell_dispatcher()


if __name__ == "__main__":
    main()
