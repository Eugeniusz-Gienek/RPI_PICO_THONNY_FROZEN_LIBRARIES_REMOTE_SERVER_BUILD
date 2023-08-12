SET destination_file=***WHERE_WILL_BE_MY_FILE_firmware.uf2_LOCATED***
SET remote_server_url=***IP_OR_DOMAIN_OF_MY_LOCAL_SERVER***
SET remote_server_user=***REMOTE_SERVER_SSH_USER***
SET remote_server_upload_dir=***REMOTE_SERVER_DIRECTORY_WHERE_FILES_WILL_BE_UPLOADED_TO_FOR_EXAMPLE_~/dl/uploaded_files/***
SET remote_server_upload_script=***REMOTE_SERVER_SCRIPT_WHICH_PERFORMS_MOVING_OF_THE_UPLOADED_FILES_FOR_EXAMPLE_~/copy_for_rebuild_pico.sh***
SET remote_server_execute_script=***REMOTE_SERVER_SCRIPT_WHICH_PERFORMS_FIRMWARE_BUILD_FOR_EXAMPLE_~/rebuild_pico.sh***
SET remote_server_target_build_file=***REMOTE_SERVER_EXPECTED_LOCATION_OF_THE_FIRWARE_TO_BE_AFTER_BUILD_FOR_EXAMPLE_~/pico/micropython/ports/rp2/build-PICO_W/firmware.uf2***