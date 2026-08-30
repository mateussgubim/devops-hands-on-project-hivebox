import os
import sys

VERSION = os.getenv("APP_VERSION")

def main(version: str) -> str:
    return version

if __name__ == "__main__":
    print(main(VERSION))
