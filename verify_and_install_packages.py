#########################################
# Install python packages securely
#########################################
# mkdir tmp
# cd tmp
# pip download pip==24.0 pip-tools==7.3.0
# python verify_and_install_packages.py
# =======================================
# after pip-tools installed:
# echo scapy > requirements.in 
# pip-compile --generate-hashes requirements.in
# pip install --require-hashes -r requirements.txt


import hashlib
import os
import requests
import subprocess
import sys

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def get_pypi_sha256(package_name, wheel_filename):
    url = f"https://pypi.org/pypi/{package_name}/json"
    headers = {"User-Agent": "python-requests/2.31.0"}
    try:
        r = requests.get(url, timeout=10, headers=headers)
        r.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None

    data = r.json()
    for files in data["releases"].values():
        for file in files:
            if file["filename"] == wheel_filename:
                return file["digests"]["sha256"]
    return None

def verify_wheels(directory="."):
    verified_files = []
    for file in os.listdir(directory):
        if file.endswith(".whl"):
            print(f"\n🔍 Verifying: {file}")
            local_hash = compute_sha256(file)

            pkg_name = file.split("-")[0]
            expected_hash = get_pypi_sha256(pkg_name, file)

            if expected_hash is None:
                print(f"❌ Cannot find official hash for {file} on PyPI.")
                continue

            if local_hash.lower() == expected_hash.lower():
                print(f"✅ Hash matches: {file}")
                with open(file + ".sha256", "w") as f:
                    f.write(f"{local_hash}  {file}\n")
                verified_files.append(file)
            else:
                print(f"❌ Hash mismatch for {file}")
                print(f"Local   : {local_hash}")
                print(f"Expected: {expected_hash}")
    return verified_files

if __name__ == "__main__":
    wheels = verify_wheels()
    if wheels:
        print("\n🎉 All verified. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + wheels)
    else:
        print("\n❌ No wheels verified. Aborting install.")
