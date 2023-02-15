"""ETL Component for this Project"""

from typing import NamedTuple
from pipelineusingpolars.common.s3_connector import s3Bucket_Connector

class source_Config(NamedTuple):
    """
    Class for Source Configuration Data


    src_first_extract_date: Determines the date for extracting the source
    src_columns: Source Columns Names
    src_col_date : Column Name for Date in Source
    src_col_isin : Column Name for isin in Source
    src_col_time: Column Name for time in Source
    src_col_start_price : Column Name for Start Price in Source
    src_col_min_price: Column Name for Minimum Price in Source
    src_col_max_price: Column Name for Maximum Price in Source
    src_col_traded_vol: Column Name for Traded Volume in Source

    """

    src_first_extract_date: str
    src_columns: str
    src_col_date : str
    src_col_isin : str
    src_col_time: str
    src_col_start_price : str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str

class target_Config(NamedTuple):
    """
    Class for target configuration data

    trg_col_isin: column name for isin in target
    trg_col_date: column name for date in target
    trg_col_op_price: column name for opening price in target
    trg_col_clos_price: column name for closing price in target
    trg_col_min_price: column name for minimum price in target
    trg_col_max_price: column name for maximum price in target
    trg_col_dail_trad_vol: column name for daily traded volume in target
    trg_col_ch_prev_clos: column name for change to previous day's closing price in target
    trg_key: basic key of target file
    trg_key_date_format: date format of target file key
    trg_format: file format of the target file
    """
    trg_col_isin: str
    trg_col_date: str
    trg_col_op_price: str
    trg_col_clos_price: str
    trg_col_min_price: str
    trg_col_max_price: str
    trg_col_dail_trad_vol: str
    trg_col_ch_prev_clos: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str

class ETLProcess():
    """
    Reads Data , Transforms and writes the data back to target
    """
    def __init__(self, s3_bucket_src: S3BucketConnector,
                 s3_bucket_trg: S3BucketConnector, meta_key: str,
                 src_args: source_Config, trg_args: target_Config):
        """
        Constructor for XetraTransformer

        :param s3_bucket_src: connection to source S3 bucket
        :param s3_bucket_trg: connection to target S3 bucket
        :param meta_key: used as self.meta_key -> key of meta file
        :param src_args: NamedTouple class with source configuration data
        :param trg_args: NamedTouple class with target configuration data
        """
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date =
        self.extract_date_list =
        self.meta_update_list = 
    
    def extract(self):
        pass

    def transform_report1(self):
        pass
    
    def load(self):
        pass
    
    def etl_report1(self):
        pass