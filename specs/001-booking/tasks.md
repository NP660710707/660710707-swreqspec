# Tasks: จองคิวตรวจสุขภาพ (Booking)
- Feature: จองคิวตรวจสุขภาพ (Booking)
- Spec ID: SPEC-BKG-001
- อ้างอิง: [spec.md](./spec.md) Draft v3, [plan.md](./plan.md)
- วันที่: 2569-10-07

สรุป: มี 9 เฟส รวม 20 tasks; ในจำนวนนี้ 2 tasks รอคำตอบ Q-02  
เฟสแรกที่ลองใช้ได้จริงคือเฟส 1: เลือกแพ็กเกจและดูช่วงเวลาว่าง  
งานในเฟส 2–3 ทำส่วนที่ไม่ติด Q-02 ก่อน โดยจุดตรวจจะระบุสิ่งที่ยังขาดจนกว่าจะกำหนดรูปแบบหมายเลขคิว

## เฟส 0: ฐานราก

### T-01 รวมค่ากำหนดจากข้อกำหนด
- รองรับ: FR-BKG-01, FR-BKG-02, FR-BKG-03, FR-BKG-05, NFR-PERF-01, NFR-SEC-01, NFR-REL-02, NFR-USE-01, ASM-02, ASM-03, ASM-06, DOM-PDPA-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-04, T-07, T-11, T-13, T-15, T-17, T-18
- ไฟล์ที่แตะ: `backend/app/config.py`, `frontend/src/config.js`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: ค่าที่ตั้งได้ใน plan.md อยู่ในไฟล์ config กลางพร้อมคอมเมนต์อ้าง ID และไม่มีการกำหนดรูปแบบคิวแทน Q-02
- สถานะ: พร้อมทำ

### T-02 เตรียมฐานข้อมูลและโมเดลหลัก
- รองรับ: CON-TECH-01, IF-HIS-01, FR-BKG-02, FR-BKG-04, DM-01, DM-02, DM-03, DM-04
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-04, T-07
- ไฟล์ที่แตะ: `backend/app/db.py`, `backend/app/models.py`, `backend/app/migrations/001_booking.py`, `backend/tests/test_booking_models.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: PostgreSQL เก็บ Booking ที่อ้างอิง HN/Slot และไม่สร้างฟิลด์เก็บเลขบัตรประชาชน
- สถานะ: พร้อมทำ

### T-03 เปิดแอปหลังบ้านพร้อมตรวจตัวตนและ TLS
- รองรับ: IF-IDP-01, NFR-SEC-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-04 และ T-07
- ไฟล์ที่แตะ: `backend/app/main.py`, `backend/app/auth.py`, `backend/app/config.py`, `backend/tests/test_app_start.py`, `backend/tests/test_auth_gate.py`, `backend/tests/test_transport_security.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: แอป FastAPI เปิดได้ และการเข้าถึงข้อมูลผู้รับบริการต้องผ่านผลยืนยันตัวตน พร้อมกำหนด TLS ขั้นต่ำตาม NFR-SEC-01
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 0
- test ที่ต้องผ่านทั้งหมด: `test_app_starts`, `test_patient_data_requires_identity`, `test_transport_requires_minimum_tls`; ไม่มี AC ตรง ๆ ในเฟสนี้
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม FR-BKG-01:
  Given เปิด PostgreSQL และแอปตาม plan.md
  When เรียกหน้า/บริการเริ่มต้นของระบบ
  Then ระบบเริ่มทำงาน และยังไม่เปิดข้อมูลผู้รับบริการโดยไม่มีผลยืนยันตัวตน
- ยังขาด: ไม่มี

## เฟส 1: เลือกแพ็กเกจและดูช่วงเวลาว่าง (FR-BKG-01, FR-BKG-06 — ไม่มี AC เฉพาะ)

### T-04 แสดงแพ็กเกจและค้นหาช่วงเวลาว่าง
- รองรับ: FR-BKG-01, FR-BKG-06, NFR-PERF-01, ASM-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานของ FR-BKG-01/FR-BKG-06; AC-BKG-05 วัดเกณฑ์โหลดในเฟส 7
- ไฟล์ที่แตะ: `backend/app/slots/router.py`, `backend/app/slots/service.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-02, T-03
- เสร็จเมื่อ: API แสดงแพ็กเกจและ Slot ที่ว่างพร้อมที่นั่งคงเหลือ และคำนวณรายการใหม่เมื่อรับแพ็กเกจอื่น
- สถานะ: พร้อมทำ

### T-05 สร้างหน้าจอเลือกแพ็กเกจและเวลา
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานของ FR-BKG-01/FR-BKG-06
- ไฟล์ที่แตะ: `frontend/src/pages/SlotPicker.jsx`, `frontend/src/App.jsx`, `frontend/src/api/client.js`
- แบบหน้าจอ: UI-BKG-01 `mockups/UI-BKG-01-select-slot.html`
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: หน้าจอเรียก API ผ่าน `client.js` แสดงแพ็กเกจอยู่บนสุด เฉพาะช่วงที่ว่างพร้อม “เหลือ N ที่” และเปลี่ยนแพ็กเกจแล้วเรียกข้อมูลใหม่
- สถานะ: พร้อมทำ

### T-06 ทดสอบการเลือกแพ็กเกจและช่วงเวลา
- รองรับ: FR-BKG-01, FR-BKG-06, UI-BKG-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานของ FR-BKG-01/FR-BKG-06
- ไฟล์ที่แตะ: `frontend/src/__tests__/slot-picker.test.jsx`, `backend/tests/test_slots.py`
- แบบหน้าจอ: UI-BKG-01 `mockups/UI-BKG-01-select-slot.html`
- ต้องทำหลัง: T-05
- เสร็จเมื่อ: tests ยืนยันการแสดงช่วงว่าง/ที่นั่งคงเหลือและการโหลดใหม่หลังเปลี่ยนแพ็กเกจ โดยใช้ client จำลองใน test หน้าจอ
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 1
- test ที่ต้องผ่านทั้งหมด: `test_slots_list_available_and_remaining`, `test_slot_picker_shows_available_slots`, `test_slot_picker_reloads_on_package_change`; และ tests จากเฟส 0 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม FR-BKG-01:
  Given มีแพ็กเกจและ Slot ที่มีที่นั่งคงเหลือ
  When เลือกแพ็กเกจแล้วเปิดดูวันและช่วงเวลา จากนั้นเปลี่ยนแพ็กเกจ
  Then เห็นเฉพาะช่วงที่ว่างพร้อมจำนวนที่นั่ง และรายการช่วงเวลาถูกคำนวณใหม่
- ยังขาด: FR-BKG-06 ไม่มี AC เฉพาะใน spec จึงยังไม่มีเกณฑ์ acceptance ของทีมสำหรับการเปลี่ยนแพ็กเกจ

## เฟส 2: จองช่วงเวลาที่ว่าง (AC-BKG-01)

### T-07 บันทึกการจองและตัดที่นั่ง
- รองรับ: FR-BKG-04, CON-TECH-01
- ตรวจด้วย: AC-BKG-01 (ส่วนบันทึกสำเร็จและที่นั่งคงเหลือเป็น 0)
- ไฟล์ที่แตะ: `backend/app/bookings/router.py`, `backend/app/bookings/service.py`, `backend/tests/test_booking_create.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-02, T-03, T-04
- เสร็จเมื่อ: `test_AC_BKG_01_booking_consumes_last_seat` ตรวจว่าที่นั่งว่าง 1 ที่ถูกจองและที่นั่งคงเหลือเป็น 0; ส่วนหมายเลขคิวจริงติด Q-02
- สถานะ: พร้อมทำ

### T-08 แสดงผลการจองจากข้อมูล API
- รองรับ: FR-BKG-04, UI-BKG-02, UI-BKG-03
- ตรวจด้วย: AC-BKG-01 (ส่วนแสดงผล โดย test ใช้ค่าหมายเลขคิวจาก client จำลอง)
- ไฟล์ที่แตะ: `frontend/src/pages/ConfirmBooking.jsx`, `frontend/src/pages/BookingResult.jsx`, `frontend/src/api/client.js`, `frontend/src/__tests__/booking-result.test.jsx`
- แบบหน้าจอ: UI-BKG-02 `mockups/UI-BKG-02-confirm.html`; UI-BKG-03 `mockups/UI-BKG-03-result.html`
- ต้องทำหลัง: T-05, T-07
- เสร็จเมื่อ: `test_AC_BKG_01_result_renders_queue_value` ยืนยันว่าหน้าจอเรียก API ผ่าน client.js และแสดงค่าคิวที่ client ส่งโดยไม่แปลงหรือกำหนดรูปแบบเอง
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 2
- test ที่ต้องผ่านทั้งหมด: `test_AC_BKG_01_booking_consumes_last_seat`, `test_AC_BKG_01_result_renders_queue_value`, และ tests จากเฟส 0–1 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม AC-BKG-01:
  Given มีช่วง 09.00 น. เหลือ 1 ที่ และผู้รับบริการยืนยันตัวตนแล้ว
  When ยืนยันการจอง
  Then การจองถูกบันทึก ที่นั่งคงเหลือเป็น 0 และหน้าจอแสดงหมายเลขคิวที่ API ส่งกลับ
- ยังขาด: การสร้างหมายเลขคิวจริงยังรอ Q-02; AC-BKG-01 จะยังไม่ครบ end-to-end จนกว่า T-20 เสร็จ

## เฟส 3: ปฏิเสธการจองซ้ำในวันเดียวกัน (AC-BKG-02)

### T-09 ปฏิเสธเมื่อมีคิวที่ยังไม่ได้ใช้
- รองรับ: FR-BKG-02, ASM-02, ASM-04
- ตรวจด้วย: AC-BKG-02 (ส่วนตรวจวันเดียวกันและปฏิเสธการจองซ้ำ)
- ไฟล์ที่แตะ: `backend/app/bookings/service.py`, `backend/tests/test_booking_duplicate.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-07
- เสร็จเมื่อ: `test_AC_BKG_02_rejects_same_day_booking` ตรวจว่าผู้รับบริการที่มี Booking สถานะ “จองแล้ว” ในวันเดียวกันถูกปฏิเสธ โดยวันคำนวณตาม Asia/Bangkok
- สถานะ: พร้อมทำ

### T-10 แสดงผลการปฏิเสธและคิวเดิม
- รองรับ: FR-BKG-02, UI-BKG-02
- ตรวจด้วย: AC-BKG-02 (ส่วนแสดงหมายเลขคิวเดิม; test หน้าจอใช้ response จำลอง)
- ไฟล์ที่แตะ: `frontend/src/pages/ConfirmBooking.jsx`, `frontend/src/api/client.js`, `frontend/src/__tests__/duplicate-booking.test.jsx`
- แบบหน้าจอ: UI-BKG-02 `mockups/UI-BKG-02-confirm.html`
- ต้องทำหลัง: T-08, T-09
- เสร็จเมื่อ: `test_AC_BKG_02_shows_existing_queue` ตรวจว่าหน้าจอปฏิเสธการจองและแสดงหมายเลขคิวเดิมจาก API response โดยไม่สร้างหมายเลขขึ้นเอง
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 3
- test ที่ต้องผ่านทั้งหมด: `test_AC_BKG_02_rejects_same_day_booking`, `test_AC_BKG_02_shows_existing_queue`, และ tests จากเฟส 0–2 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม AC-BKG-02:
  Given ผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน
  When ลองยืนยันการจองใหม่ในวันนั้น
  Then ระบบปฏิเสธและแสดงหมายเลขคิวเดิม
- ยังขาด: การสร้างหมายเลขคิวจริงยังรอ Q-02; end-to-end ที่ต้องแสดงคิวเดิมจะครบเมื่อ T-20 เสร็จ

## เฟส 4: เสนอช่วงเวลาเมื่อช่วงที่เลือกเต็ม (AC-BKG-03)

### T-11 ค้นหาและเรียงช่วงเวลาทางเลือก
- รองรับ: FR-BKG-03, ASM-02
- ตรวจด้วย: AC-BKG-03 (ส่วนเลือก 3 ช่วงและจัดลำดับ)
- ไฟล์ที่แตะ: `backend/app/slots/service.py`, `backend/app/bookings/service.py`, `backend/tests/test_booking_alternatives.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-04, T-07
- เสร็จเมื่อ: `test_AC_BKG_03_full_slot_suggestions` ตรวจว่าเมื่อ Slot เต็ม API คืน 3 ตัวเลือกในขอบเขตวันตาม FR-BKG-03 และเรียงตามระยะกับเกณฑ์ตัดสินเสมอที่กำหนด
- สถานะ: พร้อมทำ

### T-12 แสดงข้อความช่วงเวลาเต็มและตัวเลือก
- รองรับ: FR-BKG-03, UI-BKG-02
- ตรวจด้วย: AC-BKG-03 (ส่วนแจ้งเตือนและแสดงตัวเลือก)
- ไฟล์ที่แตะ: `frontend/src/pages/ConfirmBooking.jsx`, `frontend/src/api/client.js`, `frontend/src/__tests__/full-slot.test.jsx`
- แบบหน้าจอ: UI-BKG-02 `mockups/UI-BKG-02-confirm.html`
- ต้องทำหลัง: T-10, T-11
- เสร็จเมื่อ: `test_AC_BKG_03_suggestions_render` ตรวจว่าหน้าจอแสดง “ช่วงเวลาเต็ม” และตัวเลือกครบ 3 รายการพร้อมวัน/เวลา โดยไม่สร้าง Booking ใหม่
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 4
- test ที่ต้องผ่านทั้งหมด: `test_AC_BKG_03_full_slot_suggestions`, `test_AC_BKG_03_suggestions_render`, และ tests จากเฟส 0–3 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม AC-BKG-03:
  Given ช่วง 09.00 น. เหลือ 1 ที่ มีผู้ใช้อีกคนยืนยันก่อน และมีช่วงว่างอย่างน้อย 3 ช่วงในขอบเขตวันที่กำหนด
  When ผู้ใช้ยืนยันช่วง 09.00 น.
  Then เห็น “ช่วงเวลาเต็ม” และ 3 ตัวเลือกที่เรียงตามเกณฑ์ใน FR-BKG-03 โดยไม่มีรายการจองซ้อน
- ยังขาด: ไม่มี

## เฟส 5: คงการจองเมื่อส่งข้อความไม่สำเร็จ (AC-BKG-04)

### T-13 ส่งข้อความยืนยันแบบ asynchronous และทำซ้ำ
- รองรับ: FR-BKG-04, FR-BKG-05, IF-NOT-01, NFR-REL-02, ASM-03
- ตรวจด้วย: AC-BKG-04 (การจองคงอยู่และมีงานส่งซ้ำกำหนดภายใน 5 นาที)
- ไฟล์ที่แตะ: `backend/app/notifications/queue.py`, `backend/app/notifications/worker.py`, `backend/tests/test_notification_retry.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-07
- เสร็จเมื่อ: `test_AC_BKG_04_notification_retry` ตรวจว่า API ไม่รอผลส่งข้อความ มีงาน retry กำหนดภายใน 5 นาที และการจองยังคงบันทึกอยู่
- สถานะ: พร้อมทำ

### T-14 แสดงผลการจองแม้ข้อความยังส่งไม่สำเร็จ
- รองรับ: FR-BKG-05, UI-BKG-03
- ตรวจด้วย: AC-BKG-04 (ส่วนแสดงหมายเลขคิวและสถานะข้อความ)
- ไฟล์ที่แตะ: `frontend/src/pages/BookingResult.jsx`, `frontend/src/api/client.js`, `frontend/src/__tests__/notification-failure.test.jsx`
- แบบหน้าจอ: UI-BKG-03 `mockups/UI-BKG-03-result.html`
- ต้องทำหลัง: T-08, T-13
- เสร็จเมื่อ: `test_AC_BKG_04_failure_result_keeps_booking` ตรวจว่าหน้าผลแสดงค่าคิวจาก API กับสถานะส่งไม่สำเร็จ โดยไม่เปลี่ยนผลการจองเป็นล้มเหลว
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 5
- test ที่ต้องผ่านทั้งหมด: `test_AC_BKG_04_notification_retry`, `test_AC_BKG_04_failure_result_keeps_booking`, และ tests จากเฟส 0–4 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม AC-BKG-04:
  Given ระบบแจ้งเตือนไม่ตอบสนอง
  When ยืนยันการจอง
  Then การจองยังคงอยู่ หน้าจอแสดงหมายเลขคิว และมีงานส่งซ้ำกำหนดภายใน 5 นาที
- ยังขาด: การสร้างหมายเลขคิวจริงยังรอ Q-02; รายละเอียดการนับจำนวน retry ให้ทำตาม ASM-03 โดยไม่เพิ่มนโยบายอื่น

## เฟส 6: บันทึก audit log เมื่อเปิดดูการจอง (AC-BKG-06)

### T-15 บันทึก audit log ของการเข้าถึงข้อมูล
- รองรับ: DOM-PDPA-01, AC-BKG-06
- ตรวจด้วย: AC-BKG-06 (ส่วนสร้าง audit log)
- ไฟล์ที่แตะ: `backend/app/audit/service.py`, `backend/app/bookings/router.py`, `backend/app/models.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-02, T-03
- เสร็จเมื่อ: การเปิดดูรายละเอียดการจองบันทึกผู้เข้าถึง เวลา HN และการกระทำ พร้อมกำหนดการเก็บไม่น้อยกว่า 1 ปี
- สถานะ: พร้อมทำ

### T-16 ทดสอบข้อมูล audit log
- รองรับ: DOM-PDPA-01, AC-BKG-06
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: `backend/tests/test_audit_log.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-15
- เสร็จเมื่อ: `test_AC_BKG_06_audit_log` ตรวจพบผู้เข้าถึง เวลา และ HN หลังเปิดดูข้อมูลการจอง
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 6
- test ที่ต้องผ่านทั้งหมด: `test_AC_BKG_06_audit_log` และ tests จากเฟส 0–5 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม AC-BKG-06:
  Given มีข้อมูลการจองของผู้รับบริการ
  When เปิดดูข้อมูลการจอง
  Then มี audit log ระบุผู้เข้าถึง เวลา และรหัสผู้รับบริการ
- ยังขาด: ไม่มี

## เฟส 7: ตรวจสมรรถนะการค้นหาช่วงเวลาว่าง (AC-BKG-05)

### T-17 วัดเวลาค้นหาภายใต้ผู้ใช้พร้อมกัน
- รองรับ: NFR-PERF-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: `backend/tests/test_slot_search_performance.py`
- แบบหน้าจอ: ไม่มี
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: `test_AC_BKG_05_slot_search_performance` วัด p95 จากผู้ใช้พร้อมกัน 200 คนและรายงานผลเทียบเกณฑ์ไม่เกิน 2 วินาที
- สถานะ: พร้อมทำ

### T-18 ประเมินเวลาทำรายการของผู้ใช้ใหม่
- รองรับ: NFR-USE-01, ASM-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นการตรวจ NFR-USE-01
- ไฟล์ที่แตะ: `specs/001-booking/usability-test.md`
- แบบหน้าจอ: UI-BKG-01 `mockups/UI-BKG-01-select-slot.html`; UI-BKG-02 `mockups/UI-BKG-02-confirm.html`; UI-BKG-03 `mockups/UI-BKG-03-result.html`
- ต้องทำหลัง: T-08, T-10, T-12, T-14
- เสร็จเมื่อ: ผลทดสอบบันทึกว่าผู้รับบริการที่ไม่เคยใช้ฟีเจอร์ 10 คนทดลองทำรายการ และรายงานจำนวนผู้สำเร็จภายใน 3 นาทีโดยไม่ขอความช่วยเหลือ
- สถานะ: พร้อมทำ

#### จุดตรวจเฟส 7
- test ที่ต้องผ่านทั้งหมด: `test_AC_BKG_05_slot_search_performance`, `test_NFR_USE_01_new_user_booking`; และ tests จากเฟส 0–6 ต้องยังผ่าน
- เปิดระบบ: หลังบ้าน `cd backend && uvicorn app.main:app --reload --port 8000`; หน้าบ้าน `cd frontend && npm run dev`
- คนลองเองตาม AC-BKG-05:
  Given สภาพแวดล้อมทดสอบรองรับผู้ใช้พร้อมกัน 200 คน
  When ผู้ใช้เหล่านั้นค้นหาช่วงเวลาว่าง
  Then p95 ของเวลาตอบสนองไม่เกิน 2 วินาที
- ยังขาด: ไม่มี; ต้องใช้สภาพแวดล้อมโหลดที่ควบคุมได้เพื่อยืนยันผล

## เฟส 8: รอคำตอบ

### T-19 สร้างหมายเลขคิวตามรูปแบบที่ทีมยืนยัน
- รองรับ: FR-BKG-02, FR-BKG-04, FR-BKG-05, ASM-06, DM-04, UI-BKG-02, UI-BKG-03
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นส่วนที่บล็อกของ AC-BKG-01, AC-BKG-02, AC-BKG-04
- ไฟล์ที่แตะ: `backend/app/bookings/queue_number.py`, `backend/app/bookings/service.py`, `backend/tests/test_queue_number.py`
- แบบหน้าจอ: UI-BKG-02 `mockups/UI-BKG-02-confirm.html`; UI-BKG-03 `mockups/UI-BKG-03-result.html`
- ต้องทำหลัง: T-07, T-09
- เสร็จเมื่อ: เมื่อทีมตอบ Q-02 แล้ว ระบบสร้างหมายเลขตามรูปแบบที่ยืนยันและนับใหม่รายวันตาม ASM-06
- สถานะ: รอ Q-02

### T-20 ตรวจการจอง end-to-end หลังได้รูปแบบหมายเลขคิว
- รองรับ: FR-BKG-02, FR-BKG-04, FR-BKG-05, AC-BKG-01, AC-BKG-02, AC-BKG-04
- ตรวจด้วย: AC-BKG-01, AC-BKG-02, AC-BKG-04
- ไฟล์ที่แตะ: `backend/tests/test_booking_flow.py`, `frontend/src/__tests__/booking-flow.test.jsx`
- แบบหน้าจอ: UI-BKG-02 `mockups/UI-BKG-02-confirm.html`; UI-BKG-03 `mockups/UI-BKG-03-result.html`
- ต้องทำหลัง: T-08, T-10, T-14, T-19
- เสร็จเมื่อ: หลังตอบ Q-02 แล้ว การจองสำเร็จ การปฏิเสธที่แสดงคิวเดิม และกรณีส่งข้อความล้มเหลวผ่าน AC end-to-end
- สถานะ: รอ Q-02

## ตารางตรวจความครบ

### AC กับ task
| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-07, T-08 (ส่วนที่ไม่ติด Q-02), T-20 (ครบ end-to-end) |
| AC-BKG-02 | T-09, T-10 (ส่วนที่ไม่ติด Q-02), T-20 (ครบ end-to-end) |
| AC-BKG-03 | T-11, T-12 |
| AC-BKG-04 | T-13, T-14 (ส่วนที่ไม่ติด Q-02), T-20 (ครบ end-to-end) |
| AC-BKG-05 | T-17 |
| AC-BKG-06 | T-15, T-16 |

### Constraint กับ task
| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-02 |
| DOM-PDPA-01 | T-15, T-16 |
| IF-IDP-01 | T-03 |
| IF-HIS-01 | T-02, T-03 |
| IF-NOT-01 | T-13 |

### FR กับ AC และเฟส
| FR ID | AC ที่ตรวจ FR นี้ | เฟส |
|---|---|---|
| FR-BKG-01 | AC-BKG-05 (เกณฑ์ performance ของการค้นหา) | เฟส 1, เฟส 7 |
| FR-BKG-02 | AC-BKG-02 | เฟส 3 |
| FR-BKG-03 | AC-BKG-03 | เฟส 4 |
| FR-BKG-04 | AC-BKG-01 | เฟส 2 |
| FR-BKG-05 | AC-BKG-04 | เฟส 5 |
| FR-BKG-06 | ไม่มี AC ควรเสนอทีมเพิ่ม | เฟส 1 |

## สิ่งที่ยังไม่ทำ
- Q-01 ตอบแล้ว: ขอบเขตตัวเลือกคือวันก่อนหน้าวันที่เลือก 1 วัน วันที่เลือก และวันถัดไป 1 วัน (FR-BKG-03); ไม่มี task รอ Q-01
- Q-02 ยังไม่ได้คำตอบเรื่องรูปแบบหมายเลขคิว; T-19/T-20 รอคำตอบก่อนทำส่วนสร้างหมายเลขและทดสอบ end-to-end ตามที่ระบุใน UI-BKG-02, UI-BKG-03 และ DM-04
- plan.md ระบุว่ายังไม่ชัดว่ากำหนด retry 5 นาทีใน NFR-REL-02 สัมพันธ์กับช่วงห่าง 5 นาทีและจำนวน retry ใน ASM-03 อย่างไร; ไม่มี Q-xx เฉพาะใน spec จึงไม่สร้าง ID เพิ่ม งาน T-13 จำกัดตามค่าที่ระบุไว้และต้องไม่กำหนดนโยบายเพิ่มเติม
- IF-IDP-01 และ IF-HIS-01 ไม่ระบุพฤติกรรมเมื่อระบบภายนอกไม่ตอบสนอง; tasks นี้ไม่กำหนด fallback เพิ่มเอง
- เฟส 1 เป็นเส้นทางที่เปิดให้ลองเลือกแพ็กเกจ/ช่วงเวลาได้ก่อน; จุดตรวจ booking ในเฟส 2, 3 และ 5 จะยังไม่สมบูรณ์ end-to-end จนกว่า T-19 จะเสร็จ
