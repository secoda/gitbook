import os
import re
import uuid
import boto3
import shutil

# Directory containing the Markdown files
directory_path = os.getcwd()

bucket_name = "secoda-public-media-assets"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

# After, run the following regex to fix the markdown embeds on the integrations page.
# INPUT: <figure><img src="(.*)" alt.*"><figcaption>(.*)</figcaption></figure>
# REPLACE: ![]($1)\n$2

# Define the regex patterns and replacement strings
regex_patterns = [
    r"(https://raw.*/.gitbook/assets/(.*\.(gif|png|jpg|jpeg|webp|mov|mp4|mpg|mpeg|m4v|pdf|csv)))",  # '.\g<1>'),
    r"(\..*gitbook/assets/(.*\.(gif|png|jpg|jpeg|webp|pdf|csv)))"  # , '.\g<1>'),
    # Add more regex patterns and replacements as needed
]

# Track files that have been successfully uploaded to S3
successfully_uploaded_files = set()

# Function to replace instances with UUIDs preserving the extension
def replace_with_uuids(file_path):
    file_modified = False
    for pattern in regex_patterns:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        original_content = content
        for match in re.findall(pattern, content):
            uuid_value = str(uuid.uuid4())

            key = f"{uuid_value}.{match[2]}"
            url = f"https://secoda-public-media-assets.s3.amazonaws.com/{key}"
            print(f"Replacing {match[0]} with {url} in {file_path}")

            local_file_path = f".gitbook/assets/{match[1]}"
            if "%" in local_file_path:
                local_file_path = local_file_path.replace("%20", " ")
                local_file_path = local_file_path.replace("\\", "")

            # Check if local file exists before uploading
            if os.path.exists(local_file_path):
                # Only add to processed files if upload is successful
                if upload_to_s3(local_file_path, key):
                    successfully_uploaded_files.add(local_file_path)
                    content = content.replace(match[0], url)
                    file_modified = True
                else:
                    print(f"Failed to upload {local_file_path}, keeping local file")
            else:
                print(f"Warning: Local file {local_file_path} not found, skipping upload")

        if file_modified:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Updated {file_path}")

# Function to upload a file to S3
def upload_to_s3(local_file_path, s3_key):
    try:
        bucket.upload_file(local_file_path, s3_key, ExtraArgs={"ACL": "public-read"})
        print(f"Uploaded {local_file_path} to S3 with key: {s3_key}")
        return True
    except Exception as e:
        print(f"Error uploading {local_file_path} to S3: {e}")
        return False

# Function to clean up successfully uploaded files
def cleanup_uploaded_files():
    if successfully_uploaded_files:
        print(f"\nCleaning up {len(successfully_uploaded_files)} successfully uploaded files...")
        for file_path in successfully_uploaded_files:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"Removed {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")
        
        # Remove empty directories in .gitbook/assets (only after files are removed)
        gitbook_assets_dir = ".gitbook/assets"
        if os.path.exists(gitbook_assets_dir):
            for root, dirs, files in os.walk(gitbook_assets_dir, topdown=False):
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    try:
                        if not os.listdir(dir_path):  # Directory is empty
                            os.rmdir(dir_path)
                            print(f"Removed empty directory: {dir_path}")
                    except Exception as e:
                        print(f"Error removing directory {dir_path}: {e}")
    else:
        print("No files were successfully uploaded, skipping cleanup")

# Main execution
if __name__ == "__main__":
    print("Starting asset processing...")
    
    # Loop through Markdown files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                replace_with_uuids(file_path)

    print(f"\nSuccessfully uploaded {len(successfully_uploaded_files)} files")
    
    # Clean up successfully uploaded files
    cleanup_uploaded_files()
    
    print("Asset processing and cleanup complete.")
