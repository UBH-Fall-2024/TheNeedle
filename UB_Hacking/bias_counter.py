def bias_stats(text, weight_dict):
    score_list = []
    for key, weight in weight_dict.items():
        num_occurences = text.count(key)
        score_list += [weight for i in range(num_occurences)]
    return [sum(score_list), len(score_list), sum(score_list)/len(score_list)]
