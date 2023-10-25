if __name__ == "__main__":
  import os

  paths = ['data/raw', 'data/processed', 'results/tables', 'results/plots']
  for path in paths:
      if not os.path.exists(path):
          os.makedirs(path)

  import scripts.data_ingestion
  import scripts.create_alternate_schema
  import scripts.data_processing
