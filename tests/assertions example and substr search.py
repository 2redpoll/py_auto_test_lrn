#def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    # assert (actual_result == expected_result), f"expected {expected_result}, got {actual_result}"
def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert (substring in full_string), f'expected \'{substring}\' to be substring of \'{full_string}\''

s = 'My name is Vlad'
if 'name' in s:
    print('Substring found')

index = s.find('name')
if index != -1:
    print(f'Substring found at index {index}')



