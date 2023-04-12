"""Virtual interactive closet that allows a user to choose their outfit based
on the weather."""

from argparse import ArgumentParser
import json


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.weather, args.tops, args.pants, args.shoes, 
         args.accessories)
