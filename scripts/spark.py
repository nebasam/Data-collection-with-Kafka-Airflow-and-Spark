import os
from pyspark.sql import SparkSession
import boto3
import pandas as pd

class Sparkscript():
    """  spark sessions """

    def __init__(self, bootstrap='b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092', create_topic=True, topic='transc_data'):
        



def load_data_s3(self, bucket_name='10academy-group4-bucket', file_name='Clean_Amharic.txt'):
    """ Load transcription data from s3 bucket"""
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1'
    )
    # Load file directly into python
    obj = s3.Bucket(bucket_name).Object(file_name).get()
    df = pd.read_csv(obj['Body'])
    return df

    df.columns = df.columns.str.replace("(","")
    df.columns = df.columns.str.replace(")","")
    df.columns = df.columns.str.replace("ብርሀን ፈይሳየኢትዮጵያ ቦክስ ፌዴሬሽን በየአመቱ የሚያዘጋጀው የክለቦች ቻምፒዮና በአዲስ አበባ ከተማ በመካሄድ ላይ ይገኛል sentence 1","sentence")
                                        
                    

def upload_file(self,file_name: str, bucket: str, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
                                        

                                        
def load_data(self,dataset_path):
        print("Loading the audio files")
        labels=[]
        # dictionary to store files
    
        # loop through all sub-folders
        for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

            # ensure we're processing at sub-folder level
            if dirpath is not dataset_path:

                # save label (i.e., sub-folder name) in the mapping 
                label = dirpath#.split("/")[-1]

                # process all audio files in the sub-directory
                for f in filenames:

                    # load audio file
                    filename=label+"/"+f
                    labels.append(filename)
        return labels                                        





                                        
   