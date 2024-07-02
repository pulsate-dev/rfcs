import os
import shutil


def main():
    if os.path.exists("src"):
        shutil.rmtree("src")
    os.mkdir("src")

    shutil.copytree("rfcs/", "src/rfcs/", dirs_exist_ok=True)
    shutil.copytree("books/", "src/", dirs_exist_ok=True)

    with open("src/SUMMARY.md", "w") as f:
        f.write("[Introduction to RFCs](./introduction.md)\n")
        f.write("[How to submit proposals](./how-to.md)\n\n")
        f.write("----\n\n")

        for p in sorted(os.listdir('rfcs')):
            if p.endswith(".md"):
                f.write(f"[{p}](./rfcs/{p})\n")

if __name__ == '__main__':
    main()
