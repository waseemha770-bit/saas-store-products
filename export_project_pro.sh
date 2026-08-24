#!/bin/bash

# Check if dialog is installed
if ! command -v dialog &> /dev/null; then
    echo "[!] Error: 'dialog' is not installed. Please install it using: pkg install dialog"
    exit 1
fi

OUTPUT_FILE="ai_project_context.md"

# Interactive menu using dialog (Updated Title)
CHOICE=$(dialog --stdout --title "GitHub to Gemini Reviewer" \
    --menu "Choose project source:" 12 50 2 \
    1 "Project is already on your phone (Local folder)" \
    2 "Clone temporarily from GitHub (Read-only & Safe)")

clear

if [ "$CHOICE" == "1" ]; then
    TARGET_DIR=$(dialog --stdout --inputbox "Enter local folder path on your phone:" 8 50 "/data/data/com.termux/files/home/")
    clear
    if [ ! -d "$TARGET_DIR" ]; then
        echo "[!] Error: Directory does not exist."
        exit 1
    fi
    echo " [+] Reading project locally from: $TARGET_DIR"

elif [ "$CHOICE" == "2" ]; then
    USERNAME=$(dialog --stdout --inputbox "Enter GitHub Username:" 8 50)
    REPO=$(dialog --stdout --inputbox "Enter Repository Name:" 8 50)
    TOKEN=$(dialog --stdout --passwordbox "Enter GitHub Personal Access Token (PAT):" 8 50)
    clear
    
    TARGET_DIR="temp_read_only_folder"
    REPO_URL="https://${TOKEN}@github.com/${USERNAME}/${REPO}.git"
    
    echo "[*] Cloning repository temporarily (Read-only)..."
    git clone "$REPO_URL" "$TARGET_DIR" &>/dev/null
    
    if [ $? -ne 0 ]; then
        echo "[!] Error: Failed to clone. Check your details or token."
        exit 1
    fi
    echo " [+] Cloned successfully (Your GitHub repo is 100% untouched)."
else
    echo "Process cancelled."
    exit 0
fi

echo ""
echo "[*] Generating unified AI context file ($OUTPUT_FILE)..."
echo "# Software Project Context" > "$OUTPUT_FILE"
echo "Export Date: $(date)" >> "$OUTPUT_FILE"
echo -e "\n--- \n" >> "$OUTPUT_FILE"

cd "$TARGET_DIR"
file_count=0

find . -type f \
    -not -path '*/.*' \
    -not -path '*/node_modules*' \
    -not -path '*/venv/*' \
    -not -path '*/__pycache__*' \
    -not -path '*/build/*' \
    -not -path '*/dist/*' \
    -not -name '*.png' \
    -not -name '*.jpg' \
    -not -name '*.jpeg' \
    -not -name '*.gif' \
    -not -name '*.ico' \
    -not -name '*.pdf' \
    -not -name '*.zip' \
    -not -name '*.db' \
    -not -name '*.sqlite' \
    -not -name '*.lock' | while read -r file; do
    
    file_count=$((file_count + 1))
    echo "   [+] Processing file: $file"
    
    echo "## File Path: $file" >> "../$OUTPUT_FILE"
    echo '```' >> "../$OUTPUT_FILE"
    cat "$file" >> "../$OUTPUT_FILE"
    echo -e '\n```\n' >> "../$OUTPUT_FILE"
    echo "-----------------------------------" >> "../$OUTPUT_FILE"
done

cd ..

if [ "$choice" == "2" ]; then
    rm -rf "$TARGET_DIR"
fi

cp "$OUTPUT_FILE" /sdcard/Download/

echo ""
echo "=================================================="
echo "      Process Completed Successfully! 🎉          "
echo "=================================================="
echo " 📂 File saved in Termux: $OUTPUT_FILE"
echo " 📱 Saved directly to: Download/$OUTPUT_FILE"
echo "=================================================="
