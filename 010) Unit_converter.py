import sys
from typing import Dict, List, Callable, Tuple

class LinearConverter:
    """
    Handles standard linear conversions using a centralized base-unit dictionary.
    """
    def __init__(self, base_unit: str, units_dict: Dict[str, float]):
        self.base_unit = base_unit
        self.factors = units_dict

    def get_supported_units(self) -> List[str]:
        return list(self.factors.keys())

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.factors or to_unit not in self.factors:
            raise KeyError("Unsupported unit provided.")
        
        # Step 1: Convert to base unit
        value_in_base = value * self.factors[from_unit]
        # Step 2: Convert from base unit to target unit
        return value_in_base / self.factors[to_unit]


class TemperatureConverter:
    """
    Handles non-linear conversions specific to Temperature (Celsius, Fahrenheit, Kelvin).
    """
    def __init__(self):
        # Maps target units to functions that convert FROM Celsius
        self._from_celsius_map: Dict[str, Callable[[float], float]] = {
            "C": lambda c: c,
            "F": lambda c: (c * 9/5) + 32,
            "K": lambda c: c + 273.15
        }
        # Maps source units to functions that convert TO Celsius
        self._to_celsius_map: Dict[str, Callable[[float], float]] = {
            "C": lambda c: c,
            "F": lambda f: (f - 32) * 5/9,
            "K": lambda k: k - 273.15
        }

    def get_supported_units(self) -> List[str]:
        return list(self._from_celsius_map.keys())

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self._to_celsius_map or to_unit not in self._from_celsius_map:
            raise KeyError("Unsupported temperature unit.")
            
        # Standardize through Celsius base
        celsius_val = self._to_celsius_map[from_unit](value)
        return self._from_celsius_map[to_unit](celsius_val)


class UnitConverterApp:
    """
    Orchestrates the terminal user interface and initializes conversion configurations.
    """
    def __init__(self):
        # Configure the conversion registries
        self.categories = {
            "1": ("Length", LinearConverter("meters", {
                "m": 1.0, "km": 1000.0, "cm": 0.01, "mm": 0.001, 
                "mi": 1609.344, "yd": 0.9144, "ft": 0.3048, "in": 0.0254
            })),
            "2": ("Weight", LinearConverter("kilograms", {
                "kg": 1.0, "g": 0.001, "mg": 0.000001, "lb": 0.45359237, "oz": 0.028349523
            })),
            "3": ("Temperature", TemperatureConverter()),
            "4": ("Speed", LinearConverter("m/s", {
                "m/s": 1.0, "km/h": 0.277777778, "mph": 0.44704, "knot": 0.514444
            })),
            "5": ("Time", LinearConverter("seconds", {
                "s": 1.0, "min": 60.0, "hr": 3600.0, "day": 86400.0
            }))
        }

    def display_menu(self) -> None:
        print("\n" + "="*40)
        print("       PROFESSIONAL UNIT CONVERTER       ")
        print("="*40)
        for key, (name, _) in self.categories.items():
            print(f" {key}. {name}")
        print(" 6. Exit")
        print("="*40)

    def run(self) -> None:
        while True:
            self.display_menu()
            choice = input("Select a conversion category (1-6): ").strip()

            if choice == "6":
                print("\nThank you for using Unit Converter. Goodbye!")
                sys.exit()

            if choice not in self.categories:
                print("❌ Invalid entry. Please choose a valid menu number.")
                continue

            category_name, converter = self.categories[choice]
            units = converter.get_supported_units()

            print(f"\n--- {category_name} Conversion ---")
            print(f"Supported Units: {', '.join(units)}")
            
            try:
                from_unit = input("Enter source unit: ").strip()
                to_unit = input("Enter target unit: ").strip()
                
                if from_unit not in units or to_unit not in units:
                    print("❌ Error: One or both units are not supported in this module.")
                    continue
                
                value_str = input(f"Enter value in [{from_unit}]: ").strip()
                value = float(value_str)
                
                # Execute conversion calculation
                result = converter.convert(value, from_unit, to_unit)
                
                print("\n" + "-"*30)
                print(f"✅ Result: {value} {from_unit} = {result:.4f} {to_unit}")
                print("-"*30)

            except ValueError:
                print("❌ Input Error: Please enter a valid numerical value.")
            except Exception as e:
                print(f"❌ An unexpected structural error occurred: {e}")

            input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    app = UnitConverterApp()
    app.run()
