"""Console script for rrsdk."""

import fire


def help():
    print("rrsdk")
    print("=" * len("rrsdk"))
    print("Skeleton project created by Python Project Wizard (ppw)")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
