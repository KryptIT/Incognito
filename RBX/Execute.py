import ctypes
from Encoder.EncoderUTF8 import EncodingUTF8

dll = ctypes.CDLL(r"bin\\Luaume.dll")

ExecuteSC = dll.ExecuteSC
ExecuteSC.argtypes = [ctypes.POINTER(ctypes.c_char)]
ExecuteSC.restype = None

def ExecuteSync(script):
    script_bytes = EncodingUTF8(script)
    
    script_array = (ctypes.c_char * len(script_bytes))(*script_bytes)
    
    ExecuteSC(script_array)