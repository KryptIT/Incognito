import ctypes

dll = ctypes.CDLL(r"bin\\Luaume.dll")
StartClient = dll.StartClient


def AttachGame():
    dll.StartClient()