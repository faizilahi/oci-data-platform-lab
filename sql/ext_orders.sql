CREATE TABLE ext_orders (
  order_id VARCHAR2(32),
  amount NUMBER,
  order_date VARCHAR2(10)
) ORGANIZATION EXTERNAL (
  TYPE ORACLE_BIGDATA
  DEFAULT DIRECTORY data_pump_dir
  LOCATION ('raw/y=2024/m=09/d=15/')
);
