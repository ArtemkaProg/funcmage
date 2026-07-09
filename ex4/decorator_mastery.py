from functools import wraps
from typing import Callable, Any
import time
    

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        time.sleep(1)
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get('power', args[0] if args else None)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def retry(*args, **kwargs) -> Any:
            count = 0
            while count < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    count += 1
                    if count == max_attempts:
                        return f"Spell casting failed after {count} attempts"
                    print(f"Spell failed, retrying... (attempt {count}/{max_attempts})")
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)
    
    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")
    fireball_timer = spell_timer(fireball)
    print(f"Result: {fireball_timer("Knight", 20)}")

    print("\nTesting power validator...")
    temp_decorator = power_validator(8)
    result = temp_decorator(fireball)
    print(result(20, "Knight"))

    print("\nTesting retry spell...")
    temp_decorator = retry_spell(3)
    result = temp_decorator(fireball)
    print(result(15))

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_name('Lighting'))
    print(guild.validate_name('Fireball2'))
    print(guild.cast_spell('Fireball', power=15))
    print(guild.cast_spell('Lighting', power=8))


if __name__ == "__main__":
    main()
