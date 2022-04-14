import argparse

from .truerandom import true_passwords

parser = argparse.ArgumentParser(
    description='Create a csv file containing generated passwords.')
parser.add_argument('--nb', type=int, default=100,
                    help='number of passwords to generate')
parser.add_argument('--length', type=int, default=12,
                    help='length of passwords')
parser.add_argument('--csv', type=str,
                    help='CSV filepath where to write passwords')
parser.add_argument('--punctuation', type=bool, default=True,
                    help='Password has punctuation')
parser.add_argument('--digits', type=bool, default=True,
                    help='Password has digits')
parser.add_argument('--uppercase', type=bool, default=True,
                    help='Password has uppercase letters')

args = parser.parse_args()
true_passwords(
    nb=args.nb,
    csv_output=args.csv,
    length=args.length,
    has_punctuation=args.punctuation,
    has_uppercase_letters=args.uppercase,
    has_digits=args.digits
)
