---
date: 2026-03-05
categories:
  - AI
tags:
  - ai
  - llm
  - prompt-engineering
  - cursor
  - productivity
---

# Hiểu AI, dùng AI — 35 câu hỏi trọng tâm mà engineer nào cũng nên tự trả lời

AI không thiếu người dùng. Thiếu người hiểu.

Hầu hết engineer hiện tại dùng AI mỗi ngày —
Copilot gợi code, ChatGPT trả lời câu hỏi, Cursor viết cả file.
Nhưng nếu hỏi "LLM hoạt động thế nào?",
"hallucination xảy ra vì đâu?",
hay "khi nào nên tin AI, khi nào không?" —
phần lớn sẽ ngập ngừng.

Bài viết này không dạy bạn dùng tool.
Bài viết này giúp bạn **hiểu cái bạn đang dùng** —
để dùng tốt hơn, tránh bẫy,
và biến AI thành lợi thế thực sự của mình.

Đây là bài mở đầu và toàn diện nhất trong series AI —
5 layers, 35 câu hỏi,
từ bản chất đến thực hành,
từ prompt engineering đến AI-augmented growth.
Những bài sau sẽ đi sâu vào từng phần cụ thể.

<!-- more -->

!!! abstract "Bản đồ bài viết"

    | Layer | Chủ đề | Câu hỏi | Tóm tắt |
    | :---: | --- | :---: | --- |
    | **1** | Hiểu bản chất | Q1–6 | AI hoạt động thế nào, giới hạn ở đâu |
    | **2** | Đánh giá năng lực | Q7–14 | Giỏi gì, dở gì, làm sao thành lợi thế |
    | **3** | Prompt Engineering | Q15–23 | Nói chuyện với AI hiệu quả |
    | **4** | Tối ưu AI tools | Q24–31 | Cursor, workflow, thực hành hàng ngày |
    | **5** | AI-Augmented Growth | Q32–35 | Dùng AI để phát triển bản thân |

## Layer 1: Hiểu bản chất — AI thật sự là gì?

### 1. AI, ML, Deep Learning, GenAI — khác nhau thế nào?

Bốn thuật ngữ này thường bị dùng lẫn lộn,
nhưng thực ra là bốn lớp lồng nhau:

- **AI (Artificial Intelligence)** —
  ý tưởng lớn: máy có thể làm những việc đòi hỏi "trí thông minh".
  Rộng nhất, bao gồm cả rule-based system từ những năm 1960.
- **ML (Machine Learning)** —
  một nhánh của AI: thay vì lập trình rule cứng, cho máy học từ dữ liệu.
  Ví dụ: spam filter học từ hàng triệu email.
- **Deep Learning** —
  một nhánh của ML: dùng neural network nhiều tầng
  để học các pattern phức tạp.
  Ví dụ: nhận diện khuôn mặt, dịch ngôn ngữ.
- **GenAI (Generative AI)** —
  một ứng dụng của Deep Learning:
  tạo ra nội dung mới (text, ảnh, code, nhạc).
  ChatGPT, Midjourney, Copilot đều thuộc nhóm này.

<div style="display:flex;justify-content:center;padding:24px 0">
<div style="position:relative;width:320px;height:320px">
<div style="position:absolute;bottom:0;left:0;
  width:320px;height:320px;border-radius:50%;
  background:#e3f2fd;border:2px solid #1565c0">
</div>
<span style="position:absolute;top:15px;left:50%;
  transform:translateX(-50%);
  font-weight:700;color:#1565c0">
  AI
</span>
<div style="position:absolute;bottom:0;left:40px;
  width:240px;height:240px;border-radius:50%;
  background:#e8f5e9;border:2px solid #2e7d32">
</div>
<span style="position:absolute;top:92px;left:50%;
  transform:translateX(-50%);
  font-weight:700;color:#2e7d32">
  ML
</span>
<div style="position:absolute;bottom:0;left:75px;
  width:170px;height:170px;border-radius:50%;
  background:#fff3e0;border:2px solid #e65100">
</div>
<span style="position:absolute;top:160px;left:50%;
  transform:translateX(-50%);
  font-weight:700;color:#e65100;
  white-space:nowrap;font-size:.85em">
  Deep Learning
</span>
<div style="position:absolute;bottom:0;left:112px;
  width:96px;height:96px;border-radius:50%;
  background:#fce4ec;border:2px solid #c62828">
</div>
<span style="position:absolute;top:234px;left:50%;
  transform:translateX(-50%);
  font-weight:700;color:#c62828">
  GenAI
</span>
</div>
</div>

Khi ai đó nói "AI" năm 2026,
họ thường đang nói GenAI.
Nhưng AI rộng hơn GenAI rất nhiều.

### 2. LLM hoạt động thế nào (ở mức high-level)?

LLM (Large Language Model) về bản chất là một cỗ máy dự đoán:
cho trước một chuỗi từ,
nó dự đoán từ tiếp theo có xác suất cao nhất.
Lặp đi lặp lại quá trình đó →
ra được đoạn văn, đoạn code, bài phân tích.

Quá trình tạo ra LLM:

1. **Pre-training** —
   đọc hàng trăm tỷ token từ internet, sách, code...
   để học pattern ngôn ngữ.
   Tốn hàng triệu đô và hàng nghìn GPU.
2. **Fine-tuning** —
   huấn luyện thêm trên dữ liệu chất lượng cao,
   có hướng dẫn (instruction-following).
3. **RLHF / RLAIF** —
   dùng phản hồi từ con người (hoặc AI khác) để tinh chỉnh:
   câu trả lời nào tốt, câu nào không.

Quan trọng: LLM không có "cơ sở dữ liệu" bên trong để tra cứu.
Nó không "biết" — nó "dự đoán".
Sự khác biệt này giải thích
tại sao nó đôi khi tự tin nói sai.

### 3. AI "hiểu" hay chỉ "dự đoán token tiếp theo"?

Câu hỏi triết học
nhưng ảnh hưởng trực tiếp đến cách bạn dùng AI:

- **Nếu bạn nghĩ AI "hiểu"** →
  bạn sẽ tin nó như tin một đồng nghiệp giỏi →
  nguy hiểm khi nó sai.
- **Nếu bạn nghĩ AI chỉ "dự đoán"** →
  bạn sẽ luôn verify →
  chậm hơn nhưng an toàn hơn.

Thực tế nằm ở giữa:
LLM hiện tại thể hiện hành vi *giống như* hiểu —
nó tổng hợp, suy luận, tạo analogy.
Nhưng nó không có ý định, không có trải nghiệm,
không biết mình sai.

!!! tip "Ghi nhớ"

    Đối xử với AI như một
    **intern cực kỳ giỏi nhưng không có accountability** —
    output thường ấn tượng,
    nhưng bạn phải chịu trách nhiệm cuối cùng.

### 4. Hallucination là gì, tại sao xảy ra, có tránh được không?

Hallucination là khi AI tạo ra thông tin sai
nhưng trình bày cực kỳ tự tin —
bịa tên sách không tồn tại,
tạo API không có thật, trích dẫn nguồn không có.

**Tại sao xảy ra:**

- LLM không "tra cứu" — nó generate dựa trên pattern.
  Nếu pattern gợi ra câu trả lời dạng "tên sách + tác giả",
  nó sẽ tạo một cái, dù không tồn tại.
- Không có cơ chế "tôi không biết" mạnh mẽ.
  Model được huấn luyện để trả lời, không phải để từ chối.

**Giảm thiểu (không loại bỏ hoàn toàn):**

- Cung cấp context cụ thể (RAG, đính kèm file, paste code)
- Hỏi model tự đánh giá mức độ tự tin
- Verify mọi thông tin quan trọng:
  tên hàm, API, số liệu, trích dẫn
- Dùng tool có grounding (search, code execution)
  thay vì pure generation

### 5. Context window là gì và ảnh hưởng thế nào đến chất lượng?

Context window là lượng text tối đa
mà model "nhìn thấy" trong một lần —
bao gồm cả câu hỏi của bạn,
context đính kèm,
và câu trả lời nó đang viết.

| Model | Context window |
| --- | --- |
| GPT-4o | ~128K tokens |
| Claude 3.5 Sonnet | ~200K tokens |
| Gemini 1.5 Pro | ~2M tokens |

**Ảnh hưởng thực tế:**

- Context đầy → model "quên" phần đầu cuộc hội thoại
  (lost in the middle problem)
- Nhiều context không luôn tốt hơn —
  context đúng > context nhiều
- Chat dài → chất lượng giảm.
  Nên tách task mới ra conversation mới

Với Cursor: đây là lý do bạn nên dùng `@file`
để chỉ đúng file liên quan
thay vì để AI scan cả codebase.

### 6. Token, temperature, top-p — những tham số ảnh hưởng output thế nào?

Ba khái niệm bạn sẽ gặp thường xuyên khi dùng AI:

**Token** — đơn vị cơ bản mà LLM xử lý.
Không phải từ, không phải ký tự —
mà là "mảnh" ngôn ngữ.
Ví dụ: "engineering" = 1 token,
"kỹ thuật" có thể = 2-3 tokens.
Tiếng Việt thường tốn nhiều token hơn tiếng Anh
cho cùng nội dung.
Đây là lý do prompt tiếng Anh đôi khi hiệu quả hơn
về mặt context budget.

**Temperature** (0.0 → 2.0) — mức độ "sáng tạo" của output:

```
Temperature thấp              Temperature cao
0.0 ─────── 0.3 ─────── 0.7 ─────── 1.0
│ Chính xác, nhất quán  │ Đa dạng, sáng tạo │
│ Code, SQL, factual    │ Brainstorm, viết   │
└────────────────────────┘────────────────────┘
```

**Top-p** (0.0 → 1.0) —
giới hạn bao nhiêu token được "xem xét"
cho mỗi bước dự đoán:

- Top-p thấp → chỉ chọn từ những token
  có xác suất cao nhất → output safe, ít bất ngờ.
- Top-p cao → xem xét nhiều token hơn →
  output phong phú hơn nhưng có thể kém chính xác.

**Thực tế**: hầu hết tool (ChatGPT, Cursor)
đã chọn sẵn giá trị hợp lý.
Nhưng khi dùng API hoặc tool cho phép tùy chỉnh —
biết ý nghĩa các tham số này
giúp bạn điều chỉnh output đúng ý.

---

## Layer 2: Đánh giá năng lực — AI làm được gì, không làm được gì?

### 7. AI giỏi việc gì và dở việc gì?

**AI giỏi:**

- Tạo boilerplate, scaffold code, template
- Tóm tắt tài liệu dài
- Dịch thuật và chuyển đổi format
  (JSON → YAML, SQL → ORM)
- Giải thích code/concept phức tạp
- Brainstorm ý tưởng, liệt kê options
- Viết test cases, documentation
- Tìm bug đơn giản, suggest refactor

**AI dở (hoặc nguy hiểm nếu tin mù quáng):**

- Quyết định kiến trúc
  (thiếu context về team, infra, business)
- Debug logic phức tạp đa tầng
- Hiểu ngữ cảnh business/domain cụ thể
- Đánh giá trade-off dài hạn
- Bất cứ thứ gì cần số liệu chính xác 100%
- Hiểu code ở scale lớn
  (cross-service, distributed system)

**Nguyên tắc**: AI giỏi việc có pattern rõ ràng
và có thể verify nhanh.
AI dở việc đòi hỏi judgment, context sâu,
và hậu quả khó đảo ngược.

### 8. AI có thay thế developer/data engineer không?

Câu trả lời tỉnh táo: **không thay thế, nhưng thay đổi**.

- AI không thay developer —
  AI thay những developer không dùng AI
- Việc "gõ code" giảm giá trị.
  Việc "biết gõ code gì, tại sao, và verify kết quả"
  tăng giá trị
- Data Engineer vẫn cần hiểu data model,
  business logic, system design —
  AI không làm thay những phần này
- Nhưng Data Engineer dùng AI viết SQL,
  generate pipeline code, debug nhanh hơn →
  sẽ productive hơn gấp nhiều lần

Thay vì hỏi "AI có thay mình không?", hãy hỏi:
**"Mình cần giỏi thêm gì để AI trở thành lợi thế của mình?"**

### 9. Khi nào nên tin AI, khi nào phải verify?

| Tin được | Phải verify kỹ | Không nên tin |
| --- | --- | --- |
| Scaffold, boilerplate | Logic nghiệp vụ | Số liệu cụ thể |
| Giải thích concept | SQL phức tạp | Trích dẫn nguồn |
| Viết test template | Config hệ thống | Legal/compliance |
| Format, refactor nhỏ | Security code | Kiến trúc dài hạn |

!!! warning "Quy tắc đơn giản"

    Hậu quả của sai lầm càng lớn → verify càng kỹ.
    Sai README thì sửa 1 phút.
    Sai database migration thì mất 1 tuần.

### 10. AI coding vs AI chat — dùng khi nào?

| Loại | Tool | Khi nào dùng |
| --- | --- | --- |
| **AI coding** | Cursor, Copilot | Viết/refactor/debug trong codebase |
| **AI chat** | ChatGPT, Claude | Research, brainstorm, giải thích |
| **AI search** | Perplexity, Gemini | Tra cứu mới, verify fact |

Sai lầm phổ biến:
dùng ChatGPT để viết code dài (thiếu context codebase),
hoặc dùng Cursor để research concept
(không cần file context).

### 11. RAG, Fine-tuning, Prompt Engineering — khác nhau thế nào?

Ba cách "customize" AI cho nhu cầu riêng,
từ đơn giản đến phức tạp:

| Phương pháp | Cách hoạt động | Effort |
| --- | --- | --- |
| **Prompt Engineering** | Viết hướng dẫn tốt hơn | Thấp |
| **RAG** | Đính kèm dữ liệu riêng vào context | Trung bình |
| **Fine-tuning** | Huấn luyện lại model trên data riêng | Cao |

Với hầu hết engineer:
**Prompt Engineering + RAG là đủ**.
Fine-tuning chỉ cần khi bạn build AI product.

### 12. So sánh models — khi nào dùng model nào?

Không có "model tốt nhất".
Có "model phù hợp nhất cho task":

| Model | Điểm mạnh | Phù hợp cho |
| --- | --- | --- |
| **GPT-4o** | Cân bằng, multimodal | General purpose |
| **Claude** | Context dài, reasoning | Code review, viết dài |
| **Gemini** | Context 2M tokens | Research, tài liệu dài |
| **Local** (Llama) | Miễn phí, privacy | Task đơn giản |

**Chiến lược thực tế:**

- Dùng thử 2-3 model cho cùng task →
  so sánh chất lượng
- Coding: Claude thường cho code chặt chẽ hơn.
  GPT-4o nhanh hơn cho task nhỏ.
- Research: Gemini + search grounding,
  hoặc Perplexity
- Viết dài: Claude giữ tone nhất quán hơn
  qua context dài

Đừng loyal với một model — loyal với kết quả.

### 13. AI miễn phí vs trả phí — đầu tư bao nhiêu là đủ?

| Tier | Chi phí | Được gì |
| --- | --- | --- |
| **Free** | $0 | Model yếu hơn, giới hạn request |
| **Pro** | ~$20/tháng | Model mạnh nhất, higher limits |
| **Cursor Pro** | ~$20/tháng | AI coding, Agent mode |
| **API** | Pay per use | Control hoàn toàn |

**ROI thực tế**:
nếu AI tiết kiệm cho bạn 1 giờ/tuần,
$20/tháng là rẻ hơn cà phê.
Với engineer dùng AI mỗi ngày,
Cursor Pro + một AI chat Pro
là đầu tư tối thiểu nên có.

**Nguyên tắc**: bắt đầu với free để hiểu workflow →
upgrade khi chạm giới hạn →
đo lường xem có thực sự dùng hết không.
Đừng trả tiền cho tool bạn không dùng đủ.

### 14. Mình cần giỏi thêm gì để AI trở thành lợi thế?

Nghịch lý: AI càng mạnh,
engineering fundamentals càng quan trọng. Vì:

- AI viết code cho bạn →
  bạn cần **biết code nào đúng, code nào sai**
  (verification skill)
- AI generate nhanh →
  bạn cần **biết nên build cái gì**
  (problem decomposition)
- AI trả lời mọi thứ →
  bạn cần **biết hỏi đúng câu hỏi**
  (critical thinking)
- AI không hiểu system →
  bạn cần **system thinking**
  để AI không phá kiến trúc

**5 kỹ năng mà AI khuếch đại thay vì thay thế:**

1. **Problem decomposition** —
   chia bài toán lớn thành task AI có thể xử lý
2. **Verification & review** —
   đọc và đánh giá output AI nhanh, chính xác
3. **Domain knowledge** —
   hiểu business logic mà AI không biết
4. **System design** —
   nhìn bức tranh tổng thể, trade-off dài hạn
5. **Prompt craft** —
   nói chuyện với AI hiệu quả (xem Layer 3)

!!! important "AI là force multiplier"

    ```
    Skill của bạn × AI = Output
    ────────────────────────────
         0        ×  5  =   0
         1        ×  5  =   5
         3        ×  5  =  15  ← lợi thế khổng lồ
    ```

---

## Layer 3: Prompt Engineering — nói chuyện với AI thế nào cho hiệu quả?

### 15. Prompt tốt vs prompt dở khác nhau thế nào?

**Prompt dở:**
> Viết cho tôi một pipeline

**Prompt tốt:**
> Tôi cần một Airflow DAG bằng Python
> chạy hàng ngày lúc 6h sáng.
> DAG gồm 3 task:
> extract từ PostgreSQL (bảng orders, record ngày hôm trước),
> transform bằng pandas (thêm cột revenue = quantity * price),
> load vào BigQuery (dataset analytics, bảng daily_orders).
> Dùng TaskFlow API. Retry 3 lần, timeout 30 phút.

!!! tip "Checklist prompt tốt"

    - [x] **Cụ thể** — nói rõ input, output, constraint
    - [x] **Có context** — nêu stack, convention, environment
    - [x] **Có scope** — giới hạn rõ AI cần làm gì, không làm gì
    - [x] **Có format** — nói trước bạn muốn output dạng gì

### 16. Các kỹ thuật prompt

**Zero-shot**: hỏi thẳng, không cho ví dụ.
Đủ cho câu hỏi đơn giản.

**Few-shot**: cho 2-3 ví dụ mẫu trước khi hỏi.
AI sẽ bắt chước pattern.

**Chain-of-thought**: yêu cầu AI "suy nghĩ từng bước".
Hiệu quả cho bài toán logic, debug, phân tích.
> "Phân tích từng bước tại sao query này chậm,
> rồi đề xuất cách tối ưu."

**Role-play**: gán vai cho AI để thay đổi góc nhìn.
> "Bạn là một senior Data Engineer 10 năm kinh nghiệm.
> Review đoạn code này và chỉ ra vấn đề tiềm ẩn
> khi scale lên 100x data."

**Contrarian**: yêu cầu AI phản biện chính output của nó.
> "Hãy chỉ ra 3 điểm yếu lớn nhất
> của giải pháp bạn vừa đề xuất."

### 17. Làm sao để AI cho output có cấu trúc?

Nói thẳng format bạn muốn trong prompt:

- "Trả lời dạng bảng markdown:
  Tool, Ưu điểm, Nhược điểm, Khi nào dùng"
- "Output JSON với schema:
  `{name: string, type: enum[batch, stream]}`"
- "Viết dạng ADR: Context, Decision, Consequences"
- "List dạng numbered, mỗi item tối đa 2 câu"

AI rất giỏi theo format — nhưng bạn phải nói rõ.
Nếu không, nó sẽ chọn format nó "thích"
(thường là văn dài dòng).

### 18. Khi AI trả lời sai, sửa thế nào?

**Đừng hỏi lại từ đầu.**
Sửa trong conversation hiện tại hiệu quả hơn:

- "Không đúng. Phần X sai vì Y.
  Sửa lại phần đó, giữ nguyên phần còn lại."
- "Gần đúng nhưng thiếu Z. Bổ sung thêm."
- "Approach này không phù hợp vì constraint A.
  Thử approach khác."

**Khi nào nên bắt đầu conversation mới:**

- AI lặp lại cùng lỗi sau 2-3 lần sửa
- Context window quá dài, AI bắt đầu mâu thuẫn
- Bạn muốn thay đổi hoàn toàn hướng tiếp cận

### 19. System prompt / custom instructions hoạt động thế nào?

System prompt là phần hướng dẫn "ẩn"
mà AI đọc trước mọi tin nhắn của bạn. Nó quyết định:

- AI nói ngôn ngữ gì, phong cách gì
- AI biết context gì về project/domain của bạn
- AI nên ưu tiên gì
  (ngắn gọn vs chi tiết, an toàn vs sáng tạo)

Trong Cursor → đó là **Rules** (`.cursor/rules/`).
Trong ChatGPT → **Custom Instructions**.
Trong Claude → **Project Instructions**.

Viết system prompt giống viết onboarding doc
cho một đồng nghiệp mới:
nói rõ stack, convention, những thứ cần tránh,
tone & style.

### 20. Multi-turn prompting — dẫn dắt AI qua nhiều lượt

Một prompt hoàn hảo ngay từ đầu
là lý tưởng nhưng hiếm khi thực tế.
Thay vào đó, hãy dẫn dắt AI qua nhiều lượt —
giống pair programming hơn là giao task.

**Pattern hiệu quả:**

``` mermaid
sequenceDiagram
    participant You as Bạn
    participant AI as AI

    You->>AI: Scope — "Tôi cần X. Hỏi tôi để hiểu rõ."
    AI->>You: Hỏi lại để clarify
    You->>AI: Trả lời → AI đề xuất approach
    AI->>You: Đề xuất A, B, C
    You->>AI: "OK, approach B. Implement đi."
    AI->>You: Output draft
    You->>AI: "Đúng rồi, sửa phần X theo Y."
    AI->>You: Output final
```

**Sai lầm phổ biến:**

- Nhồi mọi thứ vào 1 prompt dài →
  AI bỏ sót yêu cầu
- Không cho AI hỏi lại →
  AI đoán sai context
- Bắt đầu lại từ đầu mỗi khi output chưa perfect →
  lãng phí context đã xây

**Quy tắc ngón tay cái**:
nếu task cần hơn 3 phút để giải thích cho con người,
nó nên là multi-turn với AI.

### 21. Context management — cung cấp context thế nào cho AI hiểu đúng?

Context là "vũ khí" mạnh nhất
để nâng chất lượng AI output.
Nhưng context nhiều ≠ context tốt.

!!! info "Framework WECS cho context"

    | | Yếu tố | Câu hỏi tự kiểm tra |
    | :---: | --- | --- |
    | **W** | **What** — Task | Bạn đang làm gì? |
    | **E** | **Environment** | Stack, constraint nào? |
    | **C** | **Code/Data** | Paste đúng phần cần? |
    | **S** | **Success** | Output tốt trông thế nào? |

**Ví dụ:**

Dở: "Fix cái query này" + paste query 100 dòng.

Tốt: "Query này chạy 45 giây, cần dưới 5 giây.
Bảng orders có 10M rows, partition by date.
Index có trên customer_id và order_date.
Chạy trên PostgreSQL 15.
Đây là EXPLAIN ANALYZE output: [paste].
Focus vào phần sequential scan."

**Trong Cursor**: dùng `@file` thay vì paste code →
AI có context chính xác hơn
và đồng bộ với codebase thật.

### 22. Meta-prompting — dùng AI để viết prompt tốt hơn

Bạn không cần giỏi viết prompt ngay từ đầu.
Dùng AI để bootstrap:

**Cách 1 — Nhờ AI viết prompt:**
> "Tôi muốn AI giúp viết unit test
> cho Python function xử lý JSON parsing.
> Hãy viết prompt tốt nhất để hỏi câu này."

**Cách 2 — Nhờ AI cải thiện prompt:**
> "Đây là prompt tôi đang dùng: [paste].
> Cải thiện nó để output chính xác hơn.
> Giải thích thay đổi."

**Cách 3 — Nhờ AI tạo prompt template:**
> "Tôi thường cần AI review SQL cho performance.
> Tạo prompt template tái sử dụng —
> chỗ nào cần điền thì đánh dấu [placeholder]."

Meta-prompting đặc biệt hữu ích khi:

- Bạn bắt đầu dùng AI cho task type mới
- Output AI cứ kém mà không biết fix prompt thế nào
- Bạn muốn chuẩn hóa prompt cho team

### 23. Prompt library — xây thư viện prompt riêng

Engineer giỏi không nhớ code —
họ biết tìm ở đâu. Prompt cũng vậy.

**Nên lưu prompt cho các task lặp lại:**

| Category | Template |
| --- | --- |
| **Code review** | "Review code. Focus: [X]. Output: issue theo severity." |
| **Debug** | "Error: [paste]. Context: [stack]. Đã thử: [X]." |
| **Learning** | "Giải thích [concept]. Level: [X]. Cho ví dụ." |
| **Docs** | "Viết docstring. Format: Google style." |
| **Compare** | "So sánh [A] vs [B]. Tiêu chí: [list]." |

**Lưu ở đâu:**

- File markdown trong project (dùng với Cursor Rules)
- ChatGPT Custom Instructions / Claude Projects
- Notion, Obsidian, hoặc bất cứ nơi bạn ghi chú

**Quy tắc**: mỗi khi AI cho output xuất sắc →
save lại prompt đó.
Sau 1 tháng bạn sẽ có bộ sưu tập cực giá trị.

---

## Layer 4: Tối ưu AI tools — thực hành hàng ngày

### 24. Cursor: Agent vs Ask vs Manual — khi nào dùng mode nào?

| Mode | Khi nào | Ví dụ |
| --- | --- | --- |
| **Agent** | Nhiều bước, nhiều file | Rename + cập nhật references |
| **Ask** | Hỏi, phân tích | "Giải thích code này" |
| **Manual** | Sửa nhỏ, inline | Refactor 1 hàm |

Sai lầm phổ biến:
dùng Agent cho mọi thứ →
AI sửa lung tung nhiều file, khó kiểm soát.
Hoặc dùng Ask rồi copy-paste thủ công →
chậm và dễ sai.

### 25. Cursor Rules thiết kế thế nào?

Rules giống "bộ não" của AI trong project bạn.
Nên có:

```markdown
# Project context
- Stack: Python, MkDocs Material, uv
- Blog viết bằng tiếng Việt,
  thuật ngữ kỹ thuật giữ tiếng Anh
- File naming: tiếng Việt không dấu, dùng `-`

# Code conventions
- Không thêm comment giải thích obvious code
- Prefer editing existing files

# Domain knowledge
- Blog cá nhân về data engineering
- Categories: Level Up, Soft Skills, AI,
  How-To, Kubernetes, Databases
```

Rules cụ thể theo project > rules chung chung.
Update rules khi phát hiện AI lặp lại cùng lỗi.

### 26. Workflow: AI viết trước hay bạn viết trước?

Hai workflow, phù hợp hai loại task khác nhau:

<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px" markdown>

<div markdown>
**AI-first — cần tốc độ**

``` mermaid
graph TD
    A1["Mô tả yêu cầu"] -->
    A2["AI generate draft"] -->
    A3["Bạn review & sửa"] -->
    A4["AI refine"] -->
    A5["Bạn finalize"]
    style A1 fill:#e3f2fd,stroke:#1565c0
    style A2 fill:#fff3e0,stroke:#e65100
    style A3 fill:#e3f2fd,stroke:#1565c0
    style A4 fill:#fff3e0,stroke:#e65100
    style A5 fill:#e8f5e9,stroke:#2e7d32
```
</div>

<div markdown>
**Human-first — cần suy nghĩ sâu**

``` mermaid
graph TD
    B1["Bạn sketch ý tưởng"] -->
    B2["AI expand chi tiết"] -->
    B3["Bạn sửa cho đúng intent"] -->
    B4["AI polish format"] -->
    B5["Bạn finalize"]
    style B1 fill:#e3f2fd,stroke:#1565c0
    style B2 fill:#fff3e0,stroke:#e65100
    style B3 fill:#e3f2fd,stroke:#1565c0
    style B4 fill:#fff3e0,stroke:#e65100
    style B5 fill:#e8f5e9,stroke:#2e7d32
```
</div>

</div>

Xanh = bạn. Cam = AI. Xanh lá = done.

Viết blog? AI-first cho draft,
human-first cho ý tưởng cốt lõi.
Thiết kế database schema?
Human-first cho model, AI-first cho DDL code.

### 27. Giữ code quality khi dùng AI nhiều

AI generate nhanh →
dễ tạo tech debt nếu không kiểm soát:

- **Luôn đọc code AI generate** —
  không blind accept.
  Nếu bạn không hiểu dòng code, đừng merge nó.
- **AI không thay thế code review** —
  vẫn cần human review,
  đặc biệt cho logic nghiệp vụ.
- **Cẩn thận "AI-generated bloat"** —
  AI thích viết dài, thêm edge case không cần thiết,
  thêm abstraction thừa.
- **Test vẫn phải chạy** —
  AI viết code trông đúng nhưng sai logic.
  Test là safety net cuối cùng.
- **Commit thường xuyên** —
  AI sửa nhiều file cùng lúc.
  Commit nhỏ, thường xuyên giúp rollback dễ hơn.

### 28. AI cho Data Engineer cụ thể

Những use case AI thực sự tiết kiệm thời gian:

| Use case | Prompt gợi ý |
| --- | --- |
| Viết SQL | "Window function running total by month" |
| Debug pipeline | "DAG fail task X error Y. Phân tích." |
| Generate schema | "Từ JSON này, tạo BigQuery schema." |
| Documentation | "Docstring: input, output, edge cases." |
| So sánh tools | "Airflow vs Dagster: team 3, 50 DAGs, K8s." |
| Code review | "Focus: scale 100x, error handling." |
| Học concept | "CAP theorem, level junior, 3 ví dụ." |

### 29. Cursor context: @file, @folder, @codebase, @web — khi nào dùng gì?

Context trong Cursor quyết định
AI "biết" bao nhiêu về project:

| Context | Token cost | Khi nào dùng |
| --- | --- | --- |
| **@file** | Thấp | Biết chính xác file liên quan |
| **@folder** | Trung bình | Task liên quan cả module |
| **@codebase** | Cao | Cần tìm across project |
| **@web** | Thấp-TB | Cần thông tin bên ngoài |
| **@docs** | Trung bình | Cần reference docs cụ thể |

**Chiến lược context tiết kiệm:**

1. Bắt đầu hẹp: `@file` cụ thể
2. Mở rộng nếu AI thiếu context:
   thêm `@file` khác, hoặc dùng `@folder`
3. Dùng `@codebase` chỉ khi không biết code nằm ở đâu
4. Kết hợp: `@file config.py` +
   `@web "MkDocs Material hooks docs"`

**Sai lầm**: không dùng @ gì cả → AI đoán mù.
Hoặc `@codebase` cho mọi thứ →
tốn token, context bị loãng.

### 30. Dùng AI để đọc hiểu code — onboard codebase mới

Một trong những use case mạnh nhất
mà nhiều người bỏ qua:
**dùng AI để hiểu code nhanh hơn**.

**Khi onboard project mới:**

1. Mở Cursor, dùng Ask mode:
   "Mô tả kiến trúc tổng quan của project này."
2. Chỉ vào file entry point:
   "@file main.py — Trace flow từ request đến response."
3. Hỏi về convention:
   "@folder src/ — Project này dùng pattern gì?"

**Khi đọc code người khác:**

- "Giải thích function này làm gì.
  Cần hiểu business logic, không cần syntax."
- "Tìm tất cả side effects —
  database call, API call, file write."
- "Vẽ data flow: input gì → qua đâu → output gì?"

**Khi đọc codebase lớn:**

- "Tìm tất cả nơi gọi function X.
  Phân tích impact nếu thay đổi signature."
- "So sánh cách module A và B handle error.
  Có nhất quán không?"

AI đọc code nhanh hơn bạn.
Nhưng bạn phải biết hỏi đúng câu hỏi
và verify answer.

### 31. AI-first daily workflow — thiết kế ngày làm việc với AI

Chuyển từ "thỉnh thoảng dùng AI"
sang "AI là default" đòi hỏi thay đổi thói quen:

**Sáng — Plan với AI:**

- Paste task list vào AI:
  "Đây là task hôm nay. Suggest thứ tự ưu tiên,
  ước lượng thời gian,
  và cách AI có thể hỗ trợ từng task."
- Dùng AI để break down task phức tạp
  trước khi bắt tay làm.

**Trong ngày — Pair với AI cho mọi task:**

- Viết code → Cursor Agent/Manual
- Research → AI chat (ChatGPT/Claude)
- Debug → paste error + context vào AI trước khi Google
- Documentation → AI draft, bạn review
- Meeting prep →
  "Tóm tắt 5 key points về [topic] trong 10 phút"

**Cuối ngày — Review với AI:**

- "Đây là những gì tôi làm hôm nay.
  Có pattern nào tôi nên tối ưu không?"
- Lưu lại prompt nào hiệu quả,
  workflow nào tiết kiệm thời gian.

**Mục tiêu**: sau 2 tuần,
"hỏi AI trước" trở thành phản xạ tự nhiên —
không phải vì lười nghĩ,
mà vì AI là bước khởi đầu nhanh nhất
để đi từ 0 → 80%.

---

## Layer 5: AI-Augmented Growth — dùng AI để phát triển bản thân

### 32. AI-augmented learning — dùng AI để học nhanh hơn

AI là gia sư tốt nhất bạn từng có:
luôn available, kiên nhẫn vô hạn,
điều chỉnh theo level của bạn,
và có kiến thức bao trùm hầu hết mọi lĩnh vực.

**Kỹ thuật học với AI:**

**Feynman Technique + AI**:
học concept → giải thích lại cho AI →
nhờ AI chỉ ra chỗ hiểu sai.
> "Tôi sẽ giải thích cách Kafka partition hoạt động.
> Hãy chỉ ra chỗ nào tôi hiểu sai hoặc thiếu."

**Progressive deepening**:
bắt đầu high-level, đào sâu dần.
> Lượt 1: "Giải thích database indexing ở mức overview."
> Lượt 2: "Giải thích B-tree index chi tiết hơn."
> Lượt 3: "Khi nào dùng B-tree vs hash vs GIN?
> Cho ví dụ với PostgreSQL."

**AI-powered quizzing**: nhờ AI kiểm tra kiến thức.
> "Tạo 10 câu hỏi về Docker networking,
> level intermediate.
> Hỏi từng câu, đợi tôi trả lời, rồi đánh giá."

**Analogy bridge**:
dùng AI để nối kiến thức mới với kiến thức đã có.
> "Giải thích Kubernetes ReplicaSet
> bằng analogy với thứ tôi đã biết —
> tôi là Data Engineer quen với Airflow."

### 33. Dùng AI để xây dựng Engineering Foundation

AI không chỉ giúp bạn làm nhanh hơn —
nó giúp bạn **học sâu hơn**
những thứ fundamental mà bạn chưa kịp học.

**Roadmap gợi ý — dùng AI để bổ sung foundation:**

| Foundation | Cách AI hỗ trợ |
| --- | --- |
| **DS & Algorithms** | Trace execution, so sánh complexity |
| **System Design** | Phân tích trade-off, simulate load |
| **Networking** | TCP/HTTP/DNS ở mức bạn cần |
| **Database internals** | EXPLAIN ANALYZE, index strategy |
| **Operating System** | Process, thread, memory |
| **Design Patterns** | Code example trong stack của bạn |

**Workflow cụ thể:**

1. Chọn 1 topic/tuần (ví dụ: "database indexing")
2. Hỏi AI: "Tạo learning plan cho topic X,
   5 ngày, mỗi ngày 30 phút.
   Level: intermediate Data Engineer."
3. Mỗi ngày: đọc material AI suggest →
   thực hành → hỏi AI khi stuck
4. Cuối tuần: nhờ AI quiz để kiểm tra retention

**Lợi thế lớn nhất**:
AI cá nhân hóa learning theo gap của bạn.
Thay vì đọc sách 500 trang,
bạn hỏi AI đúng phần bạn chưa biết →
tiết kiệm 80% thời gian.

### 34. AI-first mindset — thay đổi tư duy để bắt kịp thời đại

AI-first không phải "dùng AI cho mọi thứ".
AI-first là **thay đổi default behavior**:
trước mỗi task, câu hỏi đầu tiên là
"AI có thể giúp gì ở bước này?"

**Tư duy cũ vs AI-first:**

| Tư duy cũ | AI-first |
| --- | --- |
| Google → đọc 5 bài → tổng hợp | Hỏi AI → verify nếu cần |
| Viết code từ scratch | AI draft → bạn review |
| Đọc docs từ đầu đến cuối | Hỏi AI đúng phần cần |
| Debug bằng print/log | Paste error → AI phân tích |
| Course dài 40 giờ | AI tạo plan cá nhân |

**AI-first ≠ AI-only:**

- AI-first: bắt đầu với AI, sau đó apply judgment,
  verify, enhance bằng kinh nghiệm.
- AI-only: blindly accept mọi output → nguy hiểm.

**Chiến lược đuổi kịp:**

``` mermaid
graph LR
    A["Tuần 1-2\nDùng AI mọi task"] -->
    B["Tuần 3-4\nRefine workflow"]
    B -->
    C["Tháng 2+\nPrompt library"]
    C -->
    D["Tháng 3+\nAI = gia sư"]
    style A fill:#e3f2fd,stroke:#1565c0
    style B fill:#e8f5e9,stroke:#2e7d32
    style C fill:#fff3e0,stroke:#e65100
    style D fill:#fce4ec,stroke:#c62828
```

**Mục tiêu**: AI không phải tool bạn mở khi cần —
AI là "đồng đội invisible"
luôn có mặt trong workflow.

### 35. Track và đo lường: AI có thực sự giúp bạn tốt hơn?

Dùng AI nhiều không đồng nghĩa dùng AI hiệu quả.
Cần đo lường:

**Metrics nên track:**

- **Thời gian**: task X trước khi dùng AI mất bao lâu?
  Giờ mất bao lâu?
- **Chất lượng**: code AI generate có cần sửa nhiều không?
  Bug rate tăng hay giảm?
- **Learning velocity**: bạn có đang học nhanh hơn không?
  Tuần này biết thêm gì mà tuần trước chưa biết?
- **Autonomy**: bạn có thể làm task mà không có AI không?
  Hay đã phụ thuộc đến mức không thể?

**Anti-patterns cần tránh:**

| Anti-pattern | Dấu hiệu | Cách sửa |
| --- | --- | --- |
| **Skill atrophy** | Không thể code mà không có AI | Code manual 1-2 task/tuần |
| **Blind trust** | Accept mà không đọc | Đọc diff trước khi accept |
| **Context laziness** | Prompt lười | Dùng WECS (câu 21) |
| **Tool hopping** | Nhảy 5 tools | Chọn 2: coding + chat |
| **Learning bypass** | Skip hiểu, lấy output | Hỏi "tại sao" mỗi task |

**Review hàng tháng**: dành 30 phút cuối tháng tự hỏi —
"AI đang giúp mình grow,
hay đang giúp mình tránh grow?"

---

## Kết luận

AI không phải phép thuật.
AI là một công cụ cực mạnh —
nhưng mạnh đến đâu phụ thuộc vào người dùng.

35 câu hỏi trên không phải checklist
để "biết hết về AI".
Chúng là framework để bạn
**tự đánh giá và phát triển** —
từ bản chất (Layer 1), đến khả năng (Layer 2),
đến cách giao tiếp (Layer 3),
đến thực hành hàng ngày (Layer 4),
đến phát triển bản thân (Layer 5).

!!! success "Chiến lược 3 giai đoạn"

    ``` mermaid
    graph LR
        A["AI-first<br/>Bắt kịp thời đại"] -->
        B["Foundation<br/>AI = gia sư"]
        B -->
        C["Human-first<br/>Bạn quyết định"]
        style A fill:#e3f2fd,stroke:#1565c0
        style B fill:#fff3e0,stroke:#e65100
        style C fill:#e8f5e9,stroke:#2e7d32
    ```

Giống như bài [Học nhanh. Nhớ lâu.](../level-up/hoc-nhanh-nho-lau.md)
đã nói: máy tính lưu tệp, não lưu liên kết.
AI generate output,
nhưng **bạn là người tạo ra judgment**.
Và judgment chỉ đến khi bạn hiểu cái bạn đang dùng.

**Dùng AI như dùng GPS:
nó chỉ đường, nhưng bạn phải biết mình muốn đi đâu —
và nhận ra khi nó dẫn sai lối.**
