# backup_service
Project Description:

Our project is a comprehensive Django-based backup service designed to cater to the staff of an institution and the devices connected to its network. The service offers an efficient and automated solution for backing up files with predefined extensions to a local server at scheduled times. The system eliminates the need for manual initiation by users, ensuring backups occur seamlessly even when users are offline.

The core functionality of the backup service revolves around three main entities: users, administrators, and the backup system. Users are provided with a user-friendly dashboard where they can easily view their backed-up files, receive notifications indicating the success or failure of backup operations, selectively restore specific file types, update their profiles, and register multiple devices under their account. All files are encrypted to maintain privacy and security, with only the user having access to view the decrypted files.

Administrators play a crucial role in managing the backup service. A superuser is designated with the authority to assign admin privileges to regular users. Administrators have access to an admin dashboard where they can schedule backups, select file extensions to be backed up, view backup reports (including successful and unsuccessful backups), and manage user accounts. All users, whether regular or admin, will use the same login page, ensuring a consistent and convenient login experience.

To avoid redundancy and optimize storage space, the backup system implements deduplication. It checks if a file has already been backed up and detects any changes made to it. Only the modified portions of the file are backed up, reducing storage requirements. If no changes are found, the file is not backed up again. This approach maximizes efficiency while minimizing storage consumption.

Furthermore, our backup service integrates the popular AdminLTE template, offering a sleek and responsive user interface. The blended interface enhances the user experience, providing a visually appealing and intuitive design for both users and administrators. The responsive design ensures seamless access and navigation across different devices, including desktops, tablets, and mobile devices.

Overall, our Django-based backup service offers a reliable and secure solution for automated backups. It simplifies the backup process for users, provides administrators with robust management capabilities, and ensures the confidentiality and integrity of backed-up files. By seamlessly integrating the AdminLTE template, we deliver a visually appealing and user-friendly experience for all users, enhancing the overall usability of the backup service.
