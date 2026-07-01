from datetime import datetime


APP_NAME = "ReleaseRadar"
VERSION = "0.1.0"


def main():
    print("=" * 50)
    print(f"{APP_NAME} v{VERSION}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


if __name__ == "__main__":
    main()