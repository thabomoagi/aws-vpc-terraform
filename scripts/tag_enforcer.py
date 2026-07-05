import boto3
import sys
from botocore.exceptions import ClientError

REQUIRED_TAGS = ['environment', 'owner', 'project']

def get_bucket_tags(s3, bucket_name: str) -> dict:
    """Fetch tags for a bucket, returning an empty dict if none exist."""
    try:
        tagging = s3.get_bucket_tagging(Bucket=bucket_name)
        return {t['Key']: t['Value'] for t in tagging['TagSet']}
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchTagSet':
            return {}
        # Anything else (AccessDenied, throttling, etc.) — don't mask it
        raise

def check_s3_tags() -> int:
    s3 = boto3.client('s3')
    non_compliant = []

    try:
        response = s3.list_buckets()
    except ClientError as e:
        print(f"ERROR: Could not list buckets: {e}", file=sys.stderr)
        return 1

    for bucket in response['Buckets']:
        name = bucket['Name']
        try:
            tags = get_bucket_tags(s3, name)
        except ClientError as e:
            print(f"ERROR: Could not fetch tags for {name}: {e}", file=sys.stderr)
            non_compliant.append(name)
            continue

        missing = [tag for tag in REQUIRED_TAGS if tag not in tags]
        if missing:
            print(f"Alert: Bucket '{name}' is non-compliant. Missing tags: {missing}")
            non_compliant.append(name)

    print(f"\nSummary: {len(non_compliant)} non-compliant bucket(s) found.")
    return 1 if non_compliant else 0

if __name__ == "__main__":
    sys.exit(check_s3_tags())