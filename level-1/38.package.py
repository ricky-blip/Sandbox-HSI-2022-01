# package = folder dan harus ada file __init__.py
'''
cara memanggil dari package
from namaPackage.namaModule lalu import function
'''

from package.mtk import plus, minus
result = plus(100, 6)
print(result)

result = minus(50, 6)
print(result)