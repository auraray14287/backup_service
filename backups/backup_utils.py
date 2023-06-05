import os

def explore_drives_for_files(devices, admin_extensions):
    relevant_files = []  # List to store the relevant files
    
    for device in devices:
        backup_files = device.backupfile_set.all()
        
        # Traverse each backup file
        for backup_file in backup_files:
            file_extension = os.path.splitext(backup_file.file.name)[1].lower()
            
            # Check if the file extension matches the admin extensions
            if file_extension in admin_extensions:
                relevant_files.append(backup_file.file.path)
    
    # Perform desired actions with the relevant files
    for file_path in relevant_files:
        # Your logic here (e.g., initiate backup, update backup status, etc.)
        print("Backup initiated for file:", file_path)
