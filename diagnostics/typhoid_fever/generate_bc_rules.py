#!/usr/bin/env python3

import sys
import re
from itertools import combinations

if len(sys.argv) != 2:
    print("Usage: {} <questions.kqb>".format(sys.argv[0]))
    sys.exit(1)

def read_questions(filename):
    questions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
    
            if line.startswith('#'):
                continue
    
            rex = re.compile("^(?P<question>\w+)\(.*\)$")
            s = rex.search(line)
            if s:
                questions.append(s.group('question'))

    return questions

questions = read_questions(sys.argv[1])

# Next rules generation for typhoid fever diagnostic
# Following the rules if has from 5-9 is cold

index = 1
for c in combinations(questions, 5):
    print("have_patient_typhoid_fever_{}".format(index))
    print("    use have_patient_typhoid_fever()")
    print("    when")
    for q in c:
        print("        questions.{}(True)".format(q))
    print("")
    index = index + 1
