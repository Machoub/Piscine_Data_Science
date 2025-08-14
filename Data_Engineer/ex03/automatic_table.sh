#!/usr/bin/env bash
set -euo pipefail

CONTAINER=postgres_container
PGUSER=machouba
PGDB=piscineds
PGHOST=localhost
export PGPASSWORD=mysecretpassword

# Parcourt tous les CSV visibles dans le conteneur
mapfile -t files < <(docker exec "$CONTAINER" sh -lc 'ls /data/customer/*.csv 2>/dev/null')

for path in "${files[@]}"; do
  base=$(docker exec "$CONTAINER" sh -lc "basename '$path'")
  table="${base%.csv}"
  echo "Create/Load $table"

  docker exec "$CONTAINER" psql -U "$PGUSER" -d "$PGDB" -h "$PGHOST" -v ON_ERROR_STOP=1 -c "
    DROP TABLE IF EXISTS $table;
    CREATE TABLE $table (
      event_time   timestamp      NOT NULL,  -- 1: DATETIME
      event_type   text,                     -- 2
      product_id   integer,                  -- 3
      price        numeric(10,2),            -- 4
      user_id      bigint,                   -- 5
      user_session uuid                      -- 6 (remplacer par text si nécessaire)
    );
    COPY $table (event_time,event_type,product_id,price,user_id,user_session)
    FROM '/data/customer/$base' WITH (FORMAT csv, HEADER true, NULL '');
  "
done