
# AI Network Project

## 소개
이 프로젝트는 VirtualBox와 Xshell을 활용하여 Python 환경을 구축하고, RAG 기법과 LLM 모델을 이용한 AI 시스템을 개발하는 데 중점을 둡니다.

## 주요 기능
- VirtualBox와 Xshell을 이용한 네트워크 설정.
- Python 환경 구축 및 JupyterLab 실행.
- RAG 기법을 활용한 LLM 응답 최적화.
- Vectorstore를 사용한 문서 검색 및 응답.

## 설치 방법
1. **필수 조건**:
   - Python 3.8 이상
   - Anaconda
   - Xshell 및 VirtualBox
2. **환경 설정**:
   ```bash
   sudo apt install openssh-server
   wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh
   bash Anaconda3-2024.06-1-Linux-x86_64.sh
   ```
3. **Python 의존성 설치**:
   ```bash
   pip install -r requirements.txt
   ```

## 실행 방법
1. Anaconda 환경 활성화:
   ```bash
   source anaconda3/bin/activate
   ```
2. JupyterLab 실행:
   ```bash
   jupyter lab --ip 0.0.0.0 --port 8889
   ```
3. RAG 모델 테스트:
   ```bash
   python src/rag_inference.py
   ```

## 결과 예시
![샘플 이미지](assets/screenshots/example.png)
