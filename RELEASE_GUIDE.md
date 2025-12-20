# 🚀 Building and Releasing AlgoAlly

## 📦 Building the Executable

### Prerequisites
- Python 3.8+ installed
- All dependencies installed (`pip install -r requirements.txt`)
- PyInstaller installed (`pip install pyinstaller`)

### Build Steps

1. **Navigate to project directory**
   ```bash
   cd "D:\Python Projects\SLM"
   ```

2. **Activate virtual environment**
   ```bash
   .\.venv\Scripts\activate
   ```

3. **Build the executable**
   ```bash
   pyinstaller AlgoAlly.spec
   ```

4. **Find your executable**
   - Location: `dist/AlgoAlly.exe`
   - Size: ~100-500MB (includes Python + all dependencies)

### Testing the Build

Before releasing, test the executable:

1. Copy `AlgoAlly.exe` to a different folder
2. Run it (double-click)
3. Test both OpenRouter and Local model modes
4. Verify all features work

## 📤 Uploading to GitHub

### Step 1: Push Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files (except those in .gitignore)
git add .

# Commit
git commit -m "Initial release of AlgoAlly"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/AlgoAlly.git

# Push
git push -u origin main
```

### Step 2: Create a GitHub Release

1. **Go to your GitHub repository**
   - Navigate to `https://github.com/yourusername/AlgoAlly`

2. **Click on "Releases"** (right sidebar)

3. **Click "Create a new release"**

4. **Fill in release details:**
   - **Tag version**: `v1.0.0`
   - **Release title**: `AlgoAlly v1.0.0 - Initial Release`
   - **Description**:
     ```markdown
     ## 🎉 AlgoAlly v1.0.0
     
     First stable release of AlgoAlly - Your AI DSA Companion!
     
     ### ✨ Features
     - ⚡ Fast cloud inference via OpenRouter
     - 🔒 Private local model support
     - 🎨 Modern dark UI
     - 🤖 Multiple AI model options
     - 💭 5 assistance modes (Hint, Test Cases, Complexity, Idea, Code)
     
     ### 📥 Download
     - **Windows**: Download `AlgoAlly.exe` below
     - **Other platforms**: Run from source (see README)
     
     ### 🚀 Quick Start
     1. Download `AlgoAlly.exe`
     2. Run it (no installation needed!)
     3. Get an OpenRouter API key from https://openrouter.ai/keys
     4. Start solving problems!
     
     ### 📝 Notes
     - First run may take a few seconds to start
     - Antivirus might flag it (false positive - it's safe!)
     - For local models, first download will take time
     ```

5. **Upload the executable:**
   - Click "Attach binaries by dropping them here or selecting them"
   - Select `dist/AlgoAlly.exe`
   - Wait for upload to complete

6. **Publish release**
   - Click "Publish release"

### Step 3: Update README

Make sure your README.md has the correct download link:

```markdown
#### Download Pre-built Executable (Windows)
1. Go to [Releases](https://github.com/yourusername/AlgoAlly/releases)
2. Download `AlgoAlly.exe` from the latest release
3. Run it - no installation needed!
```

## 📋 Pre-Release Checklist

Before creating a release, ensure:

- [ ] All features work correctly
- [ ] README.md is up to date
- [ ] .env.example is included
- [ ] requirements.txt is current
- [ ] .gitignore excludes sensitive files
- [ ] Executable builds without errors
- [ ] Executable runs on a clean Windows machine
- [ ] All dependencies are included in the build
- [ ] Version number is updated

## 🔄 Future Releases

For subsequent releases:

1. Make your code changes
2. Update version in relevant files
3. Rebuild executable: `pyinstaller AlgoAlly.spec`
4. Test thoroughly
5. Commit and push changes
6. Create new GitHub release with new version tag (e.g., `v1.1.0`)
7. Upload new executable

## 🐛 Troubleshooting Build Issues

### "Module not found" errors
```bash
# Add missing module to AlgoAlly.spec hiddenimports list
hiddenimports=['module_name']
```

### Executable too large
- This is normal! It includes Python + all dependencies
- Typical size: 100-500MB
- Cannot be reduced significantly for this type of app

### Antivirus flags the .exe
- Common with PyInstaller executables
- It's a false positive
- Users can add exception or run from source

### Executable won't run on other machines
- Ensure you're building on Windows for Windows
- Test on a clean machine without Python installed
- Check Windows Defender/Antivirus isn't blocking it

## 📝 Notes

- **DO NOT** commit the .exe to git (it's in .gitignore)
- **DO** upload it as a GitHub Release asset
- **DO** test on a clean machine before releasing
- **DO** include clear instructions in the release notes

## 🎯 Recommended Workflow

1. **Development**: Work on code, test locally
2. **Build**: Create executable when ready for release
3. **Test**: Verify executable works on clean machine
4. **Commit**: Push code changes to GitHub
5. **Release**: Create GitHub release with executable
6. **Announce**: Share the release link!

---

**Remember**: The executable is for distribution, not for version control!
