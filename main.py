# import pytest
# from testing_layer.api_tests.add_area_test import AreaTests
# from infra_layer.infra_ui.wrapper import browserWrapper
# from testing_layer.ui_tests.check_area_test import areaTests
#
# @pytest.fixture
# def infra_layer():
#     return browserWrapper()
#
# def test_run_grid_serial(infra_layer):
#     print(infra_layer.cab_list)
#     for cabs in infra_layer.cab_list:
#         # Instantiate the areaTests class
#         search_test_instance = areaTests()
#         # Pass any necessary parameters to the test method
#         search_test_instance.verify_successful_area_add(cabs,infra_layer)
#         # You may add additional test methods from areaTests if needed
#
# if __name__ == "__main__":
#     pytest.main([__file__])
def count_overlapping(a, b):
    count = 0
    for i in range(len(b) - len(a) + 1):
        for j in range(len(a)):
            if b[i+j] != a[j]:
                break
        else:
            count += 1
    return count

def add_appearances_in_matrix_columns(words_list, matrix):
    num_cols = len(matrix[0])

    for col in range(num_cols):
        column_str = ''.join([row[col] for row in matrix])

        for i, word_count in enumerate(words_list):
            word, count = word_count
            appearances = count_overlapping(word, column_str)
            words_list[i][1] += appearances

matrix = [["c", "a", "t", "o", "e", "c", "b", "t", "f"],
          ["c", "d", "o", "g", "e", "c", "o", "t", "f"],
          ["c", "b", "e", "g", "e", "c", "b", "o", "f"],
          ["c", "o", "i", "g", "e", "c", "o", "e", "f"],
          ["c", "b", "i", "g", "e", "c", "b", "t", "f"]]

words_list = [["cat", 0], ["toe", 0], ["bob", 0]]
add_appearances_in_matrix_columns(words_list, matrix)
print(words_list)

