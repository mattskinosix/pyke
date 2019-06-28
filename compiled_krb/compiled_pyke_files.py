# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'regole2.krb'):
           [1561714839.443961, 'regole2_plans.py', 'regole2_bc.py'],
         ('', '', 'user_questions.kqb'):
           [1561714839.4535275, 'user_questions.qbc'],
         ('', '', 'fatti.kfb'):
           [1561714839.461387, 'fatti.fbc'],
        },
        compiler_version)

