import os


def sourcefiles(path) -> int:
    # Counts the number of files in individual source codes
    return len([file for (root, subdirectories, files) in os.walk(path) for file in files if file.endswith(".java")])


if __name__ == "__main__":
    print(sourcefiles(
        "/Users/Gabriel/Documents/research/data_source/sc1/addressbook-level2-1.0"))
