---
date: 2026-03-05
categories:
  - AI
tags:
  - cursor
  - ai
  - productivity
  - tools
---

# Cursor — người bạn đồng hành

Cursor có thể là người bạn đồng hành mỗi khi bạn code — nhưng
chỉ khi thực sự hiểu người bạn này. Cài xong, mở lên quen thuộc; nếu cứ
gõ tay, Google khi stuck, copy-paste từ ChatGPT thì Cursor chỉ
thành editor đắt tiền mà bạn chưa thật sự dùng đến.

Bài viết này giúp bạn **hiểu Cursor** — nó có gì, tại sao có
những thứ đó, khi nào dùng cái gì — để hai bên thật sự đồng
hành thay vì hai thế giới song song.

<!-- more -->


## Phần I — Hiểu Cursor

### 1. Tư duy chuyển đổi

Sai lầm lớn nhất khi dùng Cursor: coi nó như editor quen thuộc có
thêm chatbot. Cursor không phải plugin AI gắn vào editor — Cursor
**là** editor được thiết kế xung quanh AI.

Thay đổi quan trọng nhất không phải học phím tắt mới. Mà là thay
đổi thói quen:

| Thói quen cũ | Thói quen mới (Cursor) |
| --- | --- |
| Gõ code từ đầu | Mô tả ý định, để AI generate draft |
| Google khi không biết | Hỏi Chat với `@codebase` |
| Copy-paste từ ChatGPT | Dùng Agent sửa trực tiếp trong codebase |
| Đọc docs từ đầu đến cuối | `@docs` hoặc `@web` rồi hỏi đúng phần cần |

Nhưng trước khi thay đổi thói quen, bạn cần hiểu **bên trong
Cursor có những gì** — và tại sao nó được thiết kế như vậy.

---

### 2. Bên trong Cursor có gì

Cursor trông quen thuộc nhưng bên trong chạy một kiến trúc
khác. Mọi tính năng AI của Cursor đều xoay quanh 4 thành phần
cốt lõi:

``` mermaid
graph LR
    You["Bạn"] --> Modes
    Modes --> ContextEngine["Context Engine"]
    ContextEngine --> Models
    Rules --> ContextEngine
    Models --> Output["Code / câu trả lời"]
```

**Context Engine** — bộ máy quan trọng nhất. AI không biết gì
về project của bạn cho đến khi Context Engine cung cấp thông tin.
Khi bạn gõ `@file schema.py`, Context Engine đọc file đó và đưa
nội dung vào prompt. Khi bạn gõ `@codebase`, nó search toàn bộ
project và chọn phần liên quan nhất. Chất lượng output phụ thuộc
gần như hoàn toàn vào chất lượng context.

**Models** — bộ não xử lý. Cursor không chỉ dùng 1 model. Bạn
có thể chọn model nhanh (rẻ, phản hồi tức thì) hoặc model mạnh
(tốn hơn, suy luận sâu hơn). Chọn đúng model cho đúng task là
kỹ năng quan trọng — giống như chọn búa hay tua vít.

**Modes** — cách bạn tương tác với AI. Cursor có 4 modes khác
nhau vì mỗi tình huống cần một cách tiếp cận khác. Hỏi để hiểu
(Ask) khác hoàn toàn với giao việc để AI tự làm (Agent). Dùng
sai mode = lãng phí thời gian hoặc AI đi sai hướng.

**Rules** — bộ nhớ dài hạn. Mỗi conversation mới, AI quên hết.
Rules giải quyết vấn đề này: bạn viết convention, stack, domain
knowledge một lần — Cursor tự inject vào mọi conversation.

Bốn thành phần này phối hợp với nhau. Rules được đưa vào Context
Engine. Context Engine cung cấp thông tin cho Model. Model hoạt
động trong Mode bạn chọn. Hiểu từng thành phần sẽ giúp bạn dùng
Cursor hiệu quả hơn hẳn so với chỉ biết phím tắt.

Phần tiếp theo đi sâu vào từng thành phần.

---

### 3. Models — chọn đúng não cho đúng việc

Tại sao Cursor cho chọn model? Vì không có model nào tốt cho
mọi việc. Mỗi model có một trade-off giữa **tốc độ**, **sức
mạnh suy luận**, và **chi phí**.

**Phân loại theo mục đích:**

| Nhóm | Đặc điểm | Khi nào dùng |
| --- | --- | --- |
| **Nhanh** (cursor-small) | Phản hồi tức thì, rẻ | Autocomplete, task đơn giản |
| **Cân bằng** (claude-4-sonnet, gpt-4.1) | Đủ mạnh cho 90% công việc | Code hàng ngày, chat, agent task thông thường |
| **Mạnh** (claude-4-opus, o3) | Suy luận sâu, chậm hơn, tốn credit hơn | Architecture decision, bug phức tạp, logic rối |

**Nguyên tắc chọn model:**

- **Mặc định dùng nhóm cân bằng.** Đây là model bạn dùng 90%
  thời gian. Đủ nhanh, đủ thông minh cho hầu hết task.
- **Chuyển sang nhóm mạnh khi:** bạn cần AI suy luận nhiều
  bước (ví dụ: "redesign module này để hỗ trợ multi-tenant"),
  hoặc khi model cân bằng cho output sai/thiếu.
- **Nhóm nhanh tự chạy ở Tab autocomplete** — bạn không cần
  chọn thủ công.

**Ví dụ thực tế:**

???+ example "Cùng prompt, model khác nhau"

    Prompt: *"Refactor function này thành async,
    xử lý retry với exponential backoff"*

    **Model cân bằng:** refactor đúng, code chạy được,
    nhưng có thể bỏ sót edge case (ví dụ: max retry
    limit, jitter).

    **Model mạnh:** refactor đúng + tự thêm jitter,
    configurable max retries, proper exception chaining,
    giải thích trade-off trong comment.

    Không phải lúc nào cũng cần model mạnh.
    Nhưng khi cần, sự khác biệt rõ ràng.

**Cách đổi model:** click tên model ở góc dưới chat panel →
chọn model khác. Hoặc gõ tên model trong prompt.

!!! tip "Token economics"

    Model mạnh tốn nhiều token hơn. `@codebase` tốn
    nhiều hơn `@file`. Kết hợp model mạnh + `@codebase`
    cho một câu hỏi đơn giản = lãng phí. Dùng model
    cân bằng + `@file` cụ thể cho task nhỏ, dành model
    mạnh cho lúc thật sự cần.

---

### 4. Modes — khi nào dùng gì

Đây là phần nhiều người mới dùng Cursor bối rối nhất. Chat panel
có 4 mode: Ask, Agent, Plan, Debug. Ngoài ra còn Inline Edit
(++ctrl+k++) — không phải chat mode nhưng là cách tương tác quan
trọng. Tổng cộng **5 cách** làm việc với AI, mỗi cách cho một
mục đích khác nhau.

Nhấn bừa vào Agent vì nghe "mạnh nhất" — rồi AI sửa lung tung.
Mỗi mode tồn tại vì một lý do cụ thể. Hiểu lý do đó, bạn sẽ
chọn đúng tự nhiên.

---

**Ask** — khi bạn cần **hiểu** trước khi hành động.

Ask chỉ đọc, không sửa gì. AI phân tích code, giải thích,
tìm kiếm — nhưng không chạm vào codebase.

Dùng khi:

- Mới vào project lạ: *"@codebase giải thích architecture
  tổng quan"*
- Chưa hiểu function: *"@file utils.py giải thích
  hàm `process_batch` làm gì"*
- Cần tìm code: *"@codebase tìm tất cả nơi gọi
  `create_order`"*
- Code review: *"@file pr-changes.py review code này,
  focus security"*

Tại sao không dùng Agent luôn? Vì khi bạn chưa hiểu problem,
AI cũng không hiểu. Agent sẽ đoán và sửa — thường sai.
**Ask trước, Agent sau.**

---

**Agent** — khi bạn biết rõ mục tiêu và muốn **delegate**.

Agent là mode mạnh nhất: đọc nhiều file, sửa nhiều file, chạy
terminal commands, tự phát hiện lỗi và sửa lại. Nhưng sức mạnh
đi kèm rủi ro — Agent có thể thay đổi codebase đáng kể.

Dùng khi:

- Implement feature: *"Thêm endpoint `/api/orders` với
  pagination. Dùng FastAPI + SQLAlchemy. Viết test."*
- Refactor lớn: *"Rename `get_data` thành `fetch_orders`,
  update tất cả references trong project"*
- Viết test: *"Viết unit test cho @folder src/services/,
  dùng pytest, mock external calls"*

Tại sao không dùng Agent cho mọi thứ? Vì Agent tốn nhiều
token hơn, chạy lâu hơn, và khi scope không rõ — nó sẽ "sáng
tạo" theo cách bạn không mong muốn. Scope rõ → Agent tốt.
Scope mơ hồ → Agent nguy hiểm.

---

**Plan** — khi task phức tạp, cần **nghĩ trước khi làm**.

Plan mode để AI phân tích và đề xuất kế hoạch chi tiết trước
khi viết code. Bạn review kế hoạch, điều chỉnh, rồi mới cho
AI thực thi.

Dùng khi:

- Task lớn, nhiều bước: *"Thêm authentication bằng JWT cho
  toàn bộ API. Lên kế hoạch trước."*
- Có nhiều cách làm: *"Cần caching layer — Redis hay
  in-memory? So sánh trade-off cho project này."*
- Sợ AI đi sai hướng: Plan cho bạn cơ hội review approach
  trước khi AI bắt tay code

Tại sao cần Plan riêng? Vì với task phức tạp, nếu nhảy thẳng
vào Agent, AI có thể chọn approach sai từ đầu rồi build cả
đống code trên nền sai. Plan giúp align hướng đi trước khi
tốn effort.

---

**Debug** — khi cần **điều tra** bug có hệ thống.

Debug mode chuyên biệt cho troubleshooting: AI tạo hypothesis
về nguyên nhân, đề xuất thêm log hoặc breakpoint, phân tích
runtime info để tìm root cause.

Dùng khi:

- Bug khó reproduce: *"Function này return None ngẫu nhiên.
  Đây là log output: [paste log]"*
- Error message khó hiểu: *"Paste error + @file liên quan"*
- Performance issue: *"API endpoint này mất 5s. Phân tích
  bottleneck."*

Tại sao không dùng Ask? Ask giải thích code tĩnh. Debug kết
hợp code + runtime info (log, error, trạng thái) để suy luận
nguyên nhân. Khi bạn có error message hoặc log — Debug mode
hiệu quả hơn.

---

**Inline Edit** — khi bạn biết **chính xác chỗ cần sửa**.

Inline Edit (++ctrl+k++) không phải chat mode — nó hoạt động
ngay trong editor. Select code → mô tả thay đổi → AI sửa tại
chỗ và show diff. Nhanh, scope hẹp, 1 file.

Dùng khi:

- Sửa nhỏ, rõ ràng: *select function → "thêm error handling
  cho trường hợp input None"*
- Generate code tại chỗ: *không select → "tạo function đọc
  YAML và return dict"*
- Sinh lệnh terminal: *++ctrl+k++ trong terminal → "tìm file
  python lớn hơn 1MB"*

Tại sao không dùng Agent? Agent mở nhiều file, chạy lệnh, mất
thời gian. Inline Edit sửa ngay, không rời khỏi file đang mở.
**Sửa 1 chỗ → Inline Edit. Sửa nhiều file → Agent.**

---

**Chọn gì? Dùng flowchart này:**

``` mermaid
graph TD
    Start{"Bạn muốn gì?"} --> Q0{"Liên quan đến<br>code/project?"}
    Q0 -- Không --> Ask0["Ask mode<br>hỏi chung, brainstorm,<br>giải thích concept"]
    Q0 -- Có --> Q1{"Hiểu code hay<br>thay đổi code?"}
    Q1 -- Hiểu --> Q2{"Đang có bug/<br>error?"}
    Q2 -- Có --> Debug["Debug mode"]
    Q2 -- Không --> Ask["Ask mode"]
    Q1 -- "Thay đổi" --> Q3{"Task phức tạp,<br>nhiều cách làm?"}
    Q3 -- Có --> Plan["Plan mode"]
    Q3 -- Không --> Q4{"Sửa 1 chỗ hay<br>nhiều file?"}
    Q4 -- "1 chỗ" --> InlineEdit["Inline Edit"]
    Q4 -- "Nhiều file" --> Agent["Agent mode"]
```

**So sánh nhanh:**

| | Ask | Inline Edit | Agent | Plan | Debug |
| --- | --- | --- | --- | --- | --- |
| Brainstorm | :material-check: | :material-close: | :material-close: | :material-close: | :material-close: |
| Đọc code | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: |
| Sửa code | :material-close: | :material-check: | :material-check: | Sau approve | :material-check: |
| Multi-file | :material-close: | :material-close: | :material-check: | :material-check: | :material-check: |
| Chạy lệnh | :material-close: | :material-close: | :material-check: | :material-close: | :material-check: |
| Lên kế hoạch | :material-close: | :material-close: | :material-close: | :material-check: | :material-close: |
| Dùng runtime info | :material-close: | :material-close: | :material-close: | :material-close: | :material-check: |

---

## Phần II — Sử dụng hiệu quả

Hiểu xong kiến trúc, giờ đến cách dùng. Phần này đi từ tương
tác đơn giản nhất đến phức tạp nhất.

### 5. Ba cấp tương tác

Cursor có 3 cấp tương tác với AI, xếp theo mức độ tự chủ của
AI tăng dần — và mức độ bạn cần review cũng tăng theo.

---

**Level 1 — Tab (passive)**

AI gợi ý, bạn nhận hoặc từ chối. Không cần mở chat, không cần
gõ prompt.

- **Phím:** ++tab++ accept, ++escape++ bỏ qua,
  ++ctrl+right++ accept từng từ
- **Cách hoạt động:** khi bạn gõ code, Cursor dự đoán phần
  tiếp theo dưới dạng ghost text (chữ mờ)
- **Điểm mạnh:** Tab không chỉ complete dòng hiện tại mà
  **dự đoán edit tiếp theo** — ví dụ bạn đổi tên parameter,
  Tab gợi ý sửa tất cả usage

???+ example "Tab trong thực tế"

    Bạn vừa thêm parameter `timeout` vào function signature.
    Di chuyển xuống body → Tab gợi ý thêm `timeout` vào
    nơi gọi HTTP request. Di chuyển sang file test → Tab
    gợi ý thêm `timeout=30` vào test case.

    Bạn không cần mở Chat cho việc này. Tab đủ.

**Trust level: cao.** Tab chỉ gợi ý nhỏ, scope hẹp, dễ nhìn
thấy đúng/sai. Accept thoải mái, reject nếu sai.

---

**Level 2 — Inline Edit (active)**

Bạn chỉ đạo bằng ngôn ngữ tự nhiên, AI sửa tại chỗ và show
diff để review.

- **Phím:** ++ctrl+k++ (Linux/Windows), ++cmd+k++ (Mac)
- **Cách dùng:** select code → Ctrl/Cmd+K → mô tả thay
  đổi → review diff → accept hoặc reject
- **Không select:** Ctrl/Cmd+K → mô tả → AI generate code
  tại vị trí cursor

???+ example "Inline Edit trong thực tế"

    Select function `calculate_total`:

    > "thêm error handling: raise ValueError nếu items
    > rỗng, raise TypeError nếu item không có price"

    Cursor show diff — bạn thấy rõ chỗ nào thay đổi.
    Accept nếu đúng, reject nếu sai, sửa tay nếu gần đúng.

**Mẹo:** Inline Edit cũng hoạt động trong terminal. Nhấn
++ctrl+k++ trong terminal → mô tả lệnh bằng tiếng tự nhiên
→ Cursor sinh lệnh shell. Không cần nhớ syntax `find`, `awk`,
hay `docker`.

**Trust level: trung bình.** Scope rộng hơn Tab nhưng giới hạn
trong 1 file. Luôn đọc diff trước khi accept.

---

**Level 3 — Agent (autonomous)**

Bạn mô tả mục tiêu, AI tự lên kế hoạch và thực thi nhiều bước.

- **Phím:** ++ctrl+l++ mở chat → chọn Agent mode
- **Cách dùng:** mô tả task → AI tự đọc file, sửa file, chạy
  lệnh, phát hiện lỗi, sửa lại
- **Checkpoint:** Cursor tự tạo checkpoint mỗi bước. Nếu AI
  đi sai, bạn revert về bước trước mà không cần git.

???+ example "Agent trong thực tế"

    > "Thêm endpoint POST /api/orders. Validate input bằng
    > Pydantic. Lưu vào PostgreSQL qua SQLAlchemy. Return
    > 201 với order ID. Viết 3 test cases. @file models.py
    > @file database.py"

    Agent sẽ: đọc models.py và database.py → tạo endpoint
    → tạo Pydantic schema → viết test → chạy test →
    sửa nếu fail.

**Trust level: thấp nhất — cần review kỹ.** Agent thay đổi
nhiều file cùng lúc. Luôn commit trước khi chạy Agent. Đọc
diff của từng file trước khi accept. Nếu không hiểu chỗ nào
AI sửa — dùng Ask hỏi trước khi accept.

---

**Trust gradient tóm tắt:**

```
Tab ────── Inline Edit ────── Agent
 ↑              ↑                ↑
Tin nhiều    Đọc diff        Review kỹ
Rủi ro thấp  Scope 1 file   Scope nhiều file
```

!!! tip "Quy tắc chọn cấp"

    Luôn dùng cấp **thấp nhất** đủ cho task.
    Tab đủ? Dùng Tab. Sửa 1 chỗ? Inline Edit.
    Chỉ dùng Agent khi thật sự cần multi-file/multi-step.

---

### 6. Context — kỹ năng quyết định chất lượng output

Context Engine là trái tim của Cursor. AI chỉ biết những gì
bạn cho nó biết. Cùng một câu hỏi, người cung cấp context
tốt nhận output tốt hơn gấp nhiều lần.

**Context tự động (auto-context):**

Cursor tự inject một số context mà bạn không cần làm gì:

- File đang mở và đang focus
- Vị trí cursor trong file
- Đoạn code đang select
- Conversation history (các tin nhắn trước đó)

Đây là lý do tại sao khi bạn đặt cursor vào một function rồi
nhấn Ctrl+L, AI đã biết function đó — dù bạn chưa `@` gì.

**Context thủ công (@ mentions):**

| Syntax | Tác dụng | Khi nào dùng |
| --- | --- | --- |
| `@file tên-file` | Đưa nội dung file vào context | Biết chính xác file liên quan |
| `@folder tên-folder` | Đưa cả folder | Task liên quan cả module |
| `@codebase` | Semantic search toàn project | Không biết code nằm đâu |
| `@web "query"` | Tìm trên internet | Cần info bên ngoài project |
| `@docs tên-docs` | Reference docs đã index | Cần đối chiếu docs chính thức |
| `@git` | Lịch sử thay đổi | Debug regression, hiểu history |
| `@notepad tên` | Reference notepad | Context tái sử dụng |
| Kéo thả / paste ảnh | Screenshot vào chat | Debug UI, giải thích diagram |

**Chiến lược: bắt đầu hẹp, mở rộng khi cần.**

```
@file cụ thể
  ↓ không đủ?
@file + @file (thêm file liên quan)
  ↓ không đủ?
@folder
  ↓ không biết ở đâu?
@codebase
```

Tại sao không `@codebase` mọi lúc? Vì context window có giới
hạn. Mỗi token bạn nhét vào context = bớt chỗ cho AI suy luận.
`@codebase` trên project lớn sẽ lấy nhiều file nhưng mỗi file
chỉ lấy snippet ngắn — context bị loãng. `@file` cụ thể cho
AI thấy toàn bộ file, context đặc hơn, output chính xác hơn.

**Sai lầm phổ biến:**

- Không dùng `@` gì → AI đoán mù, output generic
- `@codebase` cho mọi thứ → tốn token, context loãng, chậm
- Quên `@web` khi hỏi về library mới → AI hallucinate API cũ
- Conversation quá dài mà không new chat → history cũ chiếm
  hết context window, câu hỏi mới bị ảnh hưởng

!!! tip "Khi nào nên tạo chat mới"

    Khi topic thay đổi hoàn toàn, hoặc conversation đã dài
    (20+ messages) — hãy tạo chat mới. Conversation history
    chiếm context window. Chat mới = context sạch.

---

### 7. Rules — bộ nhớ dài hạn

Mỗi conversation mới, AI quên hết. Bạn đã nói "dùng Python
3.12" 50 lần nhưng conversation thứ 51, AI vẫn không biết.

Rules giải quyết vấn đề này. Rules là file markdown nằm trong
project, Cursor tự inject vào mọi conversation — như system
prompt riêng cho project của bạn.

**Tạo Rules:**

File `.cursor/rules/*.md` trong project. Ví dụ:

```markdown
# Project rules

- Stack: Python 3.12, FastAPI, PostgreSQL
- Viết code theo Google Python Style Guide
- Prefer composition over inheritance
- Error handling: luôn dùng custom exception classes
- Test: pytest, mock external services
```

**4 loại Rules:**

| Loại | Khi nào apply | Ví dụ |
| --- | --- | --- |
| Always | Mọi conversation | Stack, ngôn ngữ, convention chung |
| Auto-attached | File matching glob pattern | SQL rules cho `*.sql` |
| Agent-requested | AI tự kéo vào khi thấy liên quan | API design rules |
| Manual | User gõ `@rule-name` | Rules chuyên biệt, ít dùng |

Auto-attached rule khai báo glob trong frontmatter:

```markdown
---
globs: ["**/*.sql"]
---

- Dùng explicit column names, không SELECT *
- Luôn có WHERE clause khi UPDATE/DELETE
- Tên bảng số ít, snake_case
```

**Tổ chức rules cho project thực tế:**

```
.cursor/rules/
├── general.md        ← Always: stack, ngôn ngữ, convention
├── python.md         ← Auto-attached: **/*.py
├── sql.md            ← Auto-attached: **/*.sql
├── api-design.md     ← Agent-requested: REST conventions
└── testing.md        ← Auto-attached: **/test_*.py
```

Mỗi file một concern, giữ ngắn (dưới 50 dòng). Rules dài =
AI bỏ qua phần cuối vì context bị loãng.

**Rules tốt cần gì:**

| Nên có | Không cần |
| --- | --- |
| Stack và version cụ thể | "Hãy viết code tốt" (quá chung) |
| Convention của project | Lặp lại docs chính thức |
| Những lỗi AI hay mắc | Hướng dẫn dài 500 dòng |
| Domain knowledge cụ thể | Lý thuyết về cách AI hoạt động |

!!! tip "Feedback loop"

    Khi AI lặp lại cùng lỗi 2-3 lần → thêm vào Rules.
    Khi output AI cải thiện → rules đang hiệu quả.
    Rules không phải viết 1 lần xong — nó là living document,
    cập nhật liên tục theo kinh nghiệm làm việc với AI.

---

## Phần III — Thuần thục

### 8. Workflow thực tế

Biết từng thành phần rồi, cách kết hợp chúng trong 1 ngày
làm việc mới là phần quan trọng. Dưới đây là các workflow
phổ biến nhất, mỗi workflow có tình huống, prompt thực tế, và
kết quả mong đợi.

---

**Workflow 1: Implement feature mới**

``` mermaid
graph TD
    A["Đọc requirement"] -->
    B["Ask: hỏi codebase để hiểu context"]
    B --> C{"Hiểu rõ chưa?"}
    C -- Chưa --> D["Ask thêm với @file cụ thể"]
    D --> C
    C -- Rồi --> E{"Task phức tạp?"}
    E -- Có --> F["Plan: lên kế hoạch"]
    F --> G["Review plan, điều chỉnh"]
    G --> H["Agent: implement"]
    E -- Không --> H
    H --> I["Review diff"]
    I --> J{"OK?"}
    J -- "Sửa nhỏ" --> K["Inline Edit chỗ cụ thể"]
    K --> J
    J -- OK --> L["Commit"]
```

???+ example "Demo: thêm endpoint mới"

    **Bước 1 — Ask (hiểu context):**

    > `@folder src/api/` "Project này tổ chức API
    > endpoints theo pattern nào? Authentication
    > middleware ở đâu?"

    AI trả lời: dùng FastAPI router, auth middleware
    ở `src/middleware/auth.py`, mỗi domain có folder riêng.

    **Bước 2 — Agent (implement):**

    > "Thêm CRUD endpoints cho orders: POST, GET by ID,
    > GET list với pagination. Follow pattern giống
    > @file src/api/products/router.py. Thêm test.
    > @file src/models/order.py"

    Agent tạo router, schema, test — follow đúng pattern.

    **Bước 3 — Inline Edit (polish):**

    Select response schema → ++ctrl+k++:
    *"thêm field `created_at` với type datetime"*

---

**Workflow 2: Debug**

???+ example "Demo: fix API error"

    **Bước 1 — Debug mode:**

    > "API endpoint `/api/orders` trả về 500 khi gọi
    > với payload lớn (100+ items). Error log:
    > `sqlalchemy.exc.OperationalError: connection timeout`
    > @file src/api/orders/router.py
    > @file src/database.py"

    AI phân tích: connection pool quá nhỏ cho bulk insert,
    đề xuất tăng pool size hoặc dùng batch insert.

    **Bước 2 — Agent (fix):**

    > "Implement batch insert cho orders endpoint.
    > Chunk thành batch 50 items. Dùng
    > `session.bulk_save_objects`."

---

**Workflow 3: Code review**

???+ example "Demo: review PR"

    Ask mode:

    > `@file src/services/payment.py`
    > `@file src/services/order.py`
    > "Review 2 file này. Focus: error handling,
    > race condition, và có đúng convention
    > của project không."

    AI chỉ ra: payment service không retry khi
    gateway timeout, order service thiếu lock khi
    update concurrent orders.

---

**Workflow 4: Viết docs / SQL / config**

???+ example "Demo: generate migration SQL"

    > `@file src/models/order.py` "Generate SQL migration
    > để tạo bảng orders trong PostgreSQL. Follow
    > convention trong @file migrations/001_products.sql"

    AI sinh SQL migration matching pattern hiện có.
    Review → Inline Edit nếu cần sửa nhỏ.

---

### 9. Anti-patterns — những sai lầm phổ biến

Cursor mạnh, nhưng dùng sai thì mất thời gian hơn cả không
dùng. Dưới đây là những anti-pattern phổ biến nhất:

**Agent khi chưa hiểu problem.**
Bạn gặp bug, nhảy thẳng vào Agent bảo "fix bug này". AI đoán
nguyên nhân, sửa lung tung, tạo thêm bug mới. → **Ask/Debug
trước để hiểu root cause, Agent sau để fix.**

**Không dùng @ context.**
Hỏi "tạo API endpoint" mà không `@file` model hay router hiện
có. AI viết code generic, không follow convention project.
→ **Luôn @ ít nhất 1 file liên quan.**

**Accept All không đọc diff.**
Agent sửa 10 file, bạn Accept All trong 2 giây. 2 ngày sau
phát hiện AI xóa mất error handling ở file thứ 7.
→ **Đọc diff từng file. Không hiểu chỗ nào → Ask ngay
trước khi accept.**

**Không commit trước Agent.**
Agent refactor lớn, kết quả sai, bạn muốn undo nhưng đã
accept hết. → **`git commit` trước mỗi Agent task lớn.
Agent có checkpoint, nhưng git là lưới an toàn cuối cùng.**

**Conversation quá dài.**
Chat 30+ messages, AI bắt đầu "quên" context đầu, output
kém đi. → **New chat khi topic thay đổi hoặc conversation
quá dài. Mỗi chat nên focus 1 task.**

**Dùng model mạnh cho mọi thứ.**
Hỏi "đổi tên biến" bằng claude-4-opus. Tốn credit, chờ lâu,
kết quả giống hệt model nhanh. → **Mặc định dùng model cân
bằng. Chỉ upgrade khi cần suy luận phức tạp.**

---

### 10. Nâng cao — tìm hiểu khi đã thuần thục

Những tính năng sau không cần thiết ngay, nhưng sẽ mở rộng
khả năng khi bạn đã quen với phần core:

**MCP (Model Context Protocol)** — kết nối Cursor với external
tools: database (AI query trực tiếp khi debug), browser (AI
test UI), API docs. MCP biến Cursor từ code editor thành
workstation tích hợp.

**Background Agents** — giao task dài cho Agent chạy trên cloud
trong khi bạn làm việc khác. Phù hợp cho task độc lập kiểu
"viết test coverage cho toàn bộ module X".

**Notepads** — lưu context tái sử dụng mà không cần nằm trong
codebase. Ví dụ: schema database tóm tắt, architecture notes,
API contract. Reference bằng `@notepad` trong bất kỳ chat nào.

**Custom models** — kết nối model riêng qua API key (OpenAI,
Anthropic, local models). Hữu ích nếu công ty có model nội bộ
hoặc bạn cần model chuyên biệt cho domain cụ thể.

---

## Kết

Cursor không khó. Khó là bỏ thói quen cũ.

Bạn không cần nhớ hết mọi tính năng. Chỉ cần nhớ framework:

1. **Hiểu trước, làm sau** — Ask/Debug trước, Agent sau
2. **Context quyết định chất lượng** — luôn `@` trước khi hỏi
3. **Dùng cấp thấp nhất đủ cho task** — Tab > Inline Edit >
   Agent
4. **Rules là bộ nhớ dài hạn** — AI mắc lỗi → cập nhật Rules
5. **Commit trước Agent** — git là lưới an toàn cuối cùng

Prompt bạn viết quyết định chất lượng không kém context. Kết hợp
với [Prompt Engineering — từ làm quen đến thuần thục](prompt-engineering.md)
để thành bộ đôi xử lý công việc hiệu quả.

**Thử ngay:** mở project bạn đang làm, tạo file
`.cursor/rules/general.md` với 5 dòng mô tả stack + convention.
Mở Chat ở Ask mode, gõ `@codebase` *"giải thích architecture
của project này"*. So sánh output trước và sau khi có Rules —
bạn sẽ thấy sự khác biệt ngay.

Phần còn lại sẽ đến tự nhiên khi bạn dùng mỗi ngày. Giống
như bài [Học nhanh. Nhớ lâu.](../level-up/hoc-nhanh-nho-lau.md)
nói: học bằng cách làm, không phải bằng cách đọc về nó. Mở
Cursor lên và bắt đầu thay đổi thói quen — từ hôm nay.
