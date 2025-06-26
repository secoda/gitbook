---
description: List of all the metadata that Secoda pulls from Azure Data Lake
---

# ADL Metadata Extracted

### Supported file formats

Extraction of metadata is only supported for the following file formats:

```
CSV (*.csv)
TSV (*.tsv)
JSON (*.json)
JSONL (*.jsonl)
Parquet (*.parquet)
Apache Avro (*.avro)
```

### What does Secoda extract from Azure Data Lake?

Database (Storage Account containers are referred to as databases in Secoda)

* Name

Schema (Directories within a container are referred to as schemas in Secoda)

* Name

Table (Files are referred to as tables in Secoda)

* Name
* File format type (Parquet, CSV, JSON, etc.)

Columns (Fields in files are referred to as columns in Secoda)

* Name
* Data type

### Important Notes

* Secoda will extract metadata from the most recent version of files when multiple versions exist
* The integration supports up to 100,000 files per container extraction limit
