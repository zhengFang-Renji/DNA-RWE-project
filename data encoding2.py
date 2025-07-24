def text_to_dna(text):
    # 二进制到碱基的映射规则
    mapping = {'00': 'A', '01': 'T', '10': 'C', '11': 'G'}
    
    # 将文本转换为二进制字符串
    binary_str = ''.join(format(ord(char), '08b') for char in text)
    
    # 确保二进制字符串长度是2的倍数
    if len(binary_str) % 2 != 0:
        binary_str += '0'  # 补零
    
    # 将二进制字符串分割为2位一组并转换为DNA序列
    dna_sequence = []
    for i in range(0, len(binary_str), 2):
        pair = binary_str[i:i+2]
        dna_sequence.append(mapping[pair])
    
    return ''.join(dna_sequence)

# 用户输入
user_input = input("请输入要转换的文本: ")
dna_output = text_to_dna(user_input)
print("转换后的DNA序列:", dna_output)