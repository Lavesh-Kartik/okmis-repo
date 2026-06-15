# Okims_JSON_Builder

ComfyUI용 시각적 JSON 프롬프트 빌더 노드입니다.

## 설치

폴더 전체를 아래 위치에 넣고 ComfyUI를 재시작하세요.

```text
ComfyUI/custom_nodes/ComfyUI-Okims_JSON_Builder/
```

## 노드 위치

```text
Okims/JSON > Okims_JSON_Builder
```

노드에는 아래 버튼만 표시됩니다.

```text
Open Builder
Copy JSON
```

Open Builder를 누르면 전체 편집기가 열립니다. 편집기 상단의 **Confirm & Send JSON Prompt**를 누르면 생성된 JSON 프롬프트가 ComfyUI 노드로 전송되고, 노드는 해당 값을 STRING으로 출력합니다.

이 노드는 모델을 직접 실행하지 않고 JSON 프롬프트 생성만 담당합니다.
