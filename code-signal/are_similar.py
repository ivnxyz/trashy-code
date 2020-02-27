def areSimilar(a, b):
  # Buscar elementos fuera de lugar
  indexes_out_of_place = [i for i, e in enumerate(a) if e!=b[i]]
  elements_out_of_place = len(indexes_out_of_place)

  if elements_out_of_place > 2:
    return False
  elif elements_out_of_place == 0:
    return True
  elif elements_out_of_place == 2:
    return b[indexes_out_of_place[1]] == a[indexes_out_of_place[0]]
  else:
    return b[indexes_out_of_place[0]] == a[indexes_out_of_place[0]]

print(areSimilar([1], [0]))
print(areSimilar([1, 2, 3], [2, 1, 3]))
print(areSimilar([1, 2, 2], [2, 1, 1]))
print(areSimilar([1, 1, 4], [1, 2, 3]))

