import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.examples.a_example import tests_devprocess
#from tests.examples.c_decisions import tests_decisions
#from tests.examples.h_strings import tests_strings
from tests.examples.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)
