from app.scanner import scan_resources
from app.logging_config import logger

if __name__ == "__main__":
    logger.info("Running Azure Cloud Optimizer scan..")
    scan_resources()
    logger.info("Scan Completed.")
