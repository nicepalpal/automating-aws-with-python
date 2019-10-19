import boto3
import click


session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

#Click.group is a decorator - wraps a function, tells click about our function. click controls how it is executed
#Making this group delegates control of it to the CLI commandbelow
#Call CLI function

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    #Documentation string - when you type --help it will list documentation strings
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    for object in s3.Bucket(bucket).objects.all():
        print(object)

#Call CLI function instead of list buckets allows click to control
if __name__ == '__main__':
    cli()
