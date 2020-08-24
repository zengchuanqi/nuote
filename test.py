import copy


# stage1和stage2合在一起了
def translate_letter(digits: str):
    # 如果输入的是列表形式转化成真正的列表
    if digits[0] == '[' and digits[-1] == ']':
        digits = digits[1:len(digits) - 1].split(',')
        print(digits)
    dic = {'0': ' ', '1': ' ', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = ['']
    for i in digits:
        tem = []
        for j in res:
            for k in dic[i]:
                # 去除空格
                tem.append((j + k).strip())
            res = copy.deepcopy(tem)
    return res


if __name__ == '__main__':
    print(translate_letter(input('请输入一个列表或者数字(如:[2,3],0-99):')))
