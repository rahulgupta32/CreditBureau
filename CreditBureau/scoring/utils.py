# def calculate_credit_score(responses):
#     score = 0
#     score_mapping = {'A': 10, 'B': 7, 'C': 4, 'D': 1}
#     for response in responses:
#         score += score_mapping.get(response.answer, 0)
#     return score


def calculate_credit_score(responses):
    score = 0
    for response in responses:
        question = response.question
        if response.answer == 'A':
            score += question.score_a
            
        elif response.answer == 'B':
            score += question.score_b
        
        elif response.answer == 'C':
            score += question.score_c
            
        elif response.answer == 'D':
            score += question.score_d
            
    return score            