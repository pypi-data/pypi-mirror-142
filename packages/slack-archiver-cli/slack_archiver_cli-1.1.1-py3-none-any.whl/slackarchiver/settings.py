import os
from typing import Optional

import dotenv

dotenv.load_dotenv(verbose=True)

SLACK_BOT_TOKEN: Optional[str] = os.environ.get("SLACK_BOT_TOKEN", None)
