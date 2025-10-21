import sys
from .parser import parse


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: fileparser <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        info = parse(filename)
        print(f"File name: {info.name}")
        print(f"Suffix:    {info.suffix}")
        print(f"Type:      {info.type}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
