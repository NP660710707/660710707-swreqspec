# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v3 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-12 13:02 +00:00 | test: 1 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | ไม่มี AC | T-04, T-05, T-06 | backend/app/main.py: app; frontend/src/App.jsx: App; frontend/src/api/client.js: api.getSlots | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| FR-BKG-02 | AC-BKG-02 | T-09, T-10 | backend/app/main.py: app; frontend/src/App.jsx: App | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-11, T-12 | backend/app/main.py: app; frontend/src/App.jsx: App | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-07, T-08, T-20 | backend/app/main.py: app; frontend/src/App.jsx: App; frontend/src/api/client.js: api.createBooking | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| FR-BKG-05 | AC-BKG-04 | T-13, T-14 | backend/app/main.py: app; frontend/src/App.jsx: App | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-04, T-05, T-06 | backend/app/main.py: app; frontend/src/App.jsx: App; frontend/src/api/client.js: api.getSlots | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| NFR-PERF-01 | AC-BKG-05 | T-04, T-06, T-18, T-19 | backend/app/main.py: app; frontend/src/App.jsx: App | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| NFR-SEC-01 | ไม่มี AC | T-03 | backend/app/main.py: app | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-13, T-14 | backend/app/main.py: app | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | T-20 | frontend/src/App.jsx: App | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01, T-02 | backend/app/config.py: (ค่าสถานะกลาง); backend/app/main.py: app | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| DOM-PDPA-01 | AC-BKG-06 | T-15, T-16 | backend/app/main.py: app; frontend/src/App.jsx: App | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC | T-03 | backend/app/main.py: app | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| IF-HIS-01 | ไม่มี AC | T-02, T-03 | backend/app/main.py: app | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |
| IF-NOT-01 | ไม่มี AC | T-13, T-14 | backend/app/main.py: app | pytest: 0 collected; Vitest: 1 passed (setup only) | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/main.py: app | FR-BKG-01..06, IF-IDP-01, IF-NOT-01, DOM-PDPA-01 | ไม่ | เป็น FastAPI skeleton ที่สร้าง app และ include router แต่ไม่มี router/logic ที่ปฏิบัติการจอง หรือบันทึก audit log และไม่มีการยืนยันตัวตน/ส่งข้อความ |
| frontend/src/App.jsx: App | UI-BKG-01, UI-BKG-02, UI-BKG-03, FR-BKG-01..06 | ไม่ | เป็นข้อความตัวอย่างอย่างง่าย "ระบบจองคิวตรวจสุขภาพ" เท่านั้น ไม่มี UI เลือกแพ็กเกจ/ช่วงเวลา/ยืนยัน/ผลลัพธ์ตาม mockup |
| frontend/src/api/client.js: api.getSlots, api.createBooking | FR-BKG-01, FR-BKG-04, FR-BKG-06 | ไม่ | เป็น client stub ที่เรียก `/api/slots` และ `/api/bookings` แต่ไม่มีโมเดลข้อมูลจริงและไม่มีการประมวลผลผลลัพธ์ตามความต้องการธุรกิจ |

## 3. ข้อค้นพบ
| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-001 | โค้ดไม่มี FR | backend/app/main.py; frontend/src/App.jsx; frontend/src/api/client.js | FR-BKG-01, FR-BKG-02, FR-BKG-03, FR-BKG-04, FR-BKG-05, FR-BKG-06 | โค้ดมีเฉพาะ skeleton และ client stub ไม่มี logic สำหรับแสดงช่วงเวลาว่าง ปฏิเสธการจองซ้ำ จัดสรรตัวเลือกเมื่อ slot เต็ม บันทึกการจอง ส่งข้อความยืนยัน และคำนวณตามแพ็กเกจ |  |
| F-002 | AC ไม่มี test | backend/tests; frontend/src/__tests__/setup.test.jsx | AC-BKG-01..AC-BKG-06 | มีเพียง test สำหรับ "โครงหน้าจอเปิดได้" ใน frontend และไม่มี test backend สำหรับ AC ใดเลย; pytest collected 0 items |  |
| F-003 | test อ่อน | frontend/src/__tests__/setup.test.jsx | AC-BKG-01..AC-BKG-06 | Test อ้างชื่อว่าเป็น UI setup แต่ assert เฉพาะข้อความ "ระบบจองคิวตรวจสุขภาพ" อย่างเดียว ไม่ตรวจว่า Then ของ AC ถูกจริง |  |
| F-004 | ไม่ตรง mockup | frontend/src/App.jsx | UI-BKG-01, UI-BKG-02, UI-BKG-03 | หน้า App ไม่มีส่วนเลือกแพ็กเกจ/วัน/ช่วงเวลา ไม่มีปุ่มยืนยันการจอง ไม่มีหมายเลขคิวที่เด่นตาม mockup และไม่แสดงสถานะตาม Requirement/UI |  |
| F-005 | AC ไม่มี test | attachment: file_AC-BKG-03.test.jsx (ไม่อยู่ใน workspace repo) | AC-BKG-03 | ไฟล์ทดสอบที่แนบเป็น `../pages/ConfirmBooking.jsx` แต่โฟลเดอร์ `frontend/src/pages/` ใน repo ยังไม่มีไฟล์ดังกล่าว จึงไม่สามารถใช้เป็นหลักฐานการตรวจว่าสร้างงาน T-11/T-12 เสร็จจริงได้ และยังไม่มี test จริงใน repo สำหรับ AC-BKG-03 |  |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
