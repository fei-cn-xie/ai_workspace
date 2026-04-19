
# 两个向量点积计算
def dot_product(vec1, vec2):
    """计算两个向量的点积"""
    if(len(vec1) != len(vec2)):
        raise ValueError("Vectors must be of the same length")
    return sum(a * b for a, b in zip(vec1, vec2))

# 向量模长计算
def magnitude_product(vec):
    """计算向量的模长"""
    return sum(a ** 2 for a in vec) ** 0.5
    

# 余弦相似度计算
def cosine_similarity(vec1, vec2):
    """计算两个向量的余弦相似度"""
    dot_prod = dot_product(vec1, vec2)
    mag_prod = magnitude_product(vec1) * magnitude_product(vec2)
    if mag_prod == 0:
        return 0.0  # 避免除以零
    return dot_prod / mag_prod

if __name__ == "__main__":
    vec1 = [1, 2, 3]
    vec2 = [4, 8, 12]
    similarity = cosine_similarity(vec1, vec2)
    print(f"Cosine Similarity: {similarity}")