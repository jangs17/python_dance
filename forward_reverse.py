#!/usr/bin/env python3

import socket
import sys
import logging
from argparse import ArgumentParser

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("forward_reverse.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

def get_canonical_name(hostname, retries=3):
    for attempt in range(retries):
        try:
            infolist = socket.getaddrinfo(
                hostname, None, socket.AF_UNSPEC, socket.SOCK_STREAM, 0,
                socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME
            )
            for info in infolist:
                if info[3]:  # info[3] is the canonical name
                    return info[3], info[4][0]  # info[4] is the socket address (IP)
        except socket.gaierror as e:
            logging.error(f'Forward name service failure: {e.args[1]}')
            if attempt < retries - 1:
                logging.info(f'Retrying... ({attempt + 1}/{retries})')
            else:
                sys.exit(1)

    logging.warning(f'WARNING! The IP address {infolist[0][4][0]} has no reverse name')
    sys.exit(1)

def compare_names(hostname, canonical):
    forward = hostname.lower().split('.')
    reverse = canonical.lower().split('.')

    if forward == reverse:
        logging.info('Wow, the names agree completely!')
        return

    length = min(len(forward), len(reverse))
    if (forward[-length:] == reverse[-length:] or
        (len(forward) == len(reverse) and
         forward[-length+1:] == reverse[-length+1:] and
         len(forward[-2]) > 2)):  # avoid thinking '.co.uk' means a match!
        logging.info('The forward and reverse names have a lot in common')
    else:
        logging.warning('WARNING! The reverse name belongs to a different organization')

def process_hostnames(hostnames):
    for hostname in hostnames:
        hostname = hostname.strip()
        if hostname:
            logging.info(f'Processing hostname: {hostname}')
            canonical, ip = get_canonical_name(hostname)
            logging.info(f'{hostname} has IP address {ip}')
            logging.info(f'{ip} has the canonical hostname {canonical}')
            compare_names(hostname, canonical)

def main():
    setup_logging()

    parser = ArgumentParser(description='Check whether a hostname works both forward and backward.')
    parser.add_argument('hostname', nargs='?', help='The hostname to check')
    parser.add_argument('--file', '-f', help='File containing a list of hostnames to check')

    args = parser.parse_args()

    if args.hostname:
        process_hostnames([args.hostname])
    elif args.file:
        with open(args.file, 'r') as f:
            hostnames = f.readlines()
        process_hostnames(hostnames)
    else:
        parser.print_help()
        sys.exit(2)

if __name__ == '__main__':
    main()

