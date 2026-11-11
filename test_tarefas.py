import pytest
from tarefas import ListaDeTarefas


def test_adicionar_tarefa():
    lista = ListaDeTarefas()
    tarefa = lista.adicionar("Estudar DevOps")
    assert tarefa["titulo"] == "Estudar DevOps"
    assert tarefa["concluida"] is False
    assert len(lista.listar()) == 1


def test_titulo_vazio_gera_erro():
    lista = ListaDeTarefas()
    with pytest.raises(ValueError):
        lista.adicionar("   ")


def test_concluir_tarefa():
    lista = ListaDeTarefas()
    tarefa = lista.adicionar("Fazer o pipeline")
    resultado = lista.concluir(tarefa["id"])
    assert resultado["concluida"] is True


def test_concluir_tarefa_inexistente():
    lista = ListaDeTarefas()
    with pytest.raises(KeyError):
        lista.concluir(99)