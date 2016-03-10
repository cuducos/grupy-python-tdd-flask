def fatorial(numero):
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)
