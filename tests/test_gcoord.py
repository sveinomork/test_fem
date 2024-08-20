import pytest
from vectormath import Vector3

import os


import sys,os
sys.path.append(r'C:\Users\372749\test_module\test_fem')
from test_fem.fem.fem import FEM

@pytest.fixture
def test_file(tmpdir):
    # Create a temporary file with sample content
    data_lines = [
        'IDENT     1.00000000E+00  5.00000000E+01  3.00000000E+00  0.00000000E+00',
        'DATE      1.00000000E+00  0.00000000E+00  4.00000000E+00  7.20000000E+01',
        'GCOORD    4.42046000E+05  3.05100006E+02  1.09150002E+02  4.98575012E+02',
        'GCOORD    4.42057000E+05  3.05100006E+02  1.10699997E+02  4.99049988E+02',
        'GELMNT1   1.69137000E+05  1.69137000E+05  2.60000000E+01  0.00000000E+00',
        '          3.10422000E+05  3.10410000E+05  3.10412000E+05  3.10522000E+05',
        '          3.10413000E+05  3.10523000E+05',
        'GELMNT1   1.69138000E+05  1.69138000E+05  2.80000000E+01  0.00000000E+00',
        '          3.10558000E+05  3.10562000E+05  3.10560000E+05  3.10561000E+05',
        '          2.86249000E+05  2.86252000E+05  2.86251000E+05  3.10559000E+05'
    ]
    file_path = os.path.join(tmpdir, 'test.fem')
    with open(file_path, 'w') as file:
        file.write('\n'.join(data_lines))
    return file_path




def test_translate(test_file):
    fem_obj=FEM()
    fem_obj.read_fem(test_file)
    fem_obj.translate_nodes(Vector3(100.0,100.0,100.0))
    assert fem_obj.gcoord[int(float(4.42046000E+05))].xcoord == float(4.05100006E+02)



test_translate(test_file)
