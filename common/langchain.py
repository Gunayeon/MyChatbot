import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import time

@st.cache_resource  # 객체를 caching 처리 
def get_client():
    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )
    return llm

def response_from_llm(prompt, message_history=[], model_id: str = "gpt-4o-mini"):
    # 프롬프트 생성
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "이 시스템은 여행 전문가입니다."),
        ("user", "{user_input}"),
    ])
    
    
    # 체인 생성 = 프롬프트 + 모델
    chain = chat_prompt | get_client()

    # 응답 생성
    response = chain.stream({"user_input": prompt})

    # 응답을 스트리밍 방식으로 출력
    for chunk in response:
        yield chunk
        time.sleep(0.05)