import sys
import os
import re
import pprint

def process_file(name, f):
    """
    Takes in a filename along with the file object and scans its contents against regex patterns.
    Returns a list of (filename, type, value) tuples where type is either an 'e' or a 'p'
    for e-mail or phone, and value is the formatted phone number or e-mail.

    The canonical formats are:
        (name, 'p', '###-###-#####')
        (name, 'e', 'someone@something')

    If the numbers you submit are formatted differently they will not match the gold answers.

    XXX: DO NOT change the inputs and outputs of process_file
    NOTE: Debug info should be printed to stderr
    `sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))`

    TODO: Change only the internals of this function. The assigment is modify and add lines.
    """

    dummy_pattern = r'(\w+)@(\w+).edu' # TODO: Create your own patterns for email & phone

    results = []
    for line in f:
        matches = re.findall(dummy_pattern, line)
        for match in matches:
            email = '{}@{}.edu'.format(*match)
            results.append((name,'e',email))

        # TODO: Create a section for phone matches

    return results

def process_dir(data_path):
    """XXX: DO NOT MODIFY THIS FUNCTION"""

    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r', encoding="latin-1")
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

def get_gold(gold_path):
    """XXX: DO NOT MODIFY THIS FUNCTION

    Given a path to a tsv file of gold e-mails and phone numbers
    this function returns a list of tuples of the canonical form:
    (filename, type, value)
    """
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

def score(guess_list, gold_list):
    """ XXX: DO NOT MODIFY THIS FUNCTION

    Given a list of guessed contacts and gold contacts, this function
    computes the intersection and set differences, to compute the true
    positives, false positives and false negatives.  Importantly, it
    converts all of the values to lower case before comparing
    """

    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))


def main(data_path, gold_path):
    """ XXX: DO NOT MODIFY THIS FUNCTION

    Takes in the string path to the data directory and the gold file
    """
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

if __name__ == '__main__':
    """ The commandline interface takes a directory name and gold file.
    $ python spam_lord.py data/dev/ data/devGOLD

    It then processes each file within that directory and extracts any
    matching e-mails or phone numbers and compares them to the gold file
    """
    if (len(sys.argv) != 3):
        print('usage:\tSpamLord.py <data_dir> <gold_file>')
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])
