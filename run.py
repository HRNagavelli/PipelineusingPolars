import logging 
import logging.config
import yaml



def main():
    """
    Entry Point to Run this Pipeline using Polars 
    """
    #passing YAML File
    config_path = '/Users/harshareddy/learnDE/PROD_ETL_Pipelines/ETLPipeline/PipelineusingPolars/Config/logging_configuration.yml'
    config = yaml.safe_load(open(config_path))
    print(config)
    #Configure Logging
    log_Config = config['logging']
    logging.config.dictConfig(log_Config)
    logger = logging.getLogger(__name__)
    logger.info('This is a Test.')

if __name__ == '__main__':
    main()




