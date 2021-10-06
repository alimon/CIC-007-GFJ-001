import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal, ask_wx


engine = knowledge_engine.engine(__file__)

def run():
    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc_rules')  # Runs all questions for diagnostic
    print("Realizando diagnostico...")

    diagnostics = []
    try:
        vars, plan = engine.prove_1_goal('bc_rules.have_patient_cold()')
        diagnostics.append("Resfriado")
    except knowledge_engine.CanNotProve as e:
        pass

    try:
        vars, plan = engine.prove_1_goal('bc_rules.have_patient_influenza()')
        diagnostics.append("Influenza")
    except knowledge_engine.CanNotProve as e:
        pass

    if diagnostics:
        print("Posibles diagnosticos en el paciente: {}.".format(', '.join(diagnostics)))

if __name__ == '__main__':
    run()
