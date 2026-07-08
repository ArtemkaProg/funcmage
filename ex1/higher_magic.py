from typing import Callable


def heal(target: str, power: int) -> str:
    return f"{target} heals for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def has_enough_power(_target: str, power: int) -> bool:
    return power >= 10


def spell_combiner(spell1, spell2) -> Callable:
    def combined(target, power) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable):
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def spell_sequence(spells):
    def sequence(target, power):
        res = []
        for spell in spells:
            res.append(spell(target, power))
        return res
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Arthur", 20)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power multiplier...")
    amplified = power_amplifier(heal, 2)
    print(f"Original: {heal('Arthur', 15)}, Amplified: {amplified('Arthur', 15)}")

    print("\nTesting conditional caster...")
    careful_fireball = conditional_caster(has_enough_power, fireball)
    print(f"Condition - True:  {careful_fireball("Dragon", 20)}")
    print(f"Condition - False: {careful_fireball("Dragon", 5)}")

    print("\nTesting spell sequence")
    sequence = spell_sequence((fireball, heal, has_enough_power))
    print(sequence("Arthur", 50))


if __name__ == "__main__":
    main()