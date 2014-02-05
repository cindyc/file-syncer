import json
import argparse
import logging

class FileSyncer(object):
    """Sync file systems using rsync and report progress
    """

    def __init__(self, host, username, password):
        """
        """
        self.host = host
        self.username = username
        self.password = password
        self.logger = logging.getLogger("FileSyncer")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())

    def get_sync_status(self):
        """Returns sync progress as json
        """
        all_result = {'total_size': '10GB',
                      'transferred_size': '3GB',
                     }
        return json.dumps(all_result, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ceck ports on source machine required by migration')
    parser.add_argument('-m', '--source-machine', required=True,
                            help='source machine hostname/ip')
    parser.add_argument('-u', '--username', default='Administrator',
                            help='The username to the source machine')
    parser.add_argument('-p', '--password', default='scloud2010',
                            help='The password to the source machine')
    args = parser.parse_args()
    syncer = FileSyncer(args.source_machine, args.username, args.password)
    sync_status_json = syncer.get_sync_status()
    print sync_status_json
    with open('sync_status.json', 'w') as json_file:
        json_file.write(sync_status_json)
