def new_for_me(scanner):
    actions = [abs, float, str]
    results = []
    for action in actions:
        results.append(action(scanner))
    return results

if __name__ == "__main__":
    scanner = int(input("type a num: "))
    result = new_for_me(scanner)
    print(result)
