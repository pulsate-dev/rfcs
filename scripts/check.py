import os
import fnmatch

def main():
    for p in os.listdir('rfcs'):
        if fnmatch.fnmatch(p, "0000-*.md"):
            if p == "0000-proposal-example.md":
                continue
            print(f"Error: {p} is not a valid RFC filename")
            exit(1)

if __name__ == '__main__':
    main()
