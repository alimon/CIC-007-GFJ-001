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

# Next rules generation for cold and influenza diagnostic
# Following the rules if has from 4-8 is cold
# Following the rules if has from 2 + influenza is cold

# XXX: Suppose that last question is the influenza one
influenza_question = questions.pop(-1)

index = 1
for c in combinations(questions, 4):
    print("have_patient_cold_{}".format(index))
    print("    use have_patient_cold()")
    print("    when")
    for q in c:
        print("        questions.{}(True)".format(q))
    print("")
    index = index + 1

index = 1
for c in combinations(questions, 4):
    print("have_patient_influenza_{}".format(index))
    print("    use have_patient_influenza()")
    print("    when")
    for q in c:
        print("        questions.{}(True)".format(q))
    print("        questions.have_diarrhea(True)")
    print("")
    index = index + 1
