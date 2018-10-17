''' Testing arrays. '''
def main():
    ''' Main function '''
    num_scores = int(input())
    scores = list(input().split())
    scores.sort(key=int)
    score_index = num_scores - 1
    high_score = scores[score_index]
    while scores[score_index] == high_score:
        scores.pop(score_index)
        score_index -= 1
    print(scores[score_index])

if __name__ == "__main__":
    main()
