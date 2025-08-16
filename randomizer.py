import random
import os
import sys

from typing import List

class Randomizer:

    def __init__(self, file_name: str = "names.txt") -> None:
        self.file_name = file_name
        self.content: List[str] = []
        self._load_content()

    def _load_content(self) -> None:
        if not os.path.exists(self.file_name):
            raise FileNotFoundError(f"Input file {self.file_name} not found")

        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines()]
                
            self.content = [name for name in lines if name and len(name) > 3]
            
            if not self.content:
                raise ValueError(f"No valid names found in {self.file_name}.")

        except UnicodeDecodeError as e:
            raise ValueError(f"Could not read file {self.file_name}: {e}")

    def randomize_list(self) -> None:
        if not self.content:
            raise ValueError("No content to randomize.")
        random.shuffle(self.content)

    def prepare_output_list(self, output_file: str = "randomized.txt") -> None:
        if not self.content:
            raise ValueError("No content to write. Please load names first.")
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                for i, name in enumerate(self.content, 1):
                    f.write(f"{i}. {name}\n")
                    if i % 2 == 0:
                        f.write("\n")

            print(f"Successfully created {output_file} with randomized names.")
        except IOError as e:
            raise IOError(f"Could not write to file {output_file}: {e}")


def main():
    try:
        input_file = sys.argv[1] if len(sys.argv) > 1 else "names.txt"
        output_file = sys.argv[2] if len(sys.argv) > 2 else "randomized.txt"

        print(f"Randomizer starting... \nInput file: {input_file}\nOutput file: {output_file}")

        randomizer = Randomizer(input_file)
        randomizer.randomize_list()
        randomizer.prepare_output_list(output_file)
        
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
