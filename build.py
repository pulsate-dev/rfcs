import os
import shutil

def main():
    shutil.copytree("proposals/", "src/", dirs_exist_ok=True)

    with open("src/SUMMARY.md", "w") as f:
        f.write("# Summary\n")
        f.write("[Introduction to RFCs](./introduction.md)\n")
        f.write("[How to submit proposals](./how-to.md)\n")
        f.write("----\n\n")

        for p in os.listdir('proposals'):
            f.write(f"* [{p}](./{p})\n")

if __name__ == '__main__':
    main()
