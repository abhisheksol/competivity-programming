def australian_voting(candidates, ballots):
    num_candidates = len(candidates)
    num_ballots = len(ballots)
    
    while True:
        votes = [0] * num_candidates
        for ballot in ballots:
            if len(ballot) > 0:
                votes[ballot[0]] += 1
        
        for i in range(num_candidates):
            if votes[i] > num_ballots // 2:
                return candidates[i]
        
        min_votes = min(votes)
        min_candidates = [i for i in range(num_candidates) if votes[i] == min_votes]
        
        if len(min_candidates) == 1:
            eliminated_candidate = min_candidates[0]
        else:
            eliminated_candidate = min_candidates[0]
        
        for i in range(num_ballots):
            if eliminated_candidate in ballots[i]:
                ballots[i].remove(eliminated_candidate)
        
        if len(set(ballot[0] for ballot in ballots)) == 1:
            return candidates[ballots[0][0]]

candidates = ["Candidate A", "Candidate B", "Candidate C"]
ballots = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
]

winner = australian_voting(candidates, ballots)
print("Winner:", winner)
