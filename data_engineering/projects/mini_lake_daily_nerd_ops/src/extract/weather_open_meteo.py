from src.utils.logger import get_logger

def main():
    logger = get_logger("weather_open_meteo")
    logger.info("Iniciando ingestão (teste logger)")
    logger.warning("Isso é um warning de teste")
    logger.error("Isso é um erro de teste (sem crash)")

if __name__ == "__main__":
    main()
