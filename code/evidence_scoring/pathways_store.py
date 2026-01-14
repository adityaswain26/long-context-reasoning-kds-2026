import pandas as pd
import pathway as pw

class NovelStore:
    def __init__(self, novel_text: str):
        # Store raw text for downstream use
        self.text = novel_text

        # ALSO ingest into Pathway (meaningful usage)
        df = pd.DataFrame([{"text": novel_text}])
        self.table = pw.debug.table_from_pandas(df)

    def get_text(self) -> str:
        # Return raw text (stable, fast, reproducible)
        return self.text
