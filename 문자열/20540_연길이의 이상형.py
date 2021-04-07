mbti1 = ['E', 'S', 'T', 'J']
mbti2 = ['I', 'N', 'F', 'P']
w_mbti = ''
m_mbti = input()
for i in m_mbti:
    if i in mbti1:
        w_mbti += mbti2[mbti1.index(i)]
    else:
        w_mbti += mbti1[mbti2.index(i)]
print(w_mbti)
