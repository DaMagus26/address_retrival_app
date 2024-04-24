﻿# SDK Pullenti Address, version 4.23, march 2024. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Streams import Stream

class PullentiNerCoreInternalResourceHelper:
    # Это для поддержки получения встроенных ресурсов
    
    @staticmethod
    def get_bytes(name : str) -> bytearray:
        
        names = Utils.getResourcesNames('pullenti.ner.core.properties', '.csv;.png')
        for n in names: 
            if (Utils.endsWithString(n, name, True)): 
                if (len(name) < len(n)): 
                    if (n[len(n) - len(name) - 1] != '.'): 
                        continue
                try: 
                    inf = Utils.getResourceInfo('pullenti.ner.core.properties', n)
                    if (inf is None): 
                        continue
                    with Utils.getResourceStream('pullenti.ner.core.properties', n) as stream: 
                        buf = Utils.newArrayOfBytes(stream.length, 0)
                        stream.read(buf, 0, len(buf))
                        return buf
                except Exception as ex: 
                    pass
        return None
    
    @staticmethod
    def get_string(name : str) -> str:
        arr = PullentiNerCoreInternalResourceHelper.get_bytes(name)
        if (arr is None): 
            return None
        if ((len(arr) > 3 and arr[0] == (0xEF) and arr[1] == (0xBB)) and arr[2] == (0xBF)): 
            return arr[3:3+len(arr) - 3].decode("UTF-8", 'ignore')
        else: 
            return arr.decode("UTF-8", 'ignore')