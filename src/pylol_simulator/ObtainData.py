import glob
import json
import os.path
import re
import shutil
import sys
import tarfile
import requests
import wget


def obtain_latest_version(data):
    versions = {}
    # loop through every entry in the version data
    for entry in data:
        # split the entry by . producing ["12", "10", "1"]
        vals = entry.split(".")
        # convert the split version data into a tuple of integers
        versions[entry] = (int(vals[0]), int(vals[1]), int(vals[2]))
    # sorts the versions by their value
    versions = dict(sorted(versions.items(), key=lambda item: item[1], reverse=True))
    # returns the latest version
    return list(versions.keys())[0]


# Source: https://stackoverflow.com/a/61346454
# create this bar_progress method which is invoked automatically from wget
def bar_progress(current, total, width=80):
    current = round(current / 1048576, 2)
    total = round(total / 1048576, 2)
    progress_message = "Downloading: %d%% [%dMB / %dMB]." % (current / total * 100, current, total)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

# loops through the given .tgz file
def extract(tgz_file, directory, data_path):
    files_extracted = 0
    # loop through every item in .tgz file
    for item in tgz_file:
        # ensures that the item name is in en_GB
        if item.name.startswith(data_path):
            # checks if the file is champion.json or item.json
            if data_path + "champion.json" in item.name or data_path + "item.json" in item.name:
                # extract file if it is champion.json or item.json
                tgz_file.extract(item.name, directory)
                files_extracted += 1
    return files_extracted


print("Downloading data required for the scripts.")
working_directory = "./temp/"
output_directory = "./data/"
# create the working directory if it does not exist (temp)
if not os.path.exists(working_directory):
    os.mkdir(working_directory)
versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
data_url = "https://ddragon.leagueoflegends.com/cdn/dragontail-{version}.tgz"
expected_file_name = working_directory + "dragontail-{version}.tgz"
data_folder = "{version}/data/en_GB/"
print(f"Downloading {versions_url} to obtain the latest version.")
# using the python module requests, obtain the versions.json file
resp = requests.get(versions_url)
# parse the in-memory versions.json file into JSON data
version_data = json.loads(resp.text)
resp.close()
# compile the standardised version system (Riot Games updated their patch numbering system)
version_pattern = re.compile("\d+\\.\d+\\.\d+")
# collect all versions that conform to the above standard
version_data = [version for version in version_data if version_pattern.fullmatch(version)]
# obtain the latest version
latest_version = obtain_latest_version(version_data)
print(f"Latest Version: {latest_version}.")
# substitute the latest version into the strings, replacing {version} with the latest version
data_url = re.sub("\\{version}", latest_version, data_url)
expected_file_name = re.sub("\\{version}", latest_version, expected_file_name)
data_folder = re.sub("\\{version}", latest_version, data_folder)
# if the .tgz file is already downloaded, do not download it again
if not os.path.exists(expected_file_name):
    print(f"Downloading {data_url} to {working_directory}.")
    # download the tgz file if it is missing using the python module "wget"
    dragontail_tgz_file = wget.download(data_url, working_directory, bar=bar_progress)
    dragontail_tgz_file = re.sub("/+", "/", dragontail_tgz_file)
    # Newline as bar_progress doesn't produce one.
    print(f"\nSucessfully downloaded {dragontail_tgz_file} from {data_url}!")
else:
    dragontail_tgz_file = expected_file_name
dragontail_file = tarfile.open(dragontail_tgz_file, 'r')
print(f"Extracting data from {dragontail_tgz_file}.")
content_directory = re.sub("\\.tgz", "", dragontail_tgz_file)
# extract champion.json and item.json from the downloaded .tgz file
extracted_count = extract(dragontail_file, content_directory, data_folder)
print(f"Extracted {extracted_count} files from {dragontail_tgz_file}.")
# create the output directory (data)
if not os.path.exists(output_directory):
    os.mkdir(output_directory)
print(f"Moving data into {output_directory}: ", end='')
extracted_content_folder = content_directory + "/" + data_folder
# find all files within the extracted data folder
files = glob.glob(extracted_content_folder + "/**")
# loop through the found files
for file in files:
    try:
        # using the python module "shutil", move the extracted file into the output directory
        shutil.move(file, output_directory)
    except shutil.Error:
        continue

print("Done.")
dragontail_file.close()