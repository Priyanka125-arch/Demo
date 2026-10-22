import json
import pandas as pd

# Read SBOM JSON
with open("sbom.cdx.json", "r") as file:
    sbom = json.load(file)

# Get components
components = sbom.get("components", [])

rows = []

for component in components:
    rows.append({
        "Name": component.get("name", ""),
        "Version": component.get("version", ""),
        "Type": component.get("type", ""),
        "Publisher": component.get("publisher", ""),
        "Group": component.get("group", ""),
        "PURL": component.get("purl", "")
    })

# Export to Excel
df = pd.DataFrame(rows)
df.to_excel("sbom.xlsx", index=False)

print("SBOM Excel file created successfully")
