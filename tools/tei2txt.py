from pathlib import Path
from tqdm import tqdm
from bs4 import BeautifulSoup

DEST_PATH = "./txt0"
BLOCK_LIST = [
            "saritcorpus.xml",
            "00-sarit-tei-header-template.xml"
        ]


def tei2txt(tei_file, dest_dir):
    tei_path = Path(tei_file)
    txt_path = dest_dir / (tei_path.stem + ".txt")
    if txt_path.is_file():
        return
    with open(tei_path, 'r') as tei:
        soup = BeautifulSoup(tei, 'lxml')
        try:
            text = soup.find("text").getText(separator=' ')
            with open(txt_path, "w+") as txt:
                txt.write(text)
        except AttributeError as e:
            print(tei_path.stem + ": " + str(e))


if __name__ == "__main__":
    dest_dir = Path(DEST_PATH)
    dest_dir.mkdir(exist_ok=True)
    for p in tqdm(Path("./").glob("*.xml")):
        if p.name not in BLOCK_LIST:
            tei2txt(p, dest_dir)