import random
from typing import NamedTuple
from persistence.session import create_connection

class AnuncioMain(NamedTuple):
    id: int
    titulo: str
    descricao: str

class AnuncioDetalhes(NamedTuple):
    titulo: str
    descricao: str
    id_contrato: int
    
def list_all() -> list[AnuncioMain]:
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("select id, titulo, descricao from anuncio")
        return list(map(lambda row: AnuncioMain(row.id, row.titulo, row.descricao), cursor))
    
"""def read(id:int):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("select * from anuncio where id=?", id)
        row = cursor.fetchone()
        
        return row.id, AnuncioDetalhes(
            row.titulo,
            row.descricao,
            row.id_contrato
        )
"""
        
def create(anuncio: AnuncioDetalhes):
    id_int = random.randint(1000, 9999)
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       insert into anuncio(id,titulo, descricao, id_contrato)
                       values(?,?,?,?)
                       """,
                        id_int,
                        anuncio.titulo,
                        anuncio.descricao,
                        anuncio.id_contrato
                    )
        conn.commit()
        
def update(id:int, anuncio: AnuncioDetalhes):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       update anuncio
                       set titulo=?, descricao=?, id_contrato=?,
                       where id=?
                       """,
                        anuncio.titulo,
                        anuncio.descricao,
                        anuncio.id_contrato,
                        id
                    )
        conn.commit()
        
def delete(id:int):
    with create_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("delete from anuncio where id=?", id)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
                       
                       