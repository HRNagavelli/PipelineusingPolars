import logging , logging.config

import yaml



def main():
    """
    Entry Point to Run this Pipeline using Polars 
    """
    #passing YAML File
    config_path = "Config/logging_configuration.yml"
    config = yaml.safe_load(open(config_path))
    #Configure Logging
    log_Config = config['logging']
    logging.config.dictConfig(log_Config)
    logger = logging.getLogger(__name__)
    logger.info('This is a Test.')

    if __name__ == '__main__':
        main()