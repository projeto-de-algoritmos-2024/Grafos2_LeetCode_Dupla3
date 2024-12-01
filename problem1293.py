import heapq

class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])

        # definindo a min-heap, onde armazenamos: 
        # qtd de passos dados, linha, coluna e qtd de obstáculos removidos
        heap = [(0, 0, 0, 0)]

        # conjunto que armazena os locais visitados, armazenando:
        # linha, coluna e qtd de obstáculos removidos
        visited = set()
        visited.add((0, 0, 0))

        # direita, baixo, esquerda e para cima
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            steps, row, collumn, removed_obstacles = heapq.heappop(heap)

            # verificando se já chegamos no destino
            if row == m - 1 and collumn == n - 1:
                return steps
            
            for dx, dy in directions:
                # calculando a próxima posição
                nx, ny = row + dx, collumn + dy

                # verificando se estamos dentro da matriz
                if 0 <= nx < m and 0 <= ny < n:
                    new_removed_obstacle = removed_obstacles + grid[nx][ny]

                    # se não foi visitado e a qtd de obstáculos removidos não tiver ultrapassado o limite
                    if new_removed_obstacle <= k and (nx, ny, new_removed_obstacle) not in visited:
                        visited.add((nx, ny, new_removed_obstacle))
                        heapq.heappush(heap, (steps+1, nx, ny, new_removed_obstacle))
        return -1
