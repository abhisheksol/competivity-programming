class Contestant:
    def __init__(self, _id):
        self.id = _id
        self.time = 0
        self.solved = 0
        self.submissions = [0] * 10
        self.isSolved = [False] * 10

    def __lt__(self, other):
        if self.solved == other.solved:
            if self.time == other.time:
                return self.id < other.id
            return self.time < other.time
        return self.solved > other.solved

def main():
    test_cases = 1  # Sample data, so just 1 test case
    for _ in range(test_cases):
        data = [Contestant(i) for i in range(101)]
        participation = [False] * 101  # Assuming maximum contestant id is 100
        submissions = [
            "1 2 10 C",
            "2 3 20 C",
            "1 2 30 C",
            "3 1 15 C",
            "2 3 25 C",
            "1 2 35 C",
            "1 3 20 I",
            "2 3 30 I"
        ]
        for submission in submissions:
            id, problem, time, status = map(str, submission.split())
            id = int(id)
            problem = int(problem)
            time = int(time)
            if not data[id].isSolved[problem]:
                if status == 'C':
                    data[id].solved += 1
                    data[id].isSolved[problem] = True
                    data[id].time += time + data[id].submissions[problem] * 20
                elif status == 'I':
                    data[id].submissions[problem] += 1
            participation[id] = True

        board = [contestant for i, contestant in enumerate(data) if participation[i]]
        board.sort()
        for contestant in board:
            print(contestant.id, contestant.solved, contestant.time)
        if test_cases:
            print()

if __name__ == "__main__":
    main()
