import sys
import os
import re
import pprint

# Less elegant but still works"
ph = "\(?(\d{3})[\)\s\.-]+(\d{3})[\s\.-](\d{4})"       # phone pattern 
      
p1 = "([\w\.]+)\s?@\s?([\w.]+)\.([a-zA-Z]{3})"  # email patterns   
p2 = "^([\D\-]+)@-([\D\-]+)\S" 
p3 = "<address>(\w+) WHERE (\w+) DOM (edu)"
p4 = "E-?mail: (\w+)[\s@at]+(c?s?.?stanford)[dot\.\s]+([a-zA-Z]{3})"
p5 = "([\w\.]+) \(followed by[\s\"&a-z;]+@([\.\w]+).(edu)"
p6 = "([\w\.]+)&#x40;([\.\w]+).(edu)"
p7 = "(\w+) at (\w+)[\s;]d?o?t?\s?(\w+)\s?d?o?t?\s?;?(edu)"
p8 = "mail[\sto:]+(\w+)[%20\sat]+(gradiance|stanford)[%20dot\s]+([a-zA-Z]{3})"
p9 = "obfuscate\('(\w+).([a-zA-Z]{3})','(\w+)'(\))(;)"
patterns_email = [p1, p2, p3, p4, p5, p6, p7, p8, p9]


def process_file(name, f):
    res = []
    for line in f:

        matches = re.findall(ph,line)        # find all phone numbers 
        for m in matches:
            phone = '%s-%s-%s' % m
            res.append((name,'p',phone.strip()))

        for i in patterns_email:               # find emails 
            matches2 = re.findall(i,line)
            for m2 in matches2:
                if len(m2) == 3:                    # general case, grabs most emails.
                    email = '%s@%s.%s' % m2
                    res.append((name,'e',email.strip()))
                if len(m2) == 2:                     # grabs just the email with all the dashes
                    email = '%s@%s.edu' % (m2[0][0:7:2],m2[1][0:-6:2])
                    res.append((name,'e',email.strip('-')))
                if len(m2) == 4:                      # grabs emails with "dot" in them
                    if m2[2] != 't':
                        email = '%s@%s.%s.%s' % m2
                        res.append((name,'e',email))
                if len(m2) == 5:                      # grabs the one email that is out of order
                    email = '%s@%s.%s' % (m2[2], m2[0], m2[1])
                    res.append((name,'e',email))
            
    return res



def process_dir(data_path):
    "XXX: DO NOT MODIFY THIS FUNCTION"

    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path, fname)
        f = open(path, 'r', encoding="latin-1")
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
    f_gold = open(gold_path, 'r')
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
    # print 'Guesses (%d): ' % len(guess_set)
    # pp.pprint(guess_set)
    # print 'Gold (%d): ' % len(gold_set)
    # pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp), len(fp), len(fn)))


def main(data_path, gold_path):
    """ XXX: DO NOT MODIFY THIS FUNCTION

    Takes in the string path to the data directory and the gold file
    """
    guess_list = process_dir(data_path)
    gold_list = get_gold(gold_path)
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
    main(sys.argv[1], sys.argv[2])
