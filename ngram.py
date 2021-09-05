# 2021712564 Kyung-hee Jung
# Due Date: 2021-09-12
# n_gram 구현하기

def n_gram(text, n):
    re = []
    s_text = text.split(' ') # Cut
    for i in range(0, len(s_text)-n+1, 1):
        a = ' '.join(s_text[i:i+n]) # Link
        re.append(a)
    return re


stext = "Colaboratory(또는 줄여서 'Colab')를 사용하면 브라우저에서 Python을 작성하고 실행할 수 있습니다."
ngrams = n_gram(stext, 4)
print(ngrams)

