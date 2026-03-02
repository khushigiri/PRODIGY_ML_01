import logging
import os

# Create logs folder if not exists
log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "app.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()