def suite_likelihood(suite, data):
    total = 0
    for hypo, prob in suite.iter_items():
        like = suite.likelihood(data, hypo)
        total += prob * like
    return total
