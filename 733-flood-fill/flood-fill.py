class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        dr = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        n = len(image)
        m = len(image[0])

        start = image[sr][sc]
        if start == color:
            return image

        def fun(sr, sc, image):
            q = deque([(sr, sc)])
            image[sr][sc] = color

            while q:
                x, y = q.popleft()
                for k, l in dr:
                    nx = x + k
                    ny = y + l
                    if nx >= n or ny >= m or nx < 0 or ny < 0:
                        continue
                    if image[nx][ny] != start:
                        continue
                    image[nx][ny] = color
                    q.append((nx, ny))

        fun(sr, sc, image)
        return image
