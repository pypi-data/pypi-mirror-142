import os
import sys
import time
import threading

import pyspark.pandas as ps

from pyspark.sql import dataframe, functions as F
from pyspark.sql import SparkSession

from TweetAnalysis.config.core import config
from TweetAnalysis.config import logging_config
from TweetAnalysis.tweets_streamer import get_stream


_logger = logging_config.get_logger(__name__)


# env variables for spark and kafka
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark-shell'
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


urlPattern = r"((http://)[^ ]*|(https://)[^ ]*|(www\.)[^ ]*)"
userPattern = '@[^\s]+'
hashtagPattern = '#[^\s]+'
alphaPattern = "[^a-z0-9<>]"
sequencePattern = r"(.)\1\1+"
seqReplacePattern = r"\1\1"

# Defining regex for emojis
smileemoji = r"[8:=;]['`\-]?[)d]+"
sademoji = r"[8:=;]['`\-]?\(+"
neutralemoji = r"[8:=;]['`\-]?[\/|l*]"
lolemoji = r"[8:=;]['`\-]?p+"


def make_spark():
    global spark
    spark = SparkSession.builder.master("local[1]").appName("tweets reader")\
        .config("spark.some.config.option", "some-value")\
        .getOrCreate()


def connect_to_kafka_stream() -> dataframe:
    """reading stream from kafka"""

    _logger.info('reading stream from kafka...')

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", config.kafka.KAFKA_HOST) \
        .option("subscribe", config.kafka.KAFKA_TOPIC_NAME) \
        .load()

    df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS string)")
    df = df.withColumn('tweet', df['value'])

    df = df.withColumn('value', F.regexp_replace(
        'value', userPattern, '<user>'))
    df = df.withColumn('value', F.regexp_replace('value', 'RT', ''))
    df = df.withColumn('value', F.regexp_replace('value', urlPattern, '<url>'))
    df = df.withColumn('value', F.regexp_replace(
        'value', smileemoji, '<smile>'))
    df = df.withColumn('value', F.regexp_replace(
        'value', sademoji, '<sadface>'))
    df = df.withColumn('value', F.regexp_replace(
        'value', neutralemoji, '<neutralface>'))
    df = df.withColumn('value', F.regexp_replace(
        'value', lolemoji, '<lolface>'))
    df = df.withColumn('value', F.regexp_replace(
        'value', sequencePattern, seqReplacePattern))
    df = df.withColumn('value', F.regexp_replace('value', userPattern, ''))
    df = df.withColumn('value', F.regexp_replace('value', r'/', ' / '))

    return df


def stream_to_pandas(batch_df, batch_id):
    df_pandas = ps.DataFrame(batch_df)
    print(df_pandas)
    return df_pandas

def write_stream_to_memory(df):
    """writing the tweets stream to memory"""

    _logger.info('writing the tweets stream to memory...')

    S = df.writeStream \
        .trigger(processingTime='3 seconds') \
        .option("truncate", "false") \
        .format('memory') \
        .outputMode("append") \
        .queryName('Table') \
        .start()#.awaitTermination()
    



def main(topic, wait=10):
    _logger.info(f'wating for {wait} seconds...')
    thread = threading.Thread(target=get_stream, args={'topic': topic})
    thread.start()

    make_spark()
    df = connect_to_kafka_stream()

    # thread2 = threading.Thread(target=write_stream_to_memory, kwargs={'df': df})
    # thread2.start()
    write_stream_to_memory(df)
    time.sleep(wait)



    # df_pandas = to_pandas()
    return spark.sql("""select * from Table""").toPandas()

    # _logger.info('stopping spark...')
    # try:
    #     S.stop()
    #     spark.stop()
    # except BaseException as e:
    #     _logger.warning(f"Error: {e}")
    # print(df.toPandas().show())
    # return None


if __name__ == '__main__':
    print(main('music', 10))
