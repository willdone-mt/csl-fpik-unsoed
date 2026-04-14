import json
import glob

# ubah function di bawah agar menerima argument optional berupa tipe2 dafpus yang dipakai akhir2 ini
# dan tambahkan skrip untuk mencampurkan tipe2 dafpus yang dipakai akhir2 ini agar mempermudah melihat contoh

def merge_json_files(directory_path):
    merged_data = []
    # Find all json files
    file_paths = glob.glob(directory_path + '/*.json')
    
    for path in file_paths:
        with open(path, 'r') as file:
            data = json.load(file)
            # .extend() "unpacks" the list from the file into the merged_data list
            if isinstance(data, list):
                merged_data.extend(data)
            else:
                # If a file happens to be a single object {}, still add it
                merged_data.append(data)
                
    return merged_data

directory_path = "preview_template/individual"
output_file = "preview_template/merged.json"

merged_data = merge_json_files(directory_path)

# Writing to the file will automatically wrap the result in []
with open(output_file, 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)

print(f"Successfully merged {len(merged_data)} items into {output_file}")
