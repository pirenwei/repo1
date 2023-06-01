import streamlit as st
//import openai


# 设置OpenAI API密钥
openai.api_key = 'org-8wkSnxtGzsh06oUcf8H7zKPP'


def generate_cover_letter(user_profile, job_description, summary_length, tone):
    # 根据所选的语气选择相应的模型ID
    if tone == '正式':
        model_id = 'gpt-3.5-turbo'
    elif tone == '友好':
        model_id = 'text-davinci-003'
    else:
        model_id = 'text-davinci-003'  # 默认选择友好的语气

    # 生成求职信的请求
    prompt = f"个人资料：\n{user_profile}\n\n工作描述：\n{job_description}\n\n摘要字数：{summary_length}\n\n语气：{tone}\n\n生成求职信："
    response = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        max_tokens=summary_length,
        temperature=0.5,
        n = 1
    )

    return response.choices[0].text.strip()


def save_cover_letter(cover_letter_text):
    # 将生成的求职信保存到文件
    with open("cover_letter.txt", "w") as file:
        file.write(cover_letter_text)


# Streamlit应用程序的主要部分
def main():
    st.title("求职信生成器")

    # 用户输入
    user_profile = st.text_area("个人资料")
    job_description = st.text_area("工作描述")

    # 设置选项
    summary_length = st.slider("摘要字数", min_value=50, max_value=500, step=50, value=200)
    tone = st.selectbox("语气", ['友好', '正式'])

    # 生成求职信
    if st.button("生成求职信"):
        cover_letter = generate_cover_letter(user_profile, job_description, summary_length, tone)
        st.success("求职信已生成！")
        st.text_area("生成的求职信", value=cover_letter, height=400)
        if st.button("保存求职信"):
            save_cover_letter(cover_letter)
            st.success("求职信已保存！")


if __name__ == "__main__":
    main()

