class Solution:
    def networkDelayTime(self, tempos, n, k):
        grafo = [[] for _ in range(n + 1)]
        for origem, destino, peso in tempos:
            grafo[origem].append((destino, peso))
        
        menor_tempo = [float('inf')] * (n + 1)
        menor_tempo[k] = 0  
        
        fila = [(k, 0)]  
        
        while fila:
            fila.sort(key=lambda x: x[1])  
            no_atual, tempo_atual = fila.pop(0)  
            
            for vizinho, peso in grafo[no_atual]:
                novo_tempo = tempo_atual + peso
                if novo_tempo < menor_tempo[vizinho]:
                    menor_tempo[vizinho] = novo_tempo
                    fila.append((vizinho, novo_tempo))
        
        maior_tempo = max(menor_tempo[1:]) 
        return maior_tempo if maior_tempo < float('inf') else -1
