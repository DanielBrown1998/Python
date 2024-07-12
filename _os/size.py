import math 

def formata_tamanho(tam_bytes: int, base: int  = 1024, formatacao: int = 2) -> str:
    if tam_bytes <= 0:
        return "0B"
    abbr_tam = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']        
    indice_abbr_tam = int(math.log(tam_bytes, base))
    tam = round(tam_bytes / pow(base, indice_abbr_tam), formatacao)
    return f"{tam} {abbr_tam[indice_abbr_tam]}"