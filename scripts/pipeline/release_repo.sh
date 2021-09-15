aws_access_key=$1
aws_access_secret=$2
bucket_name=$3
aws_key=$4
build_path="codecommit-base.zip"

rm -rf $build_path
cd ./initial_repo/ ; zip -r ../$build_path . * ; cd ..

pip3 install boto3

python3 scripts/pipeline/upload_file_to_s3.py $bucket_name $aws_key $aws_access_key $aws_access_secret $build_path