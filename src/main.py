#!/usr/bin/env python3

"""
Main script for rknet-dina-sync.
This script reads personnel data from an RKnet XLSX file and a DiNa-Wiki CSV file, then prepares it for CSV generation.
"""

import logging
import sys
import argparse
import pandas as pd
import re
import csv

def setup_logging():
    """
    Configures the logging settings for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def parse_arguments():
    """
    Parses command line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Read personnel data from an RKnet XLSX file and a DiNa-Wiki CSV file.'
    )
    parser.add_argument(
        '-i', '--input-rknet',
        type=str,
        required=True,
        metavar='INPUT_RKNET_FILE',
        help='Path to the RKnet XLSX input file'
    )
    parser.add_argument(
        '-d', '--input-dina',
        type=str,
        required=True,
        metavar='INPUT_DINA_FILE',
        help='Path to the DiNa-Wiki CSV input file'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        metavar='OUTPUT_FILE',
        help='Path to the output CSV file'
    )
    return parser.parse_args()

def read_personnel_data(input_file, columns=None):
    """
    Reads personnel data from the given file.

    Args:
        input_file (str): Path to the input file.
        columns (list of str): List of columns to read from the file.

    Returns:
        list of dict: List of personnel data records.
    """
    try:
        if input_file.endswith('.xlsx'):
            df = pd.read_excel(input_file, engine='openpyxl')
        else:
            df = pd.read_csv(input_file)
        logging.info(f'Data successfully read from {input_file} into memory.')
        return df.to_dict(orient='records')
    except Exception as e:
        logging.error(f'An error occurred while reading the input file {input_file}: {e}')
        sys.exit(1)

def main():
    """
    Main function to start the data reading process.
    """
    setup_logging()
    args = parse_arguments()
    rknet_data = read_personnel_data(args.input_rknet, None)
    dina_data = read_personnel_data(args.input_dina, None)

    # Find users in RKnet data who do not have a DiNa-Wiki account, checking by email
    dina_emails = {entry['E-Mail'].lower() for entry in dina_data if 'E-Mail' in entry}
    users_without_dina_account = []

    for entry in rknet_data:
        email = entry.get('E-Mail-Adresse', '').lower()
        if email not in dina_emails:
            local_part = email.split('@')[0]
            parts = local_part.split('.')
            if len(parts) == 2:
                vorname_initial = parts[0][0].lower()
                nachname_with_suffix = parts[1]
                entry['username'] = f"{vorname_initial}.{nachname_with_suffix}"
            users_without_dina_account.append(entry)

    # Log the result
    logging.info(f'Found {len(users_without_dina_account)} users without a DiNa-Wiki account.')
    for user in users_without_dina_account:
        logging.info(f"User without account: {user['Vorname']} {user['Nachname']} ({user.get('E-Mail-Adresse', 'No Email')}) - Suggested username: {user.get('username', 'No Username')}" )

    # Write the result to a CSV file
    output_file = args.output
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Benutzername', 'Voller Name', 'E-Mail', 'Gruppen'])
        for user in users_without_dina_account:
            voll_name = f'{user['Vorname']} {user['Nachname']}'
            email = user.get('E-Mail-Adresse', 'No Email')
            username = user.get('username', 'No Username')
            writer.writerow([username, voll_name, email, 'user'])
    logging.info(f'Output CSV file generated: {output_file}')

if __name__ == "__main__":
    main()
