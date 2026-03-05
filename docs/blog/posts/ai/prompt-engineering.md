---
date: 2026-03-05
categories:
  - AI
tags:
  - prompt-engineering
  - cursor
  - ai
  - productivity
---

# Prompt Engineering — từ làm quen đến thuần thục

Cùng một câu hỏi, người viết prompt tốt nhận output gấp nhiều lần
chất lượng hơn — nhưng phần lớn chỉ biết "gõ câu hỏi vào ChatGPT".
Prompt Engineering không phải mánh lới; nó là kỹ năng giao tiếp với
AI: rõ ràng, có cấu trúc, biết khi nào dùng kỹ thuật gì.

Bài viết này đưa bạn từ **làm quen** (prompt là gì, tại sao quan
trọng) đến **thuần thục** (workflow thực tế, kết hợp với Cursor).
Prompt Engineering + Cursor sẽ thành **bộ đôi** xử lý công việc hiệu
quả: bạn biết hỏi đúng, Cursor biết đúng context để trả lời.

<!-- more -->

!!! abstract "Hành trình: làm quen → hiệu quả → thuần thục"

    | Giai đoạn | Nội dung | Kết hợp Cursor |
    | --- | --- | --- |
    | **Làm quen** | Prompt là gì, thành phần, kỹ thuật cơ bản | — |
    | **Hiệu quả** | Cấu trúc prompt, context, multi-turn | @file, Rules |
    | **Thuần thục** | Workflow thực tế, anti-patterns, thư viện prompt | Agent + prompt tốt |

    ``` mermaid
    graph LR
        PE["Prompt Engineering<br/>Bạn hỏi đúng"] --> Duo["Bộ đôi"]
        Cursor["Cursor<br/>Context đúng"] --> Duo
        Duo --> Output["Output chất lượng"]
    ```

---

## Phần I — Hiểu Prompt Engineering

### 1. Prompt Engineering là gì?

Prompt Engineering là cách bạn **soạn và tổ chức lời nhắn** gửi
cho AI để nhận được output đúng ý, đủ dùng, dễ verify. Không phải
"hack" AI hay học câu thần chú — mà là **giao tiếp có phương pháp**.

LLM không đọc suy nghĩ của bạn. Nó chỉ thấy chuỗi token bạn gửi.
Prompt dở = input mơ hồ = output generic hoặc sai. Prompt tốt =
input rõ ràng = output sát yêu cầu.

| Hiểu sai | Đúng |
| --- | --- |
| "Prompt engineering = vài từ khóa đặc biệt" | = Cấu trúc + context + ràng buộc |
| "Chỉ cần hỏi tự nhiên" | Tự nhiên nhưng phải đủ thông tin |
| "AI thông minh, đoán được ý mình" | AI dự đoán token — càng rõ càng đúng |

---

### 2. Tại sao tồn tại?

Trước khi có LLM phổ biến, "giao tiếp với máy" là lập trình: cú
pháp chặt chẽ, máy không đoán. LLM cho phép ngôn ngữ tự nhiên —
nhưng **tự nhiên không đồng nghĩa với hiệu quả**. Prompt Engineering
tồn tại vì:

- **Context window có giới hạn** — bạn phải chọn đúng thứ đưa vào.
- **Model không biết ngữ cảnh của bạn** — project, stack, convention.
- **Output không có chuẩn mặc định** — dài/ngắn, format, tone đều
  do bạn chỉ rõ.

Mục tiêu: **giảm số lần "sửa lại giúp tôi"** và tăng xác suất
output dùng được ngay.

---

### 3. Bên trong một prompt tốt có gì?

Một prompt hiệu quả thường gồm vài thành phần. Không bắt buộc đủ
tất cả mọi lúc — nhưng biết chúng giúp bạn thiếu gì thì bổ sung gì.

``` mermaid
graph TD
    subgraph Prompt["Prompt"]
        R["Role / Vai trò"]
        C["Context / Ngữ cảnh"]
        T["Task / Nhiệm vụ"]
        F["Format / Định dạng"]
        X["Constraints / Ràng buộc"]
    end
    R --> O["Output chất lượng"]
    C --> O
    T --> O
    F --> O
    X --> O
```

| Thành phần | Mục đích | Ví dụ |
| --- | --- | --- |
| **Role** | Định hướng góc nhìn, độ sâu | "Bạn là senior Data Engineer..." |
| **Context** | Cho AI biết môi trường, dữ liệu | Stack, file đính kèm, lỗi cụ thể |
| **Task** | Nói rõ cần làm gì | "Viết unit test cho function X" |
| **Format** | Output trông thế nào | "Bảng markdown", "JSON schema" |
| **Constraints** | Giới hạn, điều tránh | "Không thêm dependency mới" |

**Ví dụ so sánh:**

???+ example "Prompt dở vs tốt"

    **Dở:** *"Viết cho tôi một pipeline."*

    Thiếu: context (stack, data), task cụ thể, format, ràng buộc.

    **Tốt:** *"Project dùng Airflow, Python 3.12. Cần DAG chạy
    hàng ngày lúc 6h: (1) extract từ PostgreSQL bảng orders
    theo ngày, (2) transform thêm cột revenue = quantity * price,
    (3) load vào BigQuery bảng daily_orders. Output: 1 file Python
    DAG, dùng TaskFlow API, retry 3 lần. Không dùng operator
    mới ngoài PostgresHook và BigQuery."*

    Có đủ: context, task từng bước, format (1 file), constraints.

---

### 4. Các kỹ thuật cơ bản — khi nào dùng gì?

| Kỹ thuật | Cách làm | Khi nào dùng |
| --- | --- | --- |
| **Zero-shot** | Hỏi thẳng, không ví dụ | Câu hỏi đơn giản, rõ ràng |
| **Few-shot** | Cho 2–3 ví dụ input → output trước khi hỏi | AI cần bắt chước pattern (format, style) |
| **Chain-of-thought** | Yêu cầu "suy nghĩ từng bước" | Logic, debug, phân tích nguyên nhân |
| **Role-play** | Gán vai cho AI | Review, đánh giá, góc nhìn chuyên môn |
| **Contrarian** | Bảo AI phản biện chính output | Kiểm tra điểm yếu, edge case |

**Flow chọn nhanh:**

``` mermaid
graph TD
    Q{"Task của bạn?"} --> Simple["Đơn giản, 1 bước"]
    Q --> Pattern["Cần format/pattern cụ thể"]
    Q --> Reason["Cần suy luận, phân tích"]
    Q --> Review["Cần review, đánh giá"]
    Simple --> Z["Zero-shot"]
    Pattern --> F["Few-shot"]
    Reason --> C["Chain-of-thought"]
    Review --> R["Role-play"]
```

!!! tip "Kết hợp với Cursor"

    Trong Cursor, **context** thường do bạn cung cấp qua `@file`,
    `@codebase` — không cần paste dài vào prompt. Bạn tập trung
    vào **task + format + constraints**; Cursor lo phần đưa code
    vào context.

---

## Phần II — Sử dụng hiệu quả

### 5. Ba cấp prompt — từ đơn giản đến phức tạp

Giống Cursor có 3 cấp tương tác (Tab → Inline Edit → Agent),
prompt cũng có 3 cấp. Dùng cấp **đủ thấp** cho task — không cần
prompt dài cho việc nhỏ.

---

**Cấp 1 — Prompt một dòng**

Một câu, rõ việc cần làm. Đủ cho autocomplete, sửa nhỏ, hỏi nhanh.

- *"Đổi tên biến `x` thành `request_id`"*
- *"Thêm docstring Google style cho function này"*
- *"Giải thích dòng 42 làm gì"*

Trong Cursor: dùng với Inline Edit (++ctrl+k++) hoặc Tab.
Không cần role, format — context đã có từ file đang mở.

---

**Cấp 2 — Prompt có cấu trúc (role + task + format)**

Task cần output có hình dạng rõ ràng: bảng, list, code block,
ADR.

Ví dụ:

> Bạn là Data Engineer review code. Task: review @file pipeline.py.
> Focus: error handling và idempotency. Output: bảng markdown
> 3 cột — Vấn đề, Mức độ (High/Medium/Low), Đề xuất.

Trong Cursor: Ask mode + `@file`. Rules có thể đã set sẵn role
(project convention) — prompt của bạn chỉ cần task + format.

---

**Cấp 3 — Multi-turn (nhiều lượt)**

Task phức tạp, nhiều bước, hoặc cần clarify trước khi implement.
Bạn và AI qua vài lượt: scope → approach → chi tiết → output.

Pattern: **Scope trước, implement sau.** Giống Plan mode trong
Cursor: lượt 1 mô tả tổng thể, AI hỏi lại hoặc đề xuất, bạn
chốt rồi mới bảo implement.

!!! tip "Bộ đôi PE + Cursor"

    - **Prompt tốt** = bạn nói rõ task, format, ràng buộc.
    - **Cursor** = đưa đúng @file / @codebase / Rules vào context.
    - Thiếu một trong hai: output kém. Đủ cả hai: ít sửa lại,
      nhanh đạt đúng ý.

---

### 6. Framework context — WECS

Khi output AI sai hoặc thiếu, thường là thiếu **context**. WECS
giúp bạn tự kiểm tra:

| Chữ | Yếu tố | Câu hỏi |
| --- | --- | --- |
| **W** | What | Bạn đang làm task gì? |
| **E** | Environment | Stack, version, constraint? |
| **C** | Code/Data | Đã đưa đúng file/đoạn code/data chưa? |
| **S** | Success | Output tốt trông thế nào? (format, độ dài) |

Trong Cursor: **C** thường giải quyết bằng `@file` / `@folder` /
`@codebase`. **E** có thể ghi trong Rules (stack, convention).
Bạn chỉ cần nhấn mạnh **W** và **S** trong prompt.

---

### 7. Kết hợp Prompt Engineering với Cursor

Hai thứ bổ sung cho nhau:

``` mermaid
graph LR
    subgraph Your["Bạn"]
        PE["Prompt: role, task, format, constraints"]
    end
    subgraph Cursor["Cursor"]
        CTX["Context: @file, @codebase, Rules"]
        MODE["Mode: Ask / Agent / Plan / Inline"]
    end
    PE --> Result["Output"]
    CTX --> Result
    MODE --> Result
```

**Rules = system prompt dài hạn.** Những gì lặp lại mọi conversation
(stack, ngôn ngữ, convention) → đưa vào `.cursor/rules/`. Prompt
của bạn chỉ cần **task cụ thể** cho lần đó.

**@ context = đưa đúng thứ vào.** Không cần paste 500 dòng code —
`@file path/to/file.py`. Prompt ngắn gọn, context chính xác.

**Chọn mode đúng.** Ask để hiểu, Plan để lên kế hoạch, Agent để
implement. Prompt "thêm endpoint X theo pattern Y" phù hợp Agent +
`@file` router hiện có. Prompt "giải thích flow" phù hợp Ask +
`@codebase`.

!!! success "Tóm tắt bộ đôi"

    | Bạn (Prompt) | Cursor |
    | --- | --- |
    | Nói rõ task, format, constraints | Cung cấp đúng context (@, Rules) |
    | Chọn kỹ thuật (few-shot, CoT, role) | Chọn mode (Ask / Agent / Plan) |
    | Multi-turn khi task phức tạp | Plan mode + Agent theo từng bước |

---

## Phần III — Thuần thục

### 8. Workflow thực tế: Prompt Engineering + Cursor

Ba workflow minh họa cách prompt tốt kết hợp với Cursor để xử lý
công việc hiệu quả.

---

**Workflow 1: Implement feature**

``` mermaid
graph TD
    A["Prompt: mô tả feature + constraint"] -->
    B["Ask: @codebase/code hiểu pattern"]
    B --> C["Prompt: implement theo pattern X, @file Y"]
    C --> D["Agent: implement"]
    D --> E["Inline Edit: sửa nhỏ nếu cần"]
```

???+ example "Ví dụ"

    Lượt 1 (Ask): *"@folder src/api/ Project tổ chức API thế nào?
    Auth ở đâu?"* → Hiểu pattern.

    Lượt 2 (Agent): *"Thêm CRUD orders: POST, GET by ID, GET list
    pagination. Follow pattern @file src/api/products/router.py.
    @file src/models/order.py. Viết test."* → Task rõ, context đủ.

    Lượt 3 (Inline Edit): select schema → ++ctrl+k++ *"thêm field
    created_at kiểu datetime"* → Sửa nhanh, không cần prompt dài.

---

**Workflow 2: Debug**

Prompt cần **context lỗi + môi trường** (WECS):

> API `/api/orders` 500 khi payload 100+ items. Error:
> `sqlalchemy.exc.OperationalError: connection timeout`.
> @file src/api/orders/router.py @file src/database.py
> Môi trường: PostgreSQL 15, pool size hiện tại 5. Cần phân tích
> nguyên nhân và đề xuất fix (ưu tiên không đổi infra nếu có thể).

Debug mode Cursor + prompt có context → AI gợi batch insert hoặc
tăng pool, có lý do rõ ràng.

---

**Workflow 3: Review / so sánh**

Role + task + format:

> Bạn là senior engineer. So sánh 2 cách implement caching trong
> @file service_a.py và @file service_b.py. Output: bảng markdown
> — Tiêu chí (performance, maintainability, edge case), Cách A,
> Cách B, Khuyến nghị.

Ask mode, không cần Agent. Prompt rõ format → output dễ đọc, dễ
dùng.

---

### 9. Anti-patterns — tránh gì?

| Anti-pattern | Hậu quả | Cách sửa |
| --- | --- | --- |
| Prompt quá chung chung | Output generic, sai context | Thêm WECS; trong Cursor thêm @ |
| Nhồi mọi thứ vào 1 prompt | AI bỏ sót, dễ lỗi | Chia multi-turn; dùng Plan rồi Agent |
| Không chỉ format | Output dài dòng, khó dùng | Nói rõ: bảng, list, JSON, độ dài |
| Quên Rules | AI không theo convention | Viết Rules 1 lần; prompt chỉ task |
| Agent khi chưa hiểu | AI sửa lung tung | Ask/Debug trước, Agent sau |

!!! warning "Nhớ"

    Prompt tốt + context sai = vẫn output kém. Trong Cursor, luôn
    đảm bảo @ đúng file/folder/codebase và Rules cập nhật.

---

### 10. Nâng cao — khi đã thuần thục

**Prompt library** — Lưu lại prompt hiệu quả cho task lặp lại:
review code, viết test, generate migration, so sánh tool. Có thể
đặt trong project (markdown) hoặc trong Cursor (Rules / notepad).
Mỗi lần output xuất sắc → save prompt đó.

**Meta-prompting** — Dùng AI để cải thiện prompt: *"Đây là prompt
tôi dùng: [paste]. Cải thiện để output chính xác hơn. Giải thích
thay đổi."* Hữu ích khi bạn mắc kẹt hoặc muốn chuẩn hóa cho team.

**Kết hợp với bài Cursor** — Prompt Engineering định nghĩa *bạn
nói gì*; Cursor định nghĩa *AI thấy gì* (context) và *AI làm gì*
(mode). Đọc thêm [Cursor — người bạn đồng hành](cursor.md) để
tối ưu context và mode; đọc [overview AI](overview.md) để gắn vào
bức tranh lớn hơn (Layer 3 + Layer 4).

---

## Kết

Prompt Engineering không phải học thuộc câu chữ — mà là **cấu
trúc hóa cách bạn giao tiếp với AI**: rõ role, context, task,
format, constraints. Từ làm quen (biết thành phần, kỹ thuật) đến
thuần thục (workflow + Cursor, tránh anti-patterns), bạn giảm
số lần "sửa lại" và tăng chất lượng output.

**Prompt Engineering + Cursor = bộ đôi xử lý công việc hiệu quả:**
bạn hỏi đúng, Cursor đưa đúng context và mode. Thiếu một bên thì
hiệu quả giảm; đủ cả hai thì công việc trôi chảy hơn rõ rệt.

!!! success "Thử ngay"

    1. Mở Cursor, chọn 1 task bạn hay làm (ví dụ: viết unit test).
    2. Viết prompt có đủ: task cụ thể + format (ví dụ: pytest, 3
       cases) + @file cần test.
    3. So sánh với lần trước bạn chỉ gõ "viết test cho file này".
    4. Lưu prompt tốt vào file hoặc Rules để dùng lại.

Sau đó đào sâu context: thêm Rules cho project, tập dùng @file /
@codebase đúng chỗ. Chi tiết context và mode xem trong bài
[Cursor — người bạn đồng hành](cursor.md).
