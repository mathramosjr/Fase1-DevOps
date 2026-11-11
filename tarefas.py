class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo):
        if not titulo or not titulo.strip():
            raise ValueError("O titulo da tarefa não pode ser vazio")
        tarefa = {
            "id": len(self.tarefas) + 1,
            "titulo": titulo.strip(),
            "concluida": False,
        }
        self.tarefas.append(tarefa)
        return tarefa

    def listar(self):
        return list(self.tarefas)

    def concluir(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                return tarefa
        raise KeyError(f"Terefa {id_tarefa} não encontrada")