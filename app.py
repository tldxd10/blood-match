import random
import streamlit as st

blood_types = {
    "AA": "A형",
    "AO": "A형",
    "BB": "B형",
    "BO": "B형",
    "AB": "AB형",
    "OO": "O형",
}


def make_child(mom, dad):
    mom_genes = list(mom)
    dad_genes = list(dad)
    child_types = []

    for m in mom_genes:
        for d in dad_genes:
            child = "".join(sorted(m + d))
            if child not in child_types:
                child_types.append(child)

    return child_types


st.title("🧬 혈액형 유전자 조합 분석기")
st.write("부모와 자식의 혈액형 유전자형을 직접 입력하세요.")
st.write("입력 예시: AA, AO, AB, BB, BO, OO")

mom = st.text_input("엄마의 혈액형 유전자형")
dad = st.text_input("아빠의 혈액형 유전자형")
child = st.text_input("자식의 혈액형 유전자형")

if st.button("분석하기"):
    mom = mom.upper().strip()
    dad = dad.upper().strip()
    child = child.upper().strip()

    if (
        mom not in blood_types
        or dad not in blood_types
        or child not in blood_types
    ):
        st.error(
            "잘못된 입력입니다. AA, AO, AB, BB, BO, OO 중에서 입력하세요."
        )
    else:
        possible_children = make_child(mom, dad)
        child_blood = blood_types[child]

        st.subheader("분석 결과")
        st.write("엄마의 유전자형:", mom)
        st.write("아빠의 유전자형:", dad)
        st.write("자식의 유전자형:", child)
        st.write("자식의 혈액형:", child_blood)

        st.write("### 부모에게서 나올 수 있는 자식의 유전자형")
        for gene in possible_children:
            st.write(gene, "-", blood_types[gene])

        # 엄마 유전자 1개 + 아빠 유전자 1개를 각각 랜덤 추출
        random_result = "".join(sorted([random.choice(mom), random.choice(dad)]))
        st.write(
            f"무작위 유전자 조합: {random_result} ({blood_types[random_result]})"
        )

        if child in possible_children:
            st.success(
                "혈액형 조합이 가능합니다. 정확한 친자 확인을 위해 DNA 검사가 필요합니다."
            )
        else:
            st.error(
                "혈액형 조합이 일치하지 않습니다. 친자가 아닐 가능성이 높지만, 혈액형만으로 확정할 수는 없습니다."
            )
