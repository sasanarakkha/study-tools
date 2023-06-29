#! /bin/bash

# Copyright 2022 Anton Karmanov
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Script creates a new release for pointed GitHub repository and uploads
# pointed files
#
#                    ↓ owner     ↓ repo
# https://github.com/bergentroll/dotfiles

set -e

# Create at https://github.com/settings/tokens with access to repository
declare -r token='[here your token]'

# Username or "organization"
declare -r owner='sasanarakkha'

# Name of repository
declare -r repo='study-tools'

# Array of filenames
# Must be filenames without path, so script may be in any location, but
# current working directory must contains enumerated files.
declare -a assets=('analysis-of-sbs-pāli-english-recitations.pdf' 'dhp-vocab.apkg' 'dhp-vocab.csv' 'patimokkha-word-by-word.apkg' 'patimokkha-word-by-word.csv' 'roots.apkg' 'roots.csv' 'ru-pali-dict.zip' 'ru-pali-vocab.apkg' 'ru-pali-vocab.csv' 'sbs-pali-english-vocab.apkg' 'sbs-pd.csv' 'sbs-pd.zip' 'sutta-pitaka-vocab.apkg' 'sutta-pitaka-vocab.csv' 'dhp-learning.apkg' 'patimokkha-learning.apkg' 'sbs-daily-chanting-sentences.apkg')

# Title of the release will be prepended with this through a space
declare -r release_base_name='Build'

# Tag will be prepended with this through a dash
declare -r tag_base_name='artifacts'

# Custom text
release_body="$(cat head.md)"


# Must be bool i.e. 'false' of 'true'
# Draft will not be public and will be placed on top of the list of releases
declare -r draft='false'

# <=== END OF CONFIG ===>

command -V curl
command -V file
command -V jq

declare -r authorization_header="Authorization: token ${token}"
declare -r accept_header='Accept: application/vnd.github+json'
declare -r api_base_url="https://api.github.com/repos/${owner}/${repo}/releases"
declare -r upload_base_url="https://uploads.github.com/repos/${owner}/${repo}/releases"
tag_name="${tag_base_name}-$(date +'%d.%m.%Y_%H-%M-%S' --utc)"
declare -r tag_name
release_name="${release_base_name} $(date +'%d.%m.%Y %H:%M' --utc) UTC"
declare -r release_name

release_json=$(jq --null-input \
     --arg tag_name "$tag_name" \
     --arg name "$release_name" \
     --arg body "$release_body" \
     --argjson draft "$draft" \
     '{tag_name: $tag_name, name: $name, body: $body, draft: $draft}')

create_release_output=$(curl \
  --request POST \
  --header "$authorization_header" --header "$accept_header" \
  --data "$release_json" \
  "$api_base_url")
echo "$create_release_output" | jq
echo

release_id=$(echo "$create_release_output" | jq '.id')
declare -r release_id

echo "ID = ${release_id}"
echo

for asset in "${assets[@]}"; do
  content_type=$(file -b --mime-type "$asset")
  urlencoded_asset=$(printf "$asset" | jq -srR @uri)

  echo "Uploading asset $asset"
  echo "Urlencoded assert name is ${urlencoded_asset}"
  curl \
    --request POST \
    --header "$authorization_header" --header "$accept_header" \
    --header "Content-Type: ${content_type}" \
    --data-binary "@${asset}" \
    "${upload_base_url}/${release_id}/assets?name=${urlencoded_asset}" | jq
  echo
done
