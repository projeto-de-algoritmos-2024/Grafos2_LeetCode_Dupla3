from collections import defaultdict

class Solution:
    def calculaSCC(self, n, edges):
        graph = defaultdict(list)
        transposed_graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            transposed_graph[v].append(u)
        
        def dfs(v, graph, visited, stack):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor, graph, visited, stack)
            stack.append(v)
        
        def dfs_transposed(v, transposed_graph, visited, scc):
            visited[v] = True
            scc.append(v)
            for neighbor in transposed_graph[v]:
                if not visited[neighbor]:
                    dfs_transposed(neighbor, transposed_graph, visited, scc)
        
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
                dfs_transposed(node, transposed_graph, visited, scc)
                sccs.append(scc)
        
        return sccs

    def findSmallestSetOfVertices(self, n, edges):
        sccs = self.calculaSCC(n, edges)
        
        scc_indegree = defaultdict(int)
        scc_index = {}
        
        for idx, scc in enumerate(sccs):
            for node in scc:
                scc_index[node] = idx
        
        for u, v in edges:
            u_scc = scc_index[u]
            v_scc = scc_index[v]
            if u_scc != v_scc:
                scc_indegree[v_scc] += 1
        
        result = []
        for idx, scc in enumerate(sccs):
            if scc_indegree[idx] == 0:
                result.append(scc[0])
        
        return result
