from collections import defaultdict

class Solution:
    # Aqui ta rolando o algoritmo que roda o DFS no grafo original e reverso
    def calculateSCC(self, n, edges):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)

        def dfs(v, graph, visited, stack):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor, graph, visited, stack)
            stack.append(v)

        def dfs_transposed(v, reverse_graph, visited, scc):
            visited[v] = True
            scc.append(v)
            for neighbor in reverse_graph[v]:
                if not visited[neighbor]:
                    dfs_transposed(neighbor, reverse_graph, visited, scc)

        stack = []
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                dfs(i, graph, visited, stack)

        visited = [False] * n
        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc = []
                dfs_transposed(node, reverse_graph, visited, scc)
                sccs.append(scc)

        # Ta retornando um array com todos os SCCs que tem no grafo
        return sccs


    # Função principal
    def findSmallestSetOfVertices(self, n, edges):
        sccs = self.calculateSCC(n, edges)

        # Aqui eu to criando um dicionário que separa cada item do array de
        # SCCs de acordo com um índice
        scc_index = {}
        for idx, scc in enumerate(sccs):
            for node in scc:
                scc_index[node] = idx

        # Aqui, to verificando se existe alguma aresta entre um nó de um SCC 
        # para um nó de outro SCC
        scc_indegree = defaultdict(int)
        for u, v in edges:
            u_scc = scc_index[u]
            v_scc = scc_index[v]
            if u_scc != v_scc:
                scc_indegree[v_scc] += 1

        result = [scc[0] for idx, scc in enumerate(sccs) if scc_indegree[idx] == 0]
        
        return result
