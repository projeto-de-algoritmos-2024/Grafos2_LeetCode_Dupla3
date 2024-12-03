class Solution:
    def criticalConnections(self, n, connections):
        grafo = [[] for _ in range(n)]
        for conexao in connections:
            grafo[conexao[0]].append(conexao[1])
            grafo[conexao[1]].append(conexao[0])

        nivel = [-1] * n  
        menor_nivel = [-1] * n 
        resultado = []
        tempo = 0

        def buscar_pontes(atual, pai):
            nonlocal tempo
            nivel[atual] = menor_nivel[atual] = tempo
            tempo += 1

            for vizinho in grafo[atual]:
                if vizinho == pai:
                    continue 
                if nivel[vizinho] == -1:  
                    buscar_pontes(vizinho, atual)
                    menor_nivel[atual] = min(menor_nivel[atual], menor_nivel[vizinho])
                    if menor_nivel[vizinho] > nivel[atual]:
                        resultado.append([atual, vizinho])
                else:
                    menor_nivel[atual] = min(menor_nivel[atual], nivel[vizinho])

        for i in range(n):
            if nivel[i] == -1:
                buscar_pontes(i, -1)

        return resultado
