#!/usr/bin/env bash
set -euo pipefail
CONTAINER=postgres_container
PGUSER=machouba
PGDB=piscineds
PGHOST=localhost
export PGPASSWORD=mysecretpassword

  echo "Recreate table items"
  # Créer la table d'abord
  docker exec -e PGPASSWORD="$PGPASSWORD" "$CONTAINER" psql -U "$PGUSER" -d "$PGDB" -h "$PGHOST" -v ON_ERROR_STOP=1 -c "
    DROP TABLE IF EXISTS item;
    CREATE TABLE item (
      product_id   integer NOT NULL,
      category_id  BIGINT,
      category_code        varchar(255),
      brand       varchar(255)
    );
  "
  
  # Utiliser \copy via stdin pour charger les données
  echo "\copy item from '/data/item/item.csv' WITH (FORMAT csv, HEADER true);" | docker exec -i -e PGPASSWORD="$PGPASSWORD" "$CONTAINER" psql -U "$PGUSER" -d "$PGDB" -h "$PGHOST" -v ON_ERROR_STOP=1
  
  echo "Table items recreated successfully"