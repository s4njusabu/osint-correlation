import argparse

# Basic workflow of the application
def main():
    parser = argparse.ArgumentParser(
        description="Cyber Sentries Open-Source Intelligence tool"
    )
    parser.add_argument("action", help='Action to perform eg: "USERNAME" or "EMAIL"')
    parser.add_argument("target", help='Target to find eg: "sanjusabu" or "sanjusabu@example.com"')

    args = parser.parse_args()

    print(f"action: {args.action}")
    print(f"target: {args.target}")

if __name__ == "__main__":
    main()