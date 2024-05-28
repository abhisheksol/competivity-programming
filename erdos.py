from collections import defaultdict

def calculate_erdos_numbers(papers, authors):
    # Create a graph of authors
    graph = defaultdict(list)
    for paper in papers:
        authors_list = paper.split(':')[0].split(', ')
        for author1 in authors_list:
            for author2 in authors_list:
                if author1 != author2:
                    graph[author1].append(author2)

    # Initialize Erdos numbers
    erdos_numbers = {}
    for author in authors:
        if author == 'Erdos, P.':
            erdos_numbers[author] = 0
        else:
            erdos_numbers[author] = float('inf')

    # BFS to calculate Erdos numbers
    queue = ['Erdos, P.']
    while queue:
        current_author = queue.pop(0)
        for neighbor in graph[current_author]:
            if erdos_numbers[neighbor] == float('inf'):
                erdos_numbers[neighbor] = erdos_numbers[current_author] + 1
                queue.append(neighbor)

    return erdos_numbers

def main():
    papers = [
        "Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factor matrices",
        "Erdos, P., Reisig, W.: Stuttering in petri nets",
        "Smith, M.N., Chen, X.: First order derivatives in structured programming",
        "Jablonski, T., Hsueh, Z.: Self-stabilizing data structures"
    ]
    authors = ["Smith, M.N.", "Hsueh, Z.", "Chen, X."]

    print("Scenario 1")
    erdos_numbers = calculate_erdos_numbers(papers, authors)
    for author in authors:
        if erdos_numbers[author] == float('inf'):
            print(f"{author} infinity")
        else:
            print(f"{author} {erdos_numbers[author]}")

if __name__ == "__main__":
    main()
