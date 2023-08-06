import base64

import requests
from Crypto.Random import get_random_bytes

from biolib import utils
from biolib.biolib_api_client.biolib_job_api import BiolibJobApi
from biolib.biolib_binary_format.base_package import InMemoryIndexableBuffer
from biolib.biolib_binary_format.encrypted_module_output import EncryptedModuleOutputWithKey
from biolib.biolib_binary_format.unencrypted_module_output import UnencryptedModuleOutput
from biolib.biolib_errors import BioLibError
from biolib.compute_node.job_worker.job_key_cache import JobKeyCacheState
from biolib.biolib_logging import logger_no_user_data, logger


class JobStorage:

    @staticmethod
    def upload_module_output(job_id: str, module_output: bytes, aes_key_string_b64: str):
        try:
            if utils.DISABLE_CLIENT_SIDE_ENCRYPTION:
                storage_module_output = UnencryptedModuleOutput.create_from_serialized_module_output(module_output)
                logger_no_user_data.debug(f'Job "{job_id}" uploading result to S3...')

            else:
                if not aes_key_string_b64:
                    raise Exception('Missing AES key for module output upload as client side encryption is enabled')
                storage_module_output = EncryptedModuleOutputWithKey(
                    aes_key_string_b64=aes_key_string_b64
                ).create_from_serialized_module_output(module_output)
                logger_no_user_data.debug(f'Job "{job_id}" uploading encrypted result to S3...')

        except Exception as error:
            logger_no_user_data.debug('Failed to get storage module output from serialized module output')
            logger.debug(f'Failed to get storage module output from serialized module output due to {error}')
            raise error

        try:
            presigned_upload_link = BiolibJobApi.get_job_storage_result_upload_url(job_id)

            request = requests.put(
                data=storage_module_output,
                url=presigned_upload_link,
                timeout=3600,  # timeout after 1 hour
            )

            if not request.ok:
                raise BioLibError('Failed to upload result to S3')

        except Exception as error:
            logger_no_user_data.debug('Failed to upload result to S3')
            logger.debug(f"Failed to upload result to S3 due to {error}")
            raise error

    @staticmethod
    def get_result(job):
        try:
            presigned_download_url = BiolibJobApi.get_job_storage_result_download_url(job['auth_token'])
            result_response = requests.get(
                url=presigned_download_url,
                timeout=3600,  # timeout after 1 hour
            )

            if not result_response.ok:
                raise BioLibError(result_response.content)

            storage_module_output = result_response.content

        except Exception as error:
            logger.debug(f'Failed to get results from S3 due to {error}')
            raise error

        if utils.BASE_URL_IS_PUBLIC_BIOLIB:
            with JobKeyCacheState() as cache_state:
                aes_key_string_b64 = cache_state[job['public_id']]

            return EncryptedModuleOutputWithKey(
                buffer=InMemoryIndexableBuffer(storage_module_output),
                aes_key_string_b64=aes_key_string_b64
            ).convert_to_serialized_module_output()

        else:
            return UnencryptedModuleOutput(
                buffer=InMemoryIndexableBuffer(storage_module_output)
            ).convert_to_serialized_module_output()

    @staticmethod
    def generate_and_store_key_buffer_for_job(job_id):
        aes_key_buffer = get_random_bytes(32)
        aes_key_string_b64 = base64.urlsafe_b64encode(aes_key_buffer).decode()

        with JobKeyCacheState() as cache_state:
            cache_state[job_id] = aes_key_string_b64

        return aes_key_string_b64
