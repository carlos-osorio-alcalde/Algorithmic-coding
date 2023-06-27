"""https://leetcode.com/problems/find-if-path-exists-in-graph/"""

from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        neighbors_for_each_node = {}
        for edge in edges:
            for i in range(2):
                if edge[i] in neighbors_for_each_node:
                    neighbors_for_each_node[edge[i]].append(edge[1 - i])
                else:
                    neighbors_for_each_node[edge[i]] = [edge[1 - i]]

        visited_nodes = set()

        def search(source):
            visited_nodes.add(source)
            if source == destination:
                return True

            neighbors = neighbors_for_each_node[source]
            for node in neighbors:
                if node not in visited_nodes:
                    if search(node):
                        return True

            return False

        return search(source)
