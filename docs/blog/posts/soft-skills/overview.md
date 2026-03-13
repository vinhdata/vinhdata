---
date: 2026-03-04
categories:
  - Soft Skills
tags:
  - soft-skills
  - career
  - communication
  - leadership
---

# Kỹ năng mềm mà senior engineer không thể thiếu

Hard skills đưa bạn vào phòng. Soft skills giữ bạn ở lại.

Hầu hết lộ trình phát triển của kỹ sư đều xoay quanh kỹ năng kỹ thuật — ngôn ngữ mới, framework mới, hệ thống mới. Nhưng đến một lúc, bạn nhận ra: người được thăng tiến không phải người code giỏi nhất, mà là người **có impact lớn nhất**. Và impact ở level senior không đến từ số dòng code — nó đến từ khả năng giao tiếp, ảnh hưởng, và định hình bài toán.

Bài viết này bàn về những kỹ năng "mềm" mà thực ra rất "cứng" — vì thiếu chúng, bạn sẽ mãi là người thực thi giỏi nhưng không ai nghe.

<!-- more -->

## 1. Technical writing — thuyết phục bằng văn bản

Trong môi trường remote, phần lớn ảnh hưởng của bạn đến từ chữ viết. Bạn không "nói" trong cuộc họp 30 phút — bạn viết ADR, RFC, proposal, incident report mà hàng chục người đọc trong nhiều tháng.

**Viết tốt = nghĩ rõ.** Nếu bạn không viết ra được lý do chọn giải pháp A thay vì B, có thể bạn chưa thực sự hiểu trade-off.

Những thứ senior engineer cần viết tốt:

* **ADR (Architecture Decision Record)** — ghi lại quyết định thiết kế: context, options considered, decision, consequences. Đây là cách bạn "nói chuyện" với người đọc 6 tháng sau — bao gồm cả chính bạn.
* **RFC / Design doc** — đề xuất thay đổi lớn. Mục tiêu: người đọc hiểu vấn đề, hiểu giải pháp, và hiểu tại sao bạn chọn cách này.
* **Incident report / Postmortem** — phân tích sự cố. Không phải "blame" — mà là "hệ thống nào cho phép lỗi này xảy ra, và cách ngăn nó lặp lại".
* **Runbook** — hướng dẫn vận hành. Viết cho người 3h sáng mắt nhắm mắt mở cần xử lý sự cố.

Cách luyện: mỗi quyết định thiết kế quan trọng, viết 1 đoạn ngắn giải thích "tại sao". Không cần formal ADR — chỉ cần viết ra. Dần dần nó trở thành thói quen.

---

## 2. Stakeholder communication — nói cho người không kỹ thuật hiểu

Bạn biết pipeline bị chậm vì partition skew trên BigQuery. Product manager chỉ biết "dữ liệu sáng nay chưa có". Khoảng cách đó — giữa hiểu biết kỹ thuật và ngôn ngữ business — là kỹ năng bạn cần lấp.

**Nguyên tắc:**

* **Bắt đầu từ impact, không phải nguyên nhân.** "Dashboard sáng nay sẽ delay 2 tiếng" trước, rồi mới giải thích tại sao.
* **Dùng phép so sánh.** "Schema migration giống như sửa móng nhà — phải đóng cửa tạm thời, nhưng sau đó vững hơn."
* **Đưa ra options, không chỉ vấn đề.** "Có 2 cách xử lý: A mất 1 ngày nhưng tạm thời, B mất 1 tuần nhưng triệt để. Bạn muốn ưu tiên cái nào?"
* **Quản lý kỳ vọng sớm.** Nói "có thể delay" vào thứ 2 tốt hơn nói "delay rồi" vào thứ 6.

Với Data Engineer, điều này đặc biệt quan trọng khi:

* Giải thích data quality issues cho business — "dữ liệu không sai, nhưng definition thay đổi"
* Advocate cho infrastructure investment — "đầu tư 2 tuần bây giờ tiết kiệm 2 giờ mỗi ngày sau này"
* Nói "không" với request không hợp lý — không phải "không làm được" mà là "đây là trade-off"

---

## 3. Problem framing — hỏi đúng câu trước khi giải

Kỹ năng quan trọng nhất mà ít ai dạy: **không phải giải bài toán, mà là hỏi "đây có phải bài toán đúng không?"**

Ví dụ:

* Team muốn "tối ưu pipeline cho nhanh hơn". Nhưng vấn đề thật có thể là: dữ liệu không cần real-time — chỉ cần chạy sớm hơn 1 tiếng buổi sáng.
* Stakeholder muốn "thêm 20 cột vào dashboard". Nhưng câu hỏi đúng là: "quyết định nào cần dữ liệu này để đưa ra?"
* Manager muốn "migrate sang tool X". Nhưng vấn đề thật có thể là: tool hiện tại thiếu monitoring, không phải thiếu tính năng.

**Cách luyện problem framing:**

* Trước khi nhảy vào code, dành 15 phút viết: "Vấn đề thực sự là gì? Ai bị ảnh hưởng? Nếu không làm gì, chuyện gì xảy ra?"
* Hỏi ngược: "Kết quả mong đợi là gì?" thay vì "Bạn muốn tôi làm gì?"
* Tìm root cause: dùng "5 Whys" — hỏi "tại sao" 5 lần liên tiếp để đào sâu hơn triệu chứng bề mặt.

Senior engineer được trả tiền để giải đúng bài toán, không phải giải nhanh bài toán sai.

---

## 4. Estimation & planning — sai ở đây = mất trust

Không ai kỳ vọng estimate chính xác 100%. Nhưng sai lệch liên tục — nói 1 tuần thành 1 tháng — sẽ mất trust nhanh hơn bất kỳ bug nào.

**Tại sao kỹ sư thường estimate sai:**

* **Chỉ tính happy path** — quên edge cases, testing, documentation, code review, deployment
* **Quên context switching** — 5 ngày coding ≠ 5 ngày calendar khi còn họp, ad-hoc, trả lời tin nhắn
* **Anchoring bias** — bị neo vào con số đầu tiên nghĩ ra, không điều chỉnh

**Cách estimate tốt hơn:**

* **Phân tách nhỏ** — estimate từng phần thay vì cả cục. "Build API: 2 ngày. Viết test: 1 ngày. Documentation: 0.5 ngày. Buffer: 1 ngày. Tổng: 4.5 ngày" chính xác hơn "khoảng 1 tuần".
* **Nhân đôi rồi thêm buffer** — nếu gut feeling nói 3 ngày, estimate 5-7 ngày. Bạn sẽ đúng hơn là sai.
* **Communicate uncertainty** — "Tôi estimate 1 tuần, nhưng nếu gặp vấn đề Y thì có thể 2 tuần. Tôi sẽ update vào thứ 4." Transparency > precision.
* **Track lại** — ghi estimate vs actual. Sau 3-6 tháng, bạn sẽ biết mình thường sai theo hướng nào.

---

## 5. Influence without authority — ảnh hưởng mà không cần quyền lực

Senior engineer hiếm khi có quyền ra lệnh. Bạn không phải manager. Nhưng bạn cần đẩy technical decision — chọn tool, chọn architecture, chọn approach. Làm thế nào?

**Dùng data, không dùng ý kiến.** "Tôi nghĩ tool A tốt hơn" yếu hơn "Tôi đã benchmark: tool A xử lý 10x throughput với 50% cost so với tool B. Đây là kết quả."

**Dùng prototype.** Thay vì tranh luận 3 buổi họp, build một POC trong 2 ngày. Demo nói to hơn slide.

**Dùng narrative.** Kể câu chuyện: "Tháng trước team X gặp vấn đề Y vì dùng approach Z. Chúng ta đang đi cùng hướng. Đây là cách tránh." Story > data > opinion.

**Chọn trận đánh.** Không phải mọi quyết định đều đáng tranh. Nếu impact nhỏ, let it go. Dành energy cho quyết định ảnh hưởng 6-12 tháng tới.

**Build trust trước khi cần nó.** Khi bạn có track record deliver tốt, ý kiến của bạn tự nhiên có trọng lượng. Trust không đến từ title — đến từ lịch sử hành động.

---

## 6. Mentoring — nhân đôi impact

Bạn code giỏi = impact 1x. Bạn giúp 3 người code giỏi hơn = impact 4x.

**Code review là cơ hội mentoring lớn nhất:**

* Đừng chỉ "LGTM" hoặc "fix lỗi này". Giải thích *tại sao*: "Cách này hoạt động, nhưng sẽ gặp vấn đề khi scale vì X. Thử approach Y xem."
* Hỏi thay vì chỉ: "Bạn đã cân nhắc cách nào khác chưa?" buộc người được review phải suy nghĩ sâu hơn.
* Share context: "Mình từng gặp case tương tự ở project Z, kết quả là..."

**Mentoring không cần formal:**

* Pair programming 30 phút/tuần với junior
* Chia sẻ bài viết/resource hay khi thấy người khác đang stuck ở chủ đề đó
* Viết nội bộ: "lessons learned" sau mỗi project lớn

Mentoring cũng là cách học tốt nhất cho chính bạn — đúng Feynman Technique: nếu bạn không giải thích được, bạn chưa hiểu.

---

## 7. Lộ trình luyện soft skills

Soft skills không học bằng đọc sách — học bằng thực hành có chủ đích. Cách tích hợp vào lịch trình hiện tại:

| Kỹ năng | Cách luyện hàng tuần | Tích hợp ở đâu |
| --- | --- | --- |
| Technical writing | Viết 1 ADR hoặc ghi chú thiết kế cho mỗi quyết định quan trọng | Block 2 buổi sáng hoặc core hours |
| Stakeholder comm | Mỗi khi report issue, viết 2 version: 1 kỹ thuật, 1 cho business | Core hours |
| Problem framing | Trước khi code, viết 3 câu: vấn đề là gì, ai bị ảnh hưởng, nếu không làm thì sao | Block 1 hoặc đầu core hours |
| Estimation | Ghi estimate vs actual cho mỗi task, review mỗi tháng | Weekly review |
| Influence | Mỗi technical decision lớn, chuẩn bị 1 trang data/prototype trước khi họp | Core hours |
| Mentoring | 1 code review sâu/tuần (giải thích "tại sao", không chỉ "fix gì") | Core hours |

Không cần thêm giờ. Chỉ cần thay đổi **cách** bạn làm những việc đang làm.

---

## 8. Kết luận

Hard skills có ceiling — đến một lúc, code giỏi thêm 10% không thay đổi career của bạn. Soft skills không có ceiling — và chúng compound theo thời gian.

Senior engineer không phải người biết nhiều nhất. Là người **tạo impact lớn nhất** — qua việc giao tiếp rõ ràng, framing đúng vấn đề, ảnh hưởng quyết định, và nhân đôi năng lực team.

Tin tốt: soft skills luyện được, giống như hard skills. Chỉ cần thực hành có chủ đích, mỗi tuần một chút, tích lũy theo thời gian.

**Viết rõ hơn. Hỏi đúng hơn. Ảnh hưởng nhiều hơn. Và nhớ: người được nghe không phải người nói to nhất — mà là người được tin tưởng nhất.**
