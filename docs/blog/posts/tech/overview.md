---
date: 2026-03-05
categories:
  - Tech
tags:
  - dataops
  - data-engineering
  - kubernetes
  - databases
  - infrastructure
---

# DataOps mindset — tại sao Data Engineer cần nghĩ như SRE

Bạn biết viết Airflow DAG.
Bạn biết query PostgreSQL.
Bạn biết deploy lên Kubernetes.

Nhưng khi pipeline fail lúc 3h sáng,
khi data drift không ai phát hiện đến khi CEO hỏi,
khi migration chạy 6 tiếng rồi fail giữa chừng —
bạn nhận ra:
**biết dùng tool không đủ.
Cần một mindset khác.**

DataOps là mindset đó.

Bài viết này là bài mở đầu cho series Tech —
từ triết lý DataOps
đến thực hành cụ thể với Kubernetes, Databases,
và infrastructure cho data.

<!-- more -->

!!! abstract "Bản đồ bài viết"

    | Phần | Chủ đề |
    | :---: | --- |
    | **1** | DataOps là gì — và không phải là gì |
    | **2** | Data Engineer vs SRE — điểm giao nhau |
    | **3** | 5 trụ cột của DataOps |
    | **4** | Tooling: phương tiện, không phải mục đích |
    | **5** | Bắt đầu từ đâu |

## 1. DataOps là gì — và không phải là gì

**DataOps = DevOps applied to data.**

Nhưng nói vậy thì quá đơn giản.
Cụ thể hơn:

DataOps là tập hợp practices, tools và culture
nhằm **rút ngắn cycle time**
từ raw data đến business insight —
với chất lượng cao, lặp lại được,
và không phụ thuộc vào một người duy nhất.

**DataOps KHÔNG phải:**

- Một tool cụ thể
  (không phải "mua Airflow là có DataOps")
- Data Engineering + buzzword
  (không phải gắn "Ops" vào là xong)
- Chỉ dành cho team lớn
  (team 1-3 người cũng cần,
  thậm chí cần hơn vì không có ai backup)

**DataOps LÀ:**

- Automation cho mọi thứ lặp lại
- Monitoring cho mọi thứ có thể sai
- Version control cho mọi thứ thay đổi
- Testing cho mọi thứ quan trọng

``` mermaid
graph LR
    subgraph old ["Truoc DataOps"]
        A1["Code pipeline"] --> A2["Deploy thu cong"]
        A2 --> A3["Cau troi khong loi"]
    end
    subgraph new_ops ["Voi DataOps"]
        B1["Code pipeline"] --> B2["CI/CD test"]
        B2 --> B3["Auto deploy"]
        B3 --> B4["Monitor + Alert"]
        B4 --> B5["Feedback loop"]
        B5 --> B1
    end
```

## 2. Data Engineer vs SRE — điểm giao nhau

SRE (Site Reliability Engineering) đã giải quyết
vấn đề reliability cho web services
từ hơn 15 năm trước.
Data Engineering đang ở giai đoạn tương tự —
và có thể học rất nhiều.

| Concept SRE | Áp dụng cho Data |
| --- | --- |
| **SLO/SLI** | Data freshness SLO: "dashboard update trong 15 phút" |
| **Error budget** | Pipeline fail 2%/tháng là acceptable |
| **Toil reduction** | Tự động hóa manual data fix |
| **Incident response** | Runbook khi pipeline fail |
| **Observability** | Data lineage + quality metrics |

!!! tip "Nghĩ như SRE"

    SRE không cố làm system không bao giờ fail.
    SRE thiết kế system **fail gracefully** —
    phát hiện nhanh, recover nhanh, học từ failure.
    Data Engineer cần cùng mindset:
    pipeline sẽ fail.
    Câu hỏi là bạn biết khi nào
    và recovery mất bao lâu.

## 3. Năm trụ cột của DataOps

### 3.1 Version Control — mọi thứ phải tracked

Không chỉ code.
Schema changes, DAG configs,
infrastructure as code, data contracts —
tất cả phải nằm trong Git.

**Tại sao**: khi có vấn đề,
bạn cần biết **ai thay đổi gì, khi nào, tại sao**.
Không có version control =
không có accountability = không debug được.

### 3.2 CI/CD — deploy phải tự động và an toàn

Pipeline code phải qua:

1. **Lint + format** — code nhất quán
2. **Unit test** — logic đúng
3. **Integration test** — kết nối đúng
4. **Staging deploy** — chạy thử trước
5. **Production deploy** — automated, có rollback

Manual deploy = manual error.
"Tôi chạy tay trên production" là câu nói
dẫn đến incident.

### 3.3 Data Quality — test data, không chỉ test code

Code đúng không có nghĩa data đúng.

| Loại test | Kiểm tra gì | Tool gợi ý |
| --- | --- | --- |
| **Schema** | Cột có đúng type không | dbt test, Great Expectations |
| **Freshness** | Data có mới không | dbt source freshness |
| **Volume** | Row count bất thường không | Custom alerts |
| **Distribution** | Giá trị có shift không | Statistical checks |
| **Uniqueness** | Primary key có duplicate không | SQL constraints |

### 3.4 Observability — biết chuyện gì đang xảy ra

Ba tầng observability cho data:

- **Pipeline health** —
  DAG status, task duration, failure rate
- **Data health** —
  freshness, quality score, anomaly detection
- **Business impact** —
  dashboard nào đang dùng data cũ,
  report nào sai vì data quality

Monitoring mà không ai xem = không có monitoring.
Alert mà alert mỗi ngày = noise, không phải signal.

### 3.5 Collaboration — không ai là siêu nhân

DataOps giỏi nhất cũng vô nghĩa
nếu chỉ một người biết:

- **Documentation** — runbook, architecture diagram,
  data dictionary phải có và phải cập nhật
- **Data contracts** —
  producer và consumer thống nhất schema trước
- **On-call rotation** — không phải một người
  sửa mọi thứ mọi lúc
- **Post-mortem** — khi fail, học từ đó,
  không blame

## 4. Tooling: phương tiện, không phải mục đích

Category Tech trong blog này sẽ bàn sâu
về Kubernetes, Databases, và các tools cụ thể.
Nhưng luôn nhớ:

| Tool | Vai trò | Không phải |
| --- | --- | --- |
| **Kubernetes** | Platform chạy workload | Mục tiêu cần chinh phục |
| **PostgreSQL** | Lưu trữ data | Tool duy nhất cần biết |
| **Airflow/Dagster** | Orchestrate pipelines | Giải pháp cho mọi vấn đề |
| **dbt** | Transform data | Thay thế SQL thuần |
| **Terraform** | Infrastructure as Code | Cần cho mọi project |

**Nguyên tắc chọn tool:**

1. **Bài toán trước, tool sau** —
   hiểu rõ vấn đề rồi mới chọn giải pháp
2. **Boring technology** —
   tool đã chứng minh > tool mới hấp dẫn
3. **Team capability** —
   tool mà team không vận hành được = liability
4. **Escape hatch** —
   luôn có plan B khi tool không phù hợp nữa

!!! warning "Bẫy phổ biến"

    "Chúng ta cần Kubernetes"
    thường là triệu chứng của
    "chúng ta chưa hiểu vấn đề thật sự là gì."
    K8s giải quyết orchestration ở scale.
    Nếu bạn có 3 services,
    docker compose có thể là đủ.

## 5. Bắt đầu từ đâu

Nếu bạn là Data Engineer
muốn áp dụng DataOps mindset, bắt đầu từ:

**Tuần 1-2: Foundation**

- [ ] Mọi code trong Git
  (kể cả SQL, DAG config, schema)
- [ ] CI chạy lint + basic test cho mỗi PR
- [ ] Có ít nhất 1 data quality check
  cho pipeline quan trọng nhất

**Tháng 1: Automation**

- [ ] CD tự động deploy đến staging
- [ ] Alert khi pipeline fail
  (Slack/email, không phải check dashboard thủ công)
- [ ] Runbook cho top 3 incidents phổ biến nhất

**Tháng 2-3: Observability**

- [ ] Dashboard hiển thị pipeline health
- [ ] Data freshness monitoring
- [ ] SLO cho ít nhất 1 data product quan trọng

**Ongoing: Culture**

- [ ] Post-mortem cho mỗi incident lớn
- [ ] Documentation as habit
  (viết cùng lúc build, không phải sau)
- [ ] Share knowledge — blog, demo, pair programming

---

## Kết

DataOps không phải destination.
DataOps là **cách bạn vận hành hàng ngày**.

Giống như bài
[Học nhanh. Nhớ lâu.](../level-up/hoc-nhanh-nho-lau.md)
nói về cách xây hệ thống tư duy cá nhân,
DataOps là cách xây hệ thống vận hành dữ liệu —
cả hai đều cần discipline, feedback loop,
và sự kiên nhẫn để làm đúng thay vì làm nhanh.

Những bài tiếp theo trong series Tech
sẽ đi sâu vào từng mảnh:
Kubernetes cho Data Engineer,
PostgreSQL internals,
CI/CD cho data pipelines,
và nhiều how-to thực hành khác.

**Tool thay đổi mỗi năm.
Mindset tồn tại cả career.**
