"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage
import pulumi_gcp as gcp

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket', location="US")
image_store_acl = gcp.storage.BucketACL("image-store-acl",
            bucket=bucket.name,
            predefined_acl="public-read"
    )

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
