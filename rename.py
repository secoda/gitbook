import os
import re
import uuid
import boto3

# Directory containing the Markdown files
directory_path = os.getcwd()

bucket_name = "secoda-public-media-assets"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

# Define the regex patterns and replacement strings
regex_patterns = [
    r"(https://raw.*/.gitbook/assets/(.*\.(gif|png|jpg|jpeg|webp|mov|mp4|mpg|mpeg|m4v|pdf|csv)))",  # '.\g<1>'),
    r"(\..*gitbook/assets/(.*\.(gif|png|jpg|jpeg|webp|pdf|csv)))"  # , '.\g<1>'),
    # Add more regex patterns and replacements as needed
]


# Function to replace instances with UUIDs preserving the extension
def replace_with_uuids(file_path):
    for pattern in regex_patterns:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        for match in re.findall(pattern, content):
            uuid_value = str(uuid.uuid4())

            key = f"{uuid_value}.{match[2]}"
            url = f"https://secoda-public-media-assets.s3.amazonaws.com/{key}"
            print(f"Replacing {match[0]} with {url} in {file_path}")

            local_file_path = f".gitbook/assets/{match[1]}"
            if "%" in local_file_path:
                local_file_path = local_file_path.replace("%20", " ")
                local_file_path = local_file_path.replace("\\", "")

            upload_to_s3(local_file_path, key)
            content = content.replace(match[0], url)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)


# Function to upload a file to S3
def upload_to_s3(local_file_path, s3_key):
    bucket.upload_file(local_file_path, s3_key, ExtraArgs={"ACL": "public-read"})
    print(f"Uploaded {local_file_path} to S3 with key: {s3_key}")


# Loop through Markdown files in the directory
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        if file_name.endswith(".md"):
            file_path = os.path.join(root, file_name)
            replace_with_uuids(file_path)

print("Replacement with UUIDs and S3 upload complete.")
