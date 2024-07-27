class Solution:
    def findTheCity_using_hashtable(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int: # 37 / 54 test cases passed.
        # use a hashtable to store the distance between each pair of cities

        dist = {
            i: {
                j: 0 for j in range(n)
            } for i in range(n)
        }

        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]

        smallest_index = -1
        smallest_count = float('inf')

        for start in range(n):
            paths = [k for k, v in dist[start].items() if v != 0 and v <= distanceThreshold]
            print(f"Starting at city {start} for paths {paths}")
            path_count = 0
            count_city = []
            for path in paths:

                used_city = [start]
                path_dist = 0
                prev = start
                while True:
                    used_city.append(path)

                    if path not in count_city:
                        count_city.append(path)
                        path_count += 1

                    path_dist += dist[prev][path]

                    available_paths = [
                        (k, v) for k, v in dist[path].items() if v != 0 and v <= distanceThreshold and k not in used_city
                    ]

                    if not available_paths:
                        break

                    min_path = min(available_paths, key=lambda x: x[1])[0]

                    if path_dist + dist[path][min_path] > distanceThreshold:
                        break

                    prev = path
                    path = min_path
                    print(f"Used city {used_city}")
                    continue
            print(f"Path count for city {start} is {path_count}")
            if path_count <= smallest_count:
                smallest_count = path_count
                smallest_index = start
            continue
        return smallest_index

    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # This solution is guided by ChatGPT
        pass


if __name__ == "__main__":
    sol = Solution()


    n1, edges1, distanceThreshold1, output1 = 4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4, 3
    print(sol.findTheCity_using_hashtable(n1, edges1, distanceThreshold1))

    n2, edges2, distanceThreshold2, output2 = 5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2, 0
    print(sol.findTheCity_using_hashtable(n2, edges2, distanceThreshold2))
