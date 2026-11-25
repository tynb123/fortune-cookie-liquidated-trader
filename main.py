import os

FORTUNE = "The stars foretold riches, trader. They did not say the riches would belong to the exchange."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(FORTUNE)

if __name__ == "__main__":
    main()
