#!/usr/bin/env bash
set -euo pipefail
CONTAINER=postgres_container
PGUSER=machouba
PGDB=piscineds
PGHOST=localhost
export PGPASSWORD=mysecretpassword

tables=(data_2022_oct data_2022_nov data_2022_dec data_2023_jan)

for t in "${tables[@]}"; do
  echo "Recreate table $t"
  docker exec -e PGPASSWORD="$PGPASSWORD" "$CONTAINER" psql -U "$PGUSER" -d "$PGDB" -h "$PGHOST" -v ON_ERROR_STOP=1 -c "
    DROP TABLE IF EXISTS $t;
    CREATE TABLE $t (
      event_time   timestamp      NOT NULL,
      event_type   text,
      product_id   integer,
      price        numeric(10,2),
      user_id      bigint,
      user_session uuid
    );
    COPY $t (event_time,event_type,product_id,price,user_id,user_session)
    FROM '/data/customer/${t}.csv' WITH (FORMAT csv, HEADER true, NULL '');
  "
done