test_dict = [{"kz_index": 0.9, "reason": [0.5, 0.5, 0.5]}, {"kz_index": 0.7, "reason": [0.5, 0.5, 0.5]}, {"kz_index": 0.5, "reason": [0.5, 0.5, 0.5]}]
for item in test_dict:
    item['reason'].append(0.09)
    item['kz_index'] += 2
print(test_dict)