from pydantic import BaseModel
from enum import StrEnum

class TipoTelefone(StrEnum):
    MOVEL     = "movel"
    FIXO      = "fixo"
    COMERCIAL = "comercial"

class CategoriaContato(StrEnum):
    FAMILIAR  = "familiar"
    PESSOAL   = "pessoal"
    COMERCIAL = "comercial"

class Telefone(BaseModel):
    numero: int
    tipo  : TipoTelefone
