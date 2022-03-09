# nama file .py
# memanggil file math.py
'''

import mtk

hasil = mtk.plus(10 ,8) # memanggil fungsi dari file mtk.py
print(hasil)

hasil = mtk.minus(10 ,8) # memanggil fungsi dari file mtk.py
print(hasil)
'''

# memanggil file math.py beserta fungsi nya
from package.mtk import plus, minus
result = plus(40, 6)
print(result)

result = minus(40, 6)
print(result)