import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal, ask_wx

engine = knowledge_engine.engine(__file__)

def bc_test_diagnostic():
    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc_diagnostic_questions')  # Runs all questions for diagnostic
    print("Realizando diagnostico...")
    with engine.prove_goal('bc_diagnostic_questions.give_me_diagnostic($diagnostic)') as gen:
        for vars, plan in gen:
            print("El diagnostico es: {}".format(vars['diagnostic']))
