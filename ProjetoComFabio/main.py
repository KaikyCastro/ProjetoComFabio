from Usuario import Usuario
from hashlib import sha256


usuario = Usuario("Fabio", 20, "134.301.994-09", "01/01/2000", "1234567", "Centro", "Sao Paulo", "SP", "11999999999")

result = usuario.validarCPF(usuario.getCPF())

print(result)
print(usuario.__str__())
