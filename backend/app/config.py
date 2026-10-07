"""ค่ากำหนดกลางจากข้อกำหนดของฟีเจอร์ Booking."""

# FR-BKG-01: ระยะค้นหาช่วงเวลาล่วงหน้า
BOOKING_LOOKAHEAD_DAYS = 30

# FR-BKG-03: จำนวนตัวเลือกและ Q-01: วันก่อนหน้า วันที่เลือก และวันถัดไป
ALTERNATIVE_SLOT_COUNT = 3
ALTERNATIVE_SLOT_DAY_OFFSETS = (-1, 0, 1)

# FR-BKG-02: จำนวนคิวที่ยังไม่ได้ใช้ต่อผู้รับบริการในวันเดียวกัน
MAX_ACTIVE_BOOKINGS_PER_PATIENT_PER_DAY = 1

# ASM-06: เริ่มลำดับหมายเลขคิวใหม่ในแต่ละวัน
QUEUE_SEQUENCE_RESET_DAILY = True

# ASM-02: เขตเวลาที่ใช้เปรียบเทียบวัน
BUSINESS_TIMEZONE = "Asia/Bangkok"

# ASM-03: จำนวนครั้งและช่วงห่างในการส่งข้อความซ้ำ
NOTIFICATION_MAX_RETRIES = 3
NOTIFICATION_RETRY_INTERVAL_MINUTES = 5

# NFR-REL-02: กำหนดให้ส่งข้อความที่ไม่สำเร็จซ้ำภายในเวลานี้
# ความสัมพันธ์กับช่วงห่างตาม ASM-03 ยังไม่กำหนด; ห้ามอนุมานลำดับ retry จากค่านี้เพียงอย่างเดียว
NOTIFICATION_RETRY_DEADLINE_MINUTES = 5

# DOM-PDPA-01: ระยะเวลาเก็บ audit log ขั้นต่ำ
AUDIT_LOG_RETENTION_YEARS = 1

# NFR-PERF-01: เกณฑ์ค้นหาช่วงเวลาว่างสำหรับทดสอบ
SLOT_SEARCH_P95_LIMIT_SECONDS = 2
SLOT_SEARCH_CONCURRENT_USERS = 200

# NFR-SEC-01: TLS ขั้นต่ำสำหรับข้อมูลการจองระหว่างรับส่ง
MIN_TLS_VERSION = "TLSv1.2"

# NFR-USE-01: เกณฑ์ทดสอบการใช้งานตาม ASM-05
BOOKING_USABILITY_TIME_LIMIT_MINUTES = 3
BOOKING_USABILITY_PASS_COUNT = 8
BOOKING_USABILITY_TESTER_COUNT = 10
