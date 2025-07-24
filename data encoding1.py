def binary_to_ternary(binary_str):
    """将二进制字符串转换为三进制字符串，无位数限制"""
    decimal = int(binary_str, 2)
    if decimal == 0:
        return '0'  # 处理全0情况
    ternary = []
    while decimal > 0:
        decimal, rem = divmod(decimal, 3)
        ternary.append(str(rem))
    return ''.join(reversed(ternary))  # 直接返回反转后的三进制字符串

# 编码规则表保持不变
ENCODING_RULES = {
    'A': {'0':'C', '1':'G', '2':'T'},
    'C': {'0':'G', '1':'T', '2':'A'},
    'G': {'0':'T', '1':'A', '2':'C'},
    'T': {'0':'A', '1':'C', '2':'G'}
}

def encode_dna(ternary_str):
    """将三进制字符串转换为DNA序列"""
    sequence = ['A']  # 第一个碱基固定为A
    current = 'A'
    for trit in ternary_str:
        next_base = ENCODING_RULES[current][trit]
        sequence.append(next_base)
        current = next_base
    return ''.join(sequence)

# 测试数据
binary_blocks = [
    "111111111111110111011111110000011111110000011111110000011111111000011111111000011001111000011001111000001101111000000101111000000001111000000011",
]

# 转换并打印结果
for binary in binary_blocks:
    ternary = binary_to_ternary(binary)
    dna = encode_dna(ternary)
    print(dna)

