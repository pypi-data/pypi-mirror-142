import argparse
from . import jmap


LOOKUP_TABLES = {
    "smg": jmap.SuperMarioGalaxyHashTable,
    "dkjb": jmap.JungleBeatHashTable,
    "lm": jmap.LuigisMansionHashTable
}


def dump(args):
    data = jmap.from_file(LOOKUP_TABLES[args.lookup](), args.jmap, not args.little_endian)
    jmap.dump_csv(data, args.csv)
    print("Successfully dumped data to CSV file.")


def pack(args):
    data = jmap.from_csv(LOOKUP_TABLES[args.lookup](), args.csv)
    jmap.write_file(data, args.jmap, not args.little_endian)
    print("Successfully packed JMap data.")


def main():
    parser = argparse.ArgumentParser(description="")
    subs = parser.add_subparsers(dest="command", help="Command")
    subs.required = True

    dump_parser = subs.add_parser("tocsv", description="Dump JMap data to CSV file.")
    pack_parser = subs.add_parser("tojmap", description="Pack CSV file as JMap data.")

    for sub_parser in [dump_parser, pack_parser]:
        sub_parser.add_argument("-le", "--little-endian", action="store_true", help="Is little endian? Usually false.")
        sub_parser.add_argument("lookup", choices=["smg", "dkjb", "lm"], help="The hash lookup table to use.")

    dump_parser.add_argument("jmap", help="Path to JMap data.")
    dump_parser.add_argument("csv", help="Path to CSV file.")
    dump_parser.set_defaults(func=dump)

    pack_parser.add_argument("csv", help="Path to CSV file.")
    pack_parser.add_argument("jmap", help="Path to JMap data.")
    pack_parser.set_defaults(func=pack)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
